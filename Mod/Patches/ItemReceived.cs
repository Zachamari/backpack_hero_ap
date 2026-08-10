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
        if (GameInstance.MetaProgressSaveManagerItems == null)
        {
            itemQueue.Add(itemName);
            return;
        }
        BPHAP.Log($"Adding item {itemName} to pool...");
        LocationChecked.newItemIsFromAP = true;
        if (!GameInstance.MetaProgressSaveManagerItems.itemsUnlocked.Contains(itemName)) {
            GameInstance.MetaProgressSaveManagerItems.itemsUnlocked.Add(itemName);
            // Overworld_Manager.main.OpenNewItemWindow(Item2.GetItemByName(itemName));
        } else
        {
            BPHAP.Log($"Item {itemName} was not added to the pool since it was already found.");
        } 
    }

    public static List<string> missionQueue = [];
    public static void ReceiveNewMission(string missionName)
    {
        if (GameInstance.MetaProgressSaveManagerMissions == null)
        {
            missionQueue.Add(missionName);
            return;
        }
        
        BPHAP.Log($"Adding mission {missionName} to list of accessible missions...");
        LocationChecked.newMissionIsFromAP = true;
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
        if (GameInstance.BuildingInstance == null)
        {
            buildingQueue.Add(buildingName);
            return;
        }
        buildingQueue.Clear();
        BPHAP.Log($"Adding building {buildingName} to list of buildable buildings...");
        LocationChecked.newBuildingIsFromAP = true;
        GameInstance.BuildingInstance.AddBuilding(buildingName);
        // Overworld_Manager.main.OpenNewConstructionWindow(Overworld_Structure.StructuresOfType(buildingName)[0]);
    }


    public static List<string> tileQueue = [];
    public static void ReceiveNewPath(string tileName)
    {
        if (GameInstance.BuildingInstance == null)
        {
            tileQueue.Add(tileName);
            return;
        }
        
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

}