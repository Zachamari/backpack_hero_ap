using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using System.Threading.Tasks;
using Archipelago.MultiClient.Net.Exceptions;
using System.Net.WebSockets;
using Backpackipelago;
using Backpackipelago.Patches;

namespace Backpackipelago.Archipelago;

public class ArchipelagoClient
{
    public const string APVersion = "0.6.7";
    private const string Game = "Backpack Hero";

    public static bool Authenticated;
    private bool attemptingConnection;
    private static bool initialConnectionStepsComplete = false;


    public static ArchipelagoData ServerData = new ArchipelagoData();
    // private DeathLinkHandler DeathLinkHandler;
    private ArchipelagoSession session;

    /// <summary>
    /// call to connect to an Archipelago session. Connection info should already be set up on ServerData
    /// </summary>
    /// <returns></returns>
    public void Connect()
    {
        if (Authenticated || attemptingConnection) return;

        try
        {

            session = ArchipelagoSessionFactory.CreateSession(ServerData.Uri);
            SetupSession();
        }
        catch (Exception e)
        {
            BPHAP.LogError(e.ToString());
        }

        TryConnect();
    }

    /// <summary>
    /// add handlers for Archipelago events
    /// </summary>
    private void SetupSession()
    {
        session.MessageLog.OnMessageReceived += message => BPHAP.Log(message.ToString());
        session.Items.ItemReceived += OnItemReceived;
        session.Socket.ErrorReceived += OnSessionErrorReceived;
        session.Socket.SocketClosed += OnSessionSocketClosed;

        

    }

    /// <summary>
    /// attempt to connect to the server with our connection info
    /// </summary>
    private void TryConnect()
    {
        try
        {
            // it's safe to thread this function call but unity notoriously hates threading so do not use excessively
            ThreadPool.QueueUserWorkItem(
                _ => HandleConnectResult(
                    session.TryConnectAndLogin(
                        Game,
                        ServerData.SlotName,
                        ItemsHandlingFlags.AllItems, // TODO make sure to change this line
                        new Version(APVersion),
                        password: ServerData.Password,
                        requestSlotData: true // ServerData.NeedSlotData
                    )));
        }
        catch (Exception e)
        {
            BPHAP.LogError(e.ToString());
            HandleConnectResult(new LoginFailure(e.ToString()));
            attemptingConnection = false;
        }
    }

    /// <summary>
    /// handle the connection result and do things
    /// </summary>
    /// <param name="result"></param>
    private void HandleConnectResult(LoginResult result)
    {
        string outText;
        if (result.Successful)
        {
            var success = (LoginSuccessful)result;

            ServerData.SetupSession(success.SlotData, session.RoomState.Seed);
            Authenticated = true;

            // DeathLinkHandler = new(session.CreateDeathLinkService(), ServerData.SlotName);
            session.Locations.CompleteLocationChecksAsync(ServerData.CheckedLocations.ToArray());
            outText = $"Successfully connected to {ServerData.Uri} as {ServerData.SlotName}!";

            checkedLocations = ServerData.CheckedLocations.ToHashSet<long>();

            // if (Plugin.deathLinkEnabled)
            // {
            //     DeathLinkHandler.SetDeathLink(true);
            // }

            BPHAP.Log(outText);

            if (!initialConnectionStepsComplete) {
                
                // Everything here only needs to be done upon initial connection

                // Retrieve YAML settings from server 
                try {

                    // Get YAML settings from server here

                } catch (Exception e)
                {
                    BPHAP.LogError("Error while reading YAML information: \n" + e);
                }
                
                // // Stole this bit from Hollow Knight's AP, sorry :p
                // // This is used to get all of the slot's location data and store it for later
                // BPHAP.Log("Scouting locations...");
                // Task<Dictionary<long, ScoutedItemInfo>> scoutTask = session.Locations.ScoutLocationsAsync(session.Locations.AllLocations.ToArray());
                // scoutTask.Wait();
                // BPHAP.Log("Locations scouted!");
                // Dictionary<long, ScoutedItemInfo> scoutResult = scoutTask.Result;
                    
                // ProcessScoutedLocationData(scoutResult);
                
                // // Get the seed from the server to make/get the save file name, then try to load it
                // APSaveData.roomSeed = session.RoomState.Seed;
                // APSaveData.saveFilePath = $"BepInEx/plugins/WeLoveArchipelago/APSaveData/AP_{APSaveData.roomSeed}.json";
                // APSaveData.LoadAPDataFromFile();

                // Music Rando stuff, could probably be moved elsewhere later
                
                initialConnectionStepsComplete = true;
                
            }
        }
        else
        {
            var failure = (LoginFailure)result;
            outText = $"Failed to connect to {ServerData.Uri} as {ServerData.SlotName}.";
            outText = failure.Errors.Aggregate(outText, (current, error) => current + $"\n    {error}");

            BPHAP.LogError(outText);

            Authenticated = false;
            Disconnect();
        }

        BPHAP.Log(outText);
        attemptingConnection = false;
    }


