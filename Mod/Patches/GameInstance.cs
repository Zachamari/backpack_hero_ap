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
    public static MetaProgressSaveManager MetaProgressSaveManager = null;
    public static RunTypeSelector RunTypeSelector = new RunTypeSelector();

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.Load)), HarmonyPostfix]
    public static void GetMetaProgressSaveManagerInstance(ref MetaProgressSaveManager __instance)
    {
        if (MetaProgressSaveManager == null) {
            BPHAP.Log("MetaProgressSaveManager instance stored.");
            MetaProgressSaveManager = __instance;
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




    private static bool allowDebug = false;

    // Remove later or replace with function to get copies of items from server
    [HarmonyPostfix]
    [HarmonyPatch(typeof(ItemSpawner))]
    [HarmonyPatch("GetAllValidItems")]
    public static void DebugFreeItems(List<Item2> __result)
    {

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