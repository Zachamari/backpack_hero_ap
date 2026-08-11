using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using UnityEngine;
using System.Collections.Generic;
using System.Linq;
using System;
using UnityEngine.InputSystem.EnhancedTouch;

namespace Backpackipelago.Patches;

public static class GameInstance
{
    public static MetaProgressSaveManager MetaProgressSaveManagerMissions = null;
    public static MetaProgressSaveManager MetaProgressSaveManagerItems = null;
    public static RunTypeSelector RunTypeSelector = new RunTypeSelector();

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.Load)), HarmonyPostfix]
    public static void GetMetaProgressSaveManagerInstance(ref MetaProgressSaveManager __instance)
    {
        BPHAP.Log("Instance missions: ");
        foreach (string mission in __instance.missionsUnlocked)
        {
            BPHAP.Log(mission);
        }
        BPHAP.Log("\nInstance items: ");
        foreach(string item in __instance.itemsUnlocked)
        {
            BPHAP.Log(item);
        }
        
        BPHAP.Log("MetaProgressSaveManager instance stored for Missions: " + __instance.ToString());
        MetaProgressSaveManagerMissions = __instance;

        // For some reason, there's multiple instances of MetaProgressSaveManager being thrown around, and this is really the only way I can think of to differentiate them
        if (__instance.itemsUnlocked.Count > 6)
        {
            BPHAP.Log("MetaProgressSaveManager instance stored for Items: " + __instance.ToString());
            MetaProgressSaveManagerItems = __instance;
        }

        if (ItemReceived.missionQueue.Count > 0)
        {
            foreach (string mission in ItemReceived.missionQueue)
            {
                ItemReceived.ReceiveNewMission(mission);
            }
            ItemReceived.missionQueue.Clear();
        }

        if (ItemReceived.itemQueue.Count > 0)
        {
            foreach (string itemName in ItemReceived.itemQueue)
            {
                ItemReceived.ReceiveNewItem(itemName);
            }
            ItemReceived.itemQueue.Clear();
        }
    
        if (ItemReceived.metaQueue.Count > 0)
        {
            foreach (int val in ItemReceived.metaQueue)
            {
                ItemReceived.ReceiveNewMetaProgress(val);
            }
            ItemReceived.metaQueue.Clear();
        }        
        
        if (ItemReceived.costumeQueue.Count > 0)
        {
            foreach (string costume in ItemReceived.costumeQueue)
            {
                ItemReceived.ReceiveNewCostume(costume);
            }
            ItemReceived.costumeQueue.Clear();
        }

    }

    // [HarmonyPatch(typeof(RunTypeSelector), nameof(RunTypeSelector.GetProperties)), HarmonyPostfix]
    // public static void GetMetaProgressSaveManagerInstance(ref RunTypeSelector __instance)
    // {
    //     if (RunTypeSelector == null) {
    //         BPHAP.Log("RunTypeSelector instance stored.");
    //         RunTypeSelector = __instance;
    //     }
    // }

    public static Overworld_BuildingManager BuildingInstance = null;

    [HarmonyPatch(typeof(Overworld_BuildingManager), nameof(Overworld_BuildingManager.GetBuildings)), HarmonyPostfix]
    public static void GetOverworldBuidingManagerInstance(ref Overworld_BuildingManager __instance)
    {
        if (BuildingInstance == null) {
            BuildingInstance = __instance;
            BPHAP.Log("BuildingManager instance stored: " + __instance.ToString());
        }

        if (ItemReceived.buildingQueue.Count > 0)
        {
            foreach (string building in ItemReceived.buildingQueue)
            {
                ItemReceived.ReceiveNewBuilding(building);
            }
        }

        if (ItemReceived.tileQueue.Count > 0)
        {
            foreach (string tile in ItemReceived.tileQueue)
            {
                ItemReceived.ReceiveNewPath(tile);
            }
            ItemReceived.tileQueue.Clear();
        }
    }


    [HarmonyPatch(typeof(LoadStoryGame), nameof(LoadStoryGame.LoadStoryGameCommand)), HarmonyPostfix]
    public static void TempConnectLate()
    {
        BPHAP.APClient.Connect();
    }

    public static ItemStorage ItemStorage = null;


    // Turns out this function specifically puts them in the window where you sell items in the shop; find a better function to put them directly in the inventory instead
    [HarmonyPatch(typeof(ItemStorage), nameof(ItemStorage.AddStoredItems)), HarmonyPrefix]
    public static void GetItemStorageInstance(ref string[] itemsToAdd, ref ItemStorage __instance)
    {

        BPHAP.Log("Items being added vanilla: "); 
        foreach (string item in itemsToAdd)
        {
            BPHAP.Log(item);
            ItemsToAddToStorage.Add(item);
        }

        itemsToAdd = ItemsToAddToStorage.ToArray();

        if (!allowDebug)
        {
            ItemsToAddToStorage.Clear();
        }

        if (ItemStorage == null) {
            BPHAP.Log("ItemStorage instance stored.");
            ItemStorage = __instance;
        }
    }
    



    private static List<string> ItemsToAddToStorage = [];
    public static HashSet<string> ItemsInPool = [];

    // Also move to a different file
    [HarmonyPatch(typeof(Overworld_BuildingInterface.Research), nameof(Overworld_BuildingInterface.Research.Available)), HarmonyPrefix]
    public static bool ShowAllResearch(Overworld_BuildingInterface.Research __instance, ref bool __result)
    {
        // This makes all research show up in the research menus no matter which items you have.
        // The only problem is that, for whatever reason, the game hangs for a while if it tries to display a mission that requires a character that you don't have.
        // So, to prevent that, only mess with the menu if the research doesn't unlock a mission.
        // This is accounted for in the apworld's logic.
        if (__instance.mission) {
            return true;
        } 
        __result = true;
        return false;

    }



    public static HashSet<string> receivedItems = [];
    private static bool allowDebug = false;

    // Remove later or replace with function to get copies of items from server
    [HarmonyPostfix]
    [HarmonyPatch(typeof(ItemSpawner))]
    [HarmonyPatch("GetAllValidItems")]
    public static void DebugFreeItems(List<Item2> __result)
    {

        foreach (Item2 item in __result)
        {
            if (receivedItems.Contains(Item2.GetDisplayName(item.name)))
            {
                BPHAP.Log("Received item found in pool: " + Item2.GetDisplayName(item.name));
            }
        }

        if (!allowDebug) {
            return;
        }

        BPHAP.Log("Attempting to add items to inventory...");
        try {
            
            foreach (Item2 item in __result)
            {
                BPHAP.Log("Item: " + item.name + $" (Display name: {item.displayName})");
                ItemsToAddToStorage.Add(item.name);
                // ItemsInPool.Add(Item2.GetDisplayName(item.name));
                // if (LocationChecked.blockedItems.Contains(Item2.GetDisplayName(item.name)))
                // {
                //     BPHAP.LogError("Item that was force-completed was found in pool: " + item.name);
                // }
            }
            // BPHAP.Log("Adding the following items to inventory: ");
            // foreach (string item in ItemsToAddToStorage)
            // {
            //     BPHAP.Log("Item in storage: " + item);
            // }


        } catch (Exception e)
        {
            BPHAP.LogError("Exception caught while adding items to metainventory: " + e);
        }
    }



}