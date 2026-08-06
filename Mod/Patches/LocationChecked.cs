using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using JetBrains.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.InputSystem.EnhancedTouch;

namespace Backpackipelago.Patches;

public static class LocationChecked
{

    // The list of completed researches used ingame is a private variable I have no way of accessing, so I just make my own list and force the game to use that instead
    public static HashSet<string> ResearchesComplete = [];

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.AddNewResearch)), HarmonyPrefix]
    public static void AutoCollectResearch(string name, ref string nameAndValues)
    {

        // string data;
        // if (nameAndValues.Contains(name))
        // {
        //     data = nameAndValues.Remove(0, name.Length);
        // } else
        // {
        //     BPHAP.LogError("Item " + nameAndValues + " does not match expected format. Expected name: " + name);
        //     return;
        // }
        

        if (nameAndValues.Contains("0"))
        {

            // // Use this part to auto-complete collected/released locations
            // nameAndValues = nameAndValues.Replace('0', '1');
            // BPHAP.Log($"Item {name} was forced complete (new code: {nameAndValues})");
            // ResearchesComplete.Add(Item2.GetDisplayName(name));


            return;
        }



        BPHAP.Log($"Research completed for item {name} (full code: {nameAndValues})");

        // (preventing this function from running does nothing, item is still unlocked like normal)

    }

    // [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.ResearchComplete)), HarmonyPrefix]
    // public static bool CompletedResearchCheckOverride(MetaProgressSaveManager.Research r, ref bool __result)
    // {
    //     if (ResearchesComplete.Contains(r.item.name)) {
    //         __result = true;
    //     } else { 
    //         __result = false; 
    //     }

    //     return false;
    // }


    [HarmonyPatch(typeof(PerformSpecialAction), nameof(PerformSpecialAction.OnStart)), HarmonyPrefix]
    public static bool SendOtherChecks(PerformSpecialAction __instance)
    {

        BPHAP.Log($"Check found with actionType {__instance.actionType}.");

        switch (__instance.actionType)
        {
            case PerformSpecialAction.ActionType.AddBuilding:
                BPHAP.Log($"Building unlocked: {__instance.genericObject}");
                // send check here, make return false
                break;
            case PerformSpecialAction.ActionType.UnlockCharacter:
                BPHAP.Log($"Character unlocked: {__instance.character}");
                // send check here, make return false
                break;
            case PerformSpecialAction.ActionType.UnlockCostume:
                BPHAP.Log($"Costume unlocked: {__instance.costume}");
                // send check here, make return false
                break;
        }

        return true; // remove after debugging

    }


    public static bool newItemIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.UnlockItem)), HarmonyPrefix]
    public static bool PreventVanillaItemUnlock(Item2 item)
    {
        if (newItemIsFromAP)
        {
            newItemIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Item " + item.name + " was prevented from being unlocked.");

            // Send check here

            return false;
        }
    }


    public static bool newMissionIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.AddMission)), HarmonyPrefix]
    public static bool PreventVanillaMissionUnlock(Missions m)
    {
        if (newMissionIsFromAP)
        {
            newMissionIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Mission " + m.name + " was prevented from being unlocked.");

            // Send check here

            return false;
        }
    }


    public static bool newCostumeIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.UnlockCostume)), HarmonyPrefix]
    public static bool PreventVanillaCostumeUnlock(RuntimeAnimatorController __0)
    {
        if (newCostumeIsFromAP)
        {
            newCostumeIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Costume " + __0.name + " was prevented from being unlocked.");

            // Send check here

            return false;
        }
    }


    public static bool newBuildingIsFromAP = false;

    [HarmonyPatch(typeof(Overworld_BuildingManager), nameof(Overworld_BuildingManager.AddBuilding), new Type[] { typeof(string) }), HarmonyPrefix]
    public static bool PreventVanillaBuildingUnlock(string __0)
    {
        if (newBuildingIsFromAP)
        {
            newBuildingIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Building " + __0 + " was prevented from being unlocked.");

            // Send check here

            return false;
        }
    }

    [HarmonyPatch(typeof(Overworld_BuildingManager), nameof(Overworld_BuildingManager.AddBuilding), new Type[] { typeof(GameObject) }), HarmonyPrefix]
    public static bool PreventVanillaBuildingUnlockOverload(GameObject __0)
    {
        if (newBuildingIsFromAP)
        {
            newBuildingIsFromAP = false;
            return true;
        }
        else
        {
            if (__0.name == "Store")
            {
                // The store needs to remain at its vanilla location for now because otherwise the game gets softlocked immediately 
                // (also nearly every location would need to logically require store anyway so there's not much reason to shuffle it)
                BPHAP.Log("Store unlocked!");
                return true;
            }
            BPHAP.Log("Building " + __0.name + " was prevented from being unlocked.");
            return false;
        }
    }

    [HarmonyPatch(typeof(Overworld_BuildingManager), nameof(Overworld_BuildingManager.AddTile), new Type[] { typeof(string) }), HarmonyPrefix]
    public static bool PreventVanillaTileUnlock(string __0)
    {
        if (newBuildingIsFromAP)
        {
            newBuildingIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Tile " + __0 + " was prevented from being unlocked.");

            // Send check here

            return false;
        }
    }


    public static bool metaProgressIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.AddMetaProgressMarker), new Type[] { typeof(MetaProgressSaveManager.MetaProgressMarker) }), HarmonyPrefix]
    public static bool HandleMetaProgressMarker(MetaProgressSaveManager.MetaProgressMarker m)
    {
        BPHAP.Log("AddMetaProgressMarker was run; Marker was added with enum value of " + (int)m);

        switch ((int)m)
        {
            case 6:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Tote unlocked; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 7:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("CR-8 unlocked; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 8:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Satchel unlocked; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 9:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Pochette unlocked; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 25:
                BPHAP.Log("Archery unlocked.");
                return true;
            case 22:
                BPHAP.Log("Magic unlocked.");
                return true;
            case 21:
                BPHAP.Log("Matthew unlocked.");
                return true;
                // if (!metaProgressIsFromAP) {
                //     BPHAP.Log("Matthew unlocked; Blocking progress marker.");
                //     return false;
                // } else { return true; }
            // case 28:
            //     if (!metaProgressIsFromAP) {
            //         BPHAP.Log("Vision of Danger unlocked; Blocking progress marker.");
            //         // Send check
            //         return false;
            //     } else { return true; }
            case 50:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Bramble research finished; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 51:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Deep Cave research finished; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 52:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Enchanted Swamp research finished; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 53:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Magma Core research finished; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 54:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Frozen Heart research finished; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 100:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Forges unlocked; Blocking progress marker.");
                    // Send check
                    return false;
                } else { return true; }
            case 148:
                BPHAP.Log("You win! Conglaturations!");
                BPHAP.APClient.Goal();
                return true;
            default: return true;
        }
    }

}