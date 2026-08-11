using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using JetBrains.Annotations;
using System.Collections.Generic;

namespace Backpackipelago.Patches;

public static class ItemReceived
{

    public static List<string> itemQueue = [];

    public static void ReceiveNewItem(string itemName)
    {

        BPHAP.Log($"Adding item {itemName} to pool...");
        
        if (itemQueue.Contains(itemName))
        {
            itemQueue.Remove(itemName);
        }

        if (GameInstance.MetaProgressSaveManagerItems == null || GameInstance.DebugItemManagerInstance == null)
        {
            itemQueue.Add(itemName);
            BPHAP.Log($"Skipping adding item {itemName} because instance was not stored yet.");
            return;
        }

        GameInstance.receivedItems.Add(Item2.GetDisplayName(itemName));
        LocationChecked.newItemIsFromAP = true;

        if (!GameInstance.MetaProgressSaveManagerItems.itemsUnlocked.Contains(itemName)) {
            
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

            GameInstance.MetaProgressSaveManagerItems.UnlockItem(item);
            // Overworld_Manager.main.OpenNewItemWindow(Item2.GetItemByName(itemName));
        } else
        {
            BPHAP.Log($"Item {itemName} was not added to the pool since it was already found.");
        } 
    }

    public static List<string> missionQueue = [];
    public static void ReceiveNewMission(string missionName)
    {
        if (missionQueue.Contains(missionName))
        {
            missionQueue.Remove(missionName);
        }

        if (GameInstance.MetaProgressSaveManagerMissions == null)
        {
            missionQueue.Add(missionName);
            return;
        }
        
        BPHAP.Log($"Adding mission {missionName} to list of accessible missions...");
        // LocationChecked.newMissionIsFromAP = true;
        if (!GameInstance.MetaProgressSaveManagerMissions.missionsUnlocked.Contains(missionName)) { 
            GameInstance.MetaProgressSaveManagerMissions.missionsUnlocked.Add(missionName);
            if (GameInstance.RunTypeSelector != null) {
                Overworld_Manager.main.OpenNewMissionWindow(GameInstance.RunTypeSelector.GetMissionFromName(missionName));
            }
        } else
        {
            BPHAP.Log($"Mission {missionName} wasn't unlocked since it was already unlocked.");            
        }
    }

    public static List<string> buildingQueue = [];
    public static void ReceiveNewBuilding(string buildingName)
    {
        // This function is only ever called through the building queue
        if (GameInstance.BuildingInstance == null)
        {
            return;
        }
        buildingQueue.Remove(buildingName);
        BPHAP.Log($"Adding building {buildingName} to list of buildable buildings...");
        LocationChecked.newBuildingIsFromAP = true;
        GameInstance.BuildingInstance.AddBuilding(buildingName);
        // Overworld_Manager.main.OpenNewConstructionWindow(Overworld_Structure.StructuresOfType(buildingName)[0]);
    }


    public static List<string> tileQueue = [];
    public static void ReceiveNewPath(string tileName)
    {
        // also only called thru tileQueue
        if (GameInstance.BuildingInstance == null)
        {
            return;
        }
        tileQueue.Remove(tileName);
        BPHAP.Log($"Adding path {tileName} to list of buildable paths...");
        LocationChecked.newBuildingIsFromAP = true;
        GameInstance.BuildingInstance.AddTile(tileName);
        // Not sure if I can find SellingTile objects from string names, so I might need to implement tile popups separately (or not at all bc who cares lol)
        // if (GameInstance.RunTypeSelector != null) {
        //     Overworld_Manager.main.OpenNewConstructionWindow());
        // }
    }

    public static List<int> metaQueue = [];
    public static void ReceiveNewMetaProgress(int enumVal)
    {
        if (GameInstance.MetaProgressSaveManagerMissions == null)
        {
            metaQueue.Add(enumVal);
            return;
        }

        BPHAP.Log($"Adding item {enumVal} to metaprogression...");
        LocationChecked.metaProgressIsFromAP = true;
        GameInstance.MetaProgressSaveManagerMissions.AddMetaProgressMarker((MetaProgressSaveManager.MetaProgressMarker)enumVal);
        // Figure out how to make a custom popup later
    }

    public static List<string> costumeQueue = [];
    public static void ReceiveNewCostume(string costumeName)
    {
        if (GameInstance.MetaProgressSaveManagerMissions == null)
        {
            costumeQueue.Add(costumeName);
            return;
        }

        BPHAP.Log($"Adding costume {costumeName} to available costumes...");
        LocationChecked.newCostumeIsFromAP = true;
        GameInstance.MetaProgressSaveManagerMissions.availableCostumes.Add(costumeName);
        // Overworld_Manager.main.OpenNewCostumeWindow(costumeName); // Function requires a RuntimeAnimatorController, not sure if I'm able to get that type of object easily
    }


    public static void UpdateReceivedItemQueues()
    {
        
        if (missionQueue.Count > 0)
        {
            foreach (string mission in missionQueue)
            {
                ReceiveNewMission(mission);
            }
            missionQueue.Clear();
        }

        if (itemQueue.Count > 0)
        {
            foreach (string itemName in itemQueue)
            {
                ReceiveNewItem(itemName);
            }
        }
    
        if (metaQueue.Count > 0)
        {
            foreach (int val in metaQueue)
            {
                ReceiveNewMetaProgress(val);
            }
            metaQueue.Clear();
        }        
        
        if (costumeQueue.Count > 0)
        {
            foreach (string costume in costumeQueue)
            {
                ReceiveNewCostume(costume);
            }
            costumeQueue.Clear();
        }

    }

}