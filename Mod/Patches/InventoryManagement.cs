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
    public static float MultiplierPercentPositive = 400;
    public static float MultiplierPercentNegative = 0;


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

}