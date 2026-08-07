using Backpackipelago;
using MelonLoader;
using HarmonyLib;
using JetBrains.Annotations;

namespace Backpackipelago.Patches;

public static class ItemReceived
{
    public static void ReceiveNewItem(string itemName)
    {
        BPHAP.Log($"Adding item {itemName} to pool...");
        LocationChecked.newItemIsFromAP = true;
        GameInstance.MetaProgressSaveManager.UnlockItem(Item2.GetItemByName(itemName));
        Overworld_Manager.main.OpenNewItemWindow(Item2.GetItemByName(itemName));
    }

    public static void ReceiveNewMission(string missionName)
    {
        BPHAP.Log($"Adding mission {missionName} to list of accessible missions...");
        LocationChecked.newMissionIsFromAP = true;
        GameInstance.MetaProgressSaveManager.missionsUnlocked.Add(missionName);
        if (GameInstance.RunTypeSelector != null) {
            Overworld_Manager.main.OpenNewMissionWindow(GameInstance.RunTypeSelector.GetMissionFromName(missionName));
        }
        // The earliest I can get the RunTypeSelector instance is when opening the mission select menu unfortunately, so any missions received offline won't have a popup for now since I can't find the Missions object corresponding to the missionName without that instance
    }

    public static void ReceiveNewBuilding(string buildingName)
    {
        BPHAP.Log($"Adding building {buildingName} to list of buildable buildings...");
        LocationChecked.newBuildingIsFromAP = true;
        Overworld_BuildingManager.main.AddBuilding(buildingName);
        Overworld_Manager.main.OpenNewConstructionWindow(Overworld_Structure.StructuresOfType(buildingName)[0]);
    }

    public static void ReceiveNewPath(string tileName)
    {
        BPHAP.Log($"Adding path {tileName} to list of buildable paths...");
        LocationChecked.newBuildingIsFromAP = true;
        Overworld_BuildingManager.main.AddTile(tileName);
        // Not sure if I can find SellingTile objects from string names, so I might need to implement tile popups separately (or not at all bc who cares lol)
        // if (GameInstance.RunTypeSelector != null) {
        //     Overworld_Manager.main.OpenNewConstructionWindow());
        // }
    }

    public static void ReceiveNewMetaProgress(int enumVal)
    {
        BPHAP.Log($"Adding item {enumVal} to metaprogression...");
        LocationChecked.metaProgressIsFromAP = true;
        MetaProgressSaveManager.main.AddMetaProgressMarker((MetaProgressSaveManager.MetaProgressMarker)enumVal);
        // Figure out how to make a custom popup later
    }

    public static void ReceiveNewCostume(string costumeName)
    {
        BPHAP.Log($"Adding costume {costumeName} to available costumes...");
        LocationChecked.newCostumeIsFromAP = true;
        GameInstance.MetaProgressSaveManager.availableCostumes.Add(costumeName);
        // Overworld_Manager.main.OpenNewCostumeWindow(costumeName); // Function requires a RuntimeAnimatorController, not sure if I'm able to get that type of object easily
    }

}