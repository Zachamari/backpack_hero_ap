using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.InputSystem.EnhancedTouch;
using CreepyUtil.Archipelago.ApClient;
using Backpackipelago.Archipelago;

namespace Backpackipelago.Patches;

public static class LocationChecked
{

    // The list of completed researches used ingame is a private variable I have no way of accessing, so I just make my own list and force the game to use that instead
    public static HashSet<string> researchesComplete = [];
    public static HashSet<string> researchesToScout = [];

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
            // return;

            // if (scoutHints == true)
            researchesToScout.Add(name);

            return;
        }



        BPHAP.Log($"Research completed for item {name} (full code: {nameAndValues})");
        BPHAP.APClient.SendCheck(APWorldIDs.GetInternalItemName(name));

        // (preventing this function from running does nothing, item is still unlocked like normal)

    }

    [HarmonyPatch(typeof(Overworld_BuildingInterfaceLauncher), nameof(Overworld_BuildingInterfaceLauncher.CloseInterface)), HarmonyPostfix]
    public static void CreateResearchHints()
    {
        BPHAP.Log("CloseInterface was run.");
        if (researchesToScout.Count > 0)
        {

            long[] locationIds = new long[researchesToScout.Count];
            int index = 0;

            foreach (string locationName in researchesToScout)
            {
                BPHAP.Log("Scouting " + locationName);
                try 
                {
                    locationIds[index] = BPHAP.APIDs.InternalUnlockToLocationID[APWorldIDs.FixLocationName(locationName)];
                    index++;
                }
                catch (Exception e)
                {
                    BPHAP.LogError("ERROR: Unable to identify location ID for location " + locationName + ". \n" + e);
                }
            }
            if (index != locationIds.Count())
            {
                // Removing any ids of 0 because otherwise we get disconnected when scouting the hints
                Array.Resize(ref locationIds, index);
            }

            BPHAP.APClient.ScoutServerHints(locationIds);
            researchesToScout.Clear();

        }
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


    // Not sure if this patch is needed anymore
    [HarmonyPatch(typeof(PerformSpecialAction), nameof(PerformSpecialAction.OnStart)), HarmonyPrefix]
    public static bool SendOtherChecks(PerformSpecialAction __instance)
    {

        BPHAP.Log($"Check found with actionType {__instance.actionType}.");

        switch (__instance.actionType)
        {
            case PerformSpecialAction.ActionType.AddBuilding:
                BPHAP.Log($"Building unlocked: {__instance.genericObject}");
                BPHAP.APClient.SendCheck(__instance.genericObject.ToString());
                break;
            case PerformSpecialAction.ActionType.UnlockCharacter:
                BPHAP.Log($"Character unlocked: {__instance.character}");
                BPHAP.APClient.SendCheck(__instance.character.ToString());
                // send check here, make return false?
                break;
            case PerformSpecialAction.ActionType.UnlockCostume:
                BPHAP.Log($"Costume unlocked: {__instance.costume}");
                SendCostumeCheck(__instance.costume.ToString());
                // send check here, make return false?
                break;
        }

        return true; // remove after debugging

    }

    private static void SendCostumeCheck(string costumeName)
    {
        
            if (costumeName.Contains("Purse"))
            {
                // Costume location IDs are all in a row and should always be sent progressively (since that's how it functions in the vanilla game)
                for (int i = 2; i < 7; i++)
                { 
                    if (!BPHAP.APClient.checkedLocations.Contains(i + NPC_LOCATION_OFFSET_VIV))
                    {
                        BPHAP.APClient.SendCheck(i + NPC_LOCATION_OFFSET_VIV);
                        return;
                    }
                }
                BPHAP.LogError("Unable to send costume check for item " + costumeName);          
                return;  
            }
            if (costumeName.Contains("Satchel"))
            {
                for (int i = 10; i < 12; i++)
                { 
                    if (!BPHAP.APClient.checkedLocations.Contains(i + NPC_LOCATION_OFFSET_VIV))
                    {
                        BPHAP.APClient.SendCheck(i + NPC_LOCATION_OFFSET_VIV);
                        return;
                    }
                }
                BPHAP.LogError("Unable to send costume check for item " + costumeName);       
                return;
            }
            if (costumeName.Contains("Tote"))
            {
                for (int i = 15; i < 17; i++)
                { 
                    if (!BPHAP.APClient.checkedLocations.Contains(i + NPC_LOCATION_OFFSET_VIV))
                    {
                        BPHAP.APClient.SendCheck(i + NPC_LOCATION_OFFSET_VIV);
                        return;
                    }
                }
                BPHAP.LogError("Unable to send costume check for item " + costumeName);       
                return;
            }
            if (costumeName.Contains("Pochette"))
            {
                for (int i = 20; i < 22; i++)
                { 
                    if (!BPHAP.APClient.checkedLocations.Contains(i + NPC_LOCATION_OFFSET_VIV))
                    {
                        BPHAP.APClient.SendCheck(i + NPC_LOCATION_OFFSET_VIV);
                        return;
                    }
                }
                BPHAP.LogError("Unable to send costume check for item " + costumeName);       
                return;
            }
            if (costumeName.Contains("CR8"))
            {
                for (int i = 25; i < 27; i++)
                { 
                    if (!BPHAP.APClient.checkedLocations.Contains(i + NPC_LOCATION_OFFSET_VIV))
                    {
                        BPHAP.APClient.SendCheck(i + NPC_LOCATION_OFFSET_VIV);
                        return;
                    }
                }
                BPHAP.LogError("Unable to send costume check for item " + costumeName);       
                return;
            }

            BPHAP.LogError("ERROR: Internal costume name does not contain a character's name: " + costumeName);
    }

    public static bool newItemIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.UnlockItem)), HarmonyPrefix]
    public static bool PreventVanillaItemUnlockAndSendCheck(Item2 item)
    {
        if (newItemIsFromAP)
        {
            BPHAP.Log("Allowing item " + item.name + " to be unlocked from AP.");
            newItemIsFromAP = false;
            return true;
        }
        else
        {
            BPHAP.Log("Item " + item.name + " was prevented from being unlocked.");

            BPHAP.APClient.SendCheck(item.name);

            return false;
        }
    }


    [HarmonyPatch(typeof(RunTypeManager), nameof(RunTypeManager.AssignRunType)), HarmonyPrefix]
    public static void DetectMissionStart()
    {
        BPHAP.Log("Mission just started.");
        missionJustStarted = true;
    }
    
    private static bool missionJustStarted = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.AddMission)), HarmonyPrefix]
    public static bool PreventVanillaQuestUnlockAndSendCheck(Missions m, ref MetaProgressSaveManager __instance)
    {
        BPHAP.Log("Mission MPSM instance: " + __instance.ToString());
        
        if (missionJustStarted)
        {
            // This function is also run when starting a quest (from RunTypeManager.AssignRunType), so it would erroneously send checks for researching quests at the start of missions unlocked from AP
            missionJustStarted = false;
            return true;
        }
        else
        {
            
            if (m.name == "First Journey" || m.name == "Standard Run" || m.name == "Satchel Standard" || m.name == "Tote Standard" || m.name == "Pochette Standard" || m.name == "CR8 Standard")
            {
                return true;
            }

            BPHAP.Log("Mission " + m.name + " was prevented from being unlocked.");

            string quest = m.name;

            if (m.name == "Tusk") // internal item name overlap
            {
                quest = "Red Tusk";
            }

            BPHAP.APClient.SendCheck(quest);

            return false;
        }
    }


    private const int NPC_LOCATION_OFFSET_VIV = 2100;
    public static bool newCostumeIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.UnlockCostume)), HarmonyPrefix]
    public static bool PreventVanillaCostumeUnlockAndSendCheck(RuntimeAnimatorController __0)
    {
        if (newCostumeIsFromAP)
        {
            newCostumeIsFromAP = false;
            return true;
        }
        else
        {

            BPHAP.Log("Costume " + __0.name + " was prevented from being unlocked.");

            return true;

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

            BPHAP.APClient.SendCheck(__0);

            return false;
        }
    }


    public static bool metaProgressIsFromAP = false;

    [HarmonyPatch(typeof(MetaProgressSaveManager), nameof(MetaProgressSaveManager.AddMetaProgressMarker), new Type[] { typeof(MetaProgressSaveManager.MetaProgressMarker) }), HarmonyPrefix]
    public static bool HandleMetaProgressMarker(MetaProgressSaveManager.MetaProgressMarker m)
    {
        // ItemReceived.UpdateReceivedItemQueues();
        
        BPHAP.Log("AddMetaProgressMarker was run; Marker was added with enum value of " + (int)m);

        if (missionJustStarted)
        {
            missionJustStarted = false;
        }

        switch ((int)m)
        {
            case 6:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Tote unlocked; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Tote");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 7:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("CR-8 unlocked; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("CR-8");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 8:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Satchel unlocked; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Satchel");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 9:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Pochette unlocked; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Pochette");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
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
                    BPHAP.APClient.SendCheck("Key to the Bramble");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 51:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Deep Cave research finished; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Key to the Deep Caves");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 52:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Enchanted Swamp research finished; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Key to the Enchanted Swamp");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 53:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Magma Core research finished; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Key to the Magma Core");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            case 54:
                if (!metaProgressIsFromAP) {
                    BPHAP.Log("Frozen Heart research finished; Blocking progress marker.");
                    BPHAP.APClient.SendCheck("Key to the Frozen Heart");
                    return false;
                } else { 
                    metaProgressIsFromAP = false;
                    return true; 
                }
            // case 100:
            //     if (!metaProgressIsFromAP) {
            //         BPHAP.Log("Forges unlocked; Blocking progress marker.");
            //         // Send check
            //         return false;
            //     } else { return true; }
            case 148:
                BPHAP.Log("You win! Conglaturations!");
                BPHAP.APClient.Goal();
                return true;
            default: 
                return true;
        }
    }

}