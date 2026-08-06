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

    public static HashSet<int> checkedLocations = new HashSet<int>(); 
    
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
                // If save data is cleared, the memory will be cleared to allow sending the checks again

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

        int itemId = (int) receivedItem.ItemId;
        BPHAP.Log($"Received {receivedItem.ItemName} from {receivedItem.Player.Name}!");

        if (itemId >= TRAP_ID_OFFSET) {

            // traps go here

        }
        else

        if (itemId >= FILLER_ID_OFFSET) {


            // filler goes here
        }

        // etc

        else {
            BPHAP.Log($"Received item {receivedItem.ItemName} was not recognized. Contact the mod developer if you see this message! (ID = {itemId})");
        }
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


    // todo: fill these numbers
    public const int TRAP_ID_OFFSET = 100;
    public const int FILLER_ID_OFFSET = 200;  
}