    public static Dictionary<int, ScoutedLocationData> scoutedLocations = new Dictionary<int, ScoutedLocationData>();

    public static void ProcessScoutedLocationData(Dictionary<long, ScoutedItemInfo> scoutResult){
        
        foreach (KeyValuePair<long, ScoutedItemInfo> scout in scoutResult)
        {
            try {

                int locationId = (int) scout.Key;   // I store it as an int here bc the location sending function uses integers and quite frankly I don't want to bother changing all that for a likely unnoticeable decrease in memory usage. Maybe later if I need to optimize it better
                BPHAP.Log($"Processing scouted location data for location {locationId}...");
                ScoutedItemInfo item = scout.Value;
                string itemName = item.ItemName ?? $"?Item {item.ItemId}";
                string locationName = item.LocationName ?? $"?Location {item.LocationId}";
                string receivingPlayer = item.Player.Alias ?? "someone else";
                string receivingGame = item.Player.Game ?? "Unknown Game";
                string itemClass = item.Flags.ToString() ?? "None";
                bool isLocalItem = item.IsReceiverRelatedToActivePlayer; 
                scoutedLocations.Add(locationId, new ScoutedLocationData(locationName, itemName, receivingPlayer, receivingGame, itemClass, isLocalItem));  // Store all the above information in a new ScoutedLocationData object that can be called using the location ID

            } catch (Exception e) {
                BPHAP.LogError($"Error while collecting scouted location data! \n{e}");
            }
        }
    }

    /// <summary>
    /// something went wrong, or we need to properly disconnect from the server. cleanup and re null our session
    /// </summary>
    public void Disconnect()
    {
        try {
            BPHAP.Log("Disconnecting from server...");
            session?.Socket.DisconnectAsync();
            session = null;
            Authenticated = false;
        } catch (Exception e) {
            BPHAP.LogError("Error while disconnecting from server: \n" + e);
            session = null;
            Authenticated = false;
        }
    }

    public void SendMessage(string message)
    {
        session.Socket.SendPacketAsync(new SayPacket { Text = message });
    }

    public HashSet<long> checkedLocations = new HashSet<long>(); 
    
    public void SendCheck(string locationName)
    {
        try {
            string location = locationName;

    	    if (location.Contains(" Variant"))
	        {
	    	    location = location.Substring(0, location.IndexOf(" Variant"));
        	}
    	    if (location.Contains(" (UnityEngine.GameObject)"))
	        {
	    	    location = location.Substring(0, location.IndexOf(" (UnityEngine.GameObject)"));
        	}

            BPHAP.Log("Sending check for location: " + location);
            SendCheck(BPHAP.APIDs.InternalUnlockToLocationID[location]);

        } catch (Exception e)
        {
            BPHAP.LogError($"ERROR: Location with name '{locationName}' was unrecognized. Failed to send check.\n{e}");
        }
    }

	public void SendCheck(int location) {


        // if (!scoutedLocations.ContainsKey(location))
        // {
        //     // If the location isn't in the multiworld, don't bother
        //     return;
        // }

        BPHAP.Log($"Sending check: {location}");

        // BPHAP.Log("Checked Locations:");
        // foreach (int i in checkedLocations) {
        //     string j = $"{i}";
        //     BPHAP.Log(j);
        // }

        if (!checkedLocations.Contains(location)) {

            try {

                session.Locations.CompleteLocationChecks(location);
                checkedLocations.Add(location);  // Add the location to the list of cached locations so it doesn't try to send the same check 9 billion times

            } catch (NullReferenceException e) {

                BPHAP.LogError("Failed to send location check. The server may be down or you may have otherwise lost connection to the AP server. Check that the server is still running and reconnect. \n Full error message: \n" + e);    
            
            } catch (Exception e) {

                BPHAP.LogError($"An unexpected error occurred: {e}");

            }

        } else {

            BPHAP.Log($"Check {location} was already sent.");
        
        }
	}

	public void Goal() {
		session.SetGoalAchieved();
	}

	// public void CheckDeathLink(MainGameManager man) {
	// 	DeathLinkHandler.KillPlayer(man);
	// }

	// public void SendDeathLink(string deathMessage) {
	// 	DeathLinkHandler.SendDeathLink(deathMessage);
	// }

    public static List<long> ReceivedProgressiveMissions = []; 
    public static List<long> ReceivedImportantProgression = [];

