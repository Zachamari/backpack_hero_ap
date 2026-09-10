using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using UnityEngine;
using System.Collections.Generic;
using System.Linq;
using System;
using UnityEngine.InputSystem.EnhancedTouch;

namespace Backpackipelago.Patches;

public static class InventoryManagement
{
    public static float MultiplierPercentPositive = 100;
    public static float MultiplierPercentNegative = 100;


    [HarmonyPatch(typeof(Overworld_ResourceManager), nameof(Overworld_ResourceManager.ChangeResourceAmountBy), new Type[] { typeof(List<Overworld_ResourceManager.Resource>), typeof(Overworld_ResourceManager.Resource.Type), typeof(int) }), HarmonyPrefix]
    public static void ResourceMultiplier(List<Overworld_ResourceManager.Resource> resources, Overworld_ResourceManager.Resource.Type type, ref int amount)
    {

        BPHAP.Log("ChangeResourceAmountBy was run.");
        if (amount <= 0)
        {
            BPHAP.Log("Before: " + amount);
            amount = Mathf.RoundToInt(amount * (MultiplierPercentNegative / 100));
            BPHAP.Log("After: " + amount);
            return;
        }
        BPHAP.Log("Before: " + amount);
        amount = Mathf.RoundToInt(amount * (MultiplierPercentPositive / 100));
        BPHAP.Log("After: " + amount);

        // List<Overworld_ResourceManager.Resource> resources = new List<Overworld_ResourceManager.Resource>();
        // foreach (Overworld_ResourceManager.Resource r in __result)
        // {
        //     resources.Add(new Overworld_ResourceManager.Resource {
        //         type = r.type,
        //         amount = Mathf.RoundToInt(r.amount * (EfficiencyMultiplierPercent / 100))
        //     });
        //     BPHAP.Log($"Initial resource amount: {r.amount}");
        //     BPHAP.Log($"After multiplier: {r.amount * EfficiencyMultiplierPercent / 100}");
        // }
        // __result = resources;
        
    }

    public static void ReceiveInventoryItem(string itemName)
    {
        BPHAP.Log("Adding item to Haversack inventory: " + itemName);

        Item2 item = GameInstance.DebugItemManagerInstance.GetItem2ByName(itemName);
        if (item == null)
        {
            BPHAP.LogError("ERROR: Item with itemName " + itemName + " wasn't found in DIM (returned null).");
            BPHAP.Log("Items in DIM:");
            foreach (Item2 item2 in Item2.allItems)
            {
                BPHAP.Log("Item: " + item2);
            }
            return;
        }

        GameInstance.MetaProgressSaveManagerItems.AddItem(item); // adds item to haversack inventory

        // maybe eventually make a popup window here

    }

}