    /// <summary>
    /// we received an item so reward it here
    /// </summary>
    /// <param name="helper">item helper which we can grab our item from</param>
    private void OnItemReceived(ReceivedItemsHelper helper) {
        
        var receivedItem = helper.DequeueItem();

        if (helper.Index <= ServerData.Index) return;

        ServerData.Index++;

        // if items can be received while in an invalid state for actually handling them, they can be placed in a local
        // queue/collection to be handled later

        long itemId = receivedItem.ItemId;

        BPHAP.Log($"Received {receivedItem.ItemName} from {receivedItem.Player.Name}!");

        if (itemId >= GENERIC_FILLER_OFFSET) {

            // generic filler getting added to inventory goes here

            return;

        }
        

        if (itemId >= ALTERNATE_COSTUMES_OFFSET) {

            ItemReceived.ReceiveNewCostume(APWorldIDs.GetInternalCostumeName(receivedItem.ItemName));

            return;
        }


        if (itemId >= AREA_KEYS_OFFSET) { // Range includes characters and other progression

            ReceivedImportantProgression.Add(itemId);

            // this could technically be more optimized if I used the item IDs instead of the item names, but whateverrrrrrrrr, this is more readable
            switch (receivedItem.ItemName) {

                case "Key to the Bramble":
                    ItemReceived.ReceiveNewMetaProgress(50);
                    break;
                case "Key to the Deep Caves":
                    ItemReceived.ReceiveNewMetaProgress(51);
                    break;
                case "Key to the Enchanted Swamp":
                    ItemReceived.ReceiveNewMetaProgress(52);
                    break;
                case "Key to the Magma Core":
                    ItemReceived.ReceiveNewMetaProgress(53);
                    break;
                case "Key to the Frozen Heart":
                    ItemReceived.ReceiveNewMetaProgress(54);
                    break;

                case "Tote":
                    ItemReceived.ReceiveNewMetaProgress(6);
                    break;
                case "CR-8":
                    ItemReceived.ReceiveNewMetaProgress(7);
                    break;
                case "Satchel":
                    ItemReceived.ReceiveNewMetaProgress(8);
                    break;
                case "Pochette":
                    ItemReceived.ReceiveNewMetaProgress(9);
                    break;
                case "Purse":
                    break;

                default:
                    BPHAP.LogError($"ERROR: Progression Item {receivedItem.ItemName} was not recognized.");
                    break;
            }
            return;
        }

        
        if (itemId >= BUILDING_OFFSET_TILE) {

            ItemReceived.tileQueue.Add(receivedItem.ItemName);
            return;

        }

        if (itemId >= BUILDING_OFFSET_PROG) { // range includes non-prog buildings as well

            ItemReceived.buildingQueue.Add(APWorldIDs.GetInternalBuildingName(receivedItem.ItemName));
            return;
            
        }

        if (itemId >= QUEST_OFFSET_PROGRESSIVE) {

            string name = receivedItem.ItemName.Substring(19);
            if (ReceivedProgressiveMissions.Contains(itemId))
            {
                ItemReceived.ReceiveNewMission(name + " 2");
                return;
            }
            if (name == "Scissors")
            {
                ItemReceived.ReceiveNewMission("Scissors"); // Scissors 1 is just called Scissors internally (without the 1), so it needs a special exception
                ReceivedProgressiveMissions.Add(itemId);
                return;
            }
            ItemReceived.ReceiveNewMission(name + " 1");
            ReceivedProgressiveMissions.Add(itemId);
            return;
            
        }

        if (itemId >= QUEST_OFFSET) {

            string name = APWorldIDs.GetInternalMissionName(receivedItem.ItemName.Substring(7));
            ItemReceived.ReceiveNewMission(name);
            return;
            
        }

        if (itemId >= ITEM_OFFSET) { // no reason to have this comparison here other than for consistency since ITEM_OFFSET == 0. but i like consistency

            string name = APWorldIDs.GetInternalItemName(receivedItem.ItemName);
            ItemReceived.ReceiveNewItem(name);
            return;
            
        }

        

        BPHAP.Log($"Received item {receivedItem.ItemName} was not recognized. Contact the mod developer if you see this message! (ID = {itemId})");
    }

    /// <summary>
    /// something went wrong with our socket connection
    /// </summary>
    /// <param name="e">thrown exception from our socket</param>
    /// <param name="message">message received from the server</param>
    private void OnSessionErrorReceived(Exception e, string message)
    {
        BPHAP.LogError(e.ToString());
        BPHAP.Log(message);
    }

    /// <summary>
    /// something went wrong closing our connection. disconnect and clean up
    /// </summary>
    /// <param name="reason"></param>
    private void OnSessionSocketClosed(string reason)
    {
        BPHAP.LogError($"Connection to Archipelago lost: {reason}");
        Disconnect();
    }


    public const int ITEM_OFFSET = 0;
    public const int QUEST_OFFSET = 1000;
    public const int QUEST_OFFSET_PROGRESSIVE = 1500;
    public const int BUILDING_OFFSET_PROG = 2000;
    public const int BUILDING_OFFSET_USEFUL = 2100;
    public const int BUILDING_OFFSET_DECOR = 2200;
    public const int BUILDING_OFFSET_TILE = 2300;
    public const int AREA_KEYS_OFFSET = 2500;
    public const int CHARACTERS_OFFSET = 2550;
    public const int OTHER_PROGRESSION_OFFSET = 2600;
    public const int ALTERNATE_COSTUMES_OFFSET = 2800;
    public const int GENERIC_FILLER_OFFSET = 3000;

}