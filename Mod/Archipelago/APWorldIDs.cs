using System.Collections.Generic;
using System.IO;
using MelonLoader.TinyJSON;
using System.Text;
using Newtonsoft.Json;
using UnityEngine.InputSystem;
using System.Runtime.InteropServices;

namespace Backpackipelago.Archipelago;
public class APWorldIDs
{
    public Dictionary<string, int> ItemNameToID { get; }
    public Dictionary<string, int> InternalUnlockToLocationID { get; }
    
    public APWorldIDs()
    {

        using (StreamReader reader = new StreamReader("apworld_item_name_to_id.json"))
        {
            string contents = reader.ReadToEnd();
            this.ItemNameToID = JsonConvert.DeserializeObject<Dictionary<string, int>>(contents);
        }

        Dictionary<string, int> LocationNameToID;

        using (StreamReader reader = new StreamReader("apworld_location_name_to_id.json"))
        {
            string contents = reader.ReadToEnd();
            LocationNameToID = JsonConvert.DeserializeObject<Dictionary<string, int>>(contents);
        }

        Dictionary<string, int> temp = new Dictionary<string, int>();

        foreach (string location in LocationNameToID.Keys)
        {
            // I need to split the location string into two parts by the dash in the middle and only use the second part, 
            // because otherwise I'd need to figure out a way to prevent all instances of "Barracks Research", "Purse Quest Reward", etc
            // from triggering on the major progression unlocks in the foreach loop below 
            string specificLocation = location.Split([" - "], System.StringSplitOptions.None)[1];

            foreach (string item in ItemNameToID.Keys)
            {
                if (specificLocation.Contains(item))
                {
                    if (item == "Charging Manastone")
                    {
                        // For some reason, Charging Manastone has 2 vanilla unlock locations: one from a quest, and one from research. So, I need to differentiate them here.
                        if (location.Contains("Research"))
                        {
                            temp.Add("Charging Manastone (Research)", LocationNameToID[location]);
        
                        }
                        else
                        {
                            temp.Add("Charging Manastone (Quest)", LocationNameToID[location]);
        
                        }
                        break;
                    }
                    if (item.Contains("Quest:"))
                    {

                        string missionName = GetInternalMissionName(item.Split([": "], System.StringSplitOptions.None)[1]);

                        temp.Add(missionName, LocationNameToID[location]);
                        break;
    
                    }
                    if (item.Contains("Hyacinth"))
                    {
                        // literally only the hyacinths have capitalization mismatches between AP and internal. All the other buildings are fine
                        temp.Add(GetInternalBuildingName(item), LocationNameToID[location]); 
                        break;
                    }
                    temp.Add(GetInternalItemName(item), LocationNameToID[location]); 
                    break;
                }
            }
        }


        this.InternalUnlockToLocationID = temp; // Dictionary should contain items in the form of, ex. {"Dagger": ID} with no other extraneous information


        BPHAP.Log("");
        foreach(KeyValuePair<string, int> item in ItemNameToID)
        {
            BPHAP.Log($"Logged Item Name: {item.Key} - ID: {item.Value}");
        }
        BPHAP.Log("");
        foreach(KeyValuePair<string, int> location in InternalUnlockToLocationID)
        {
            BPHAP.Log($"Logged Internal Location Name: {location.Key} - ID: {location.Value}");
        }

    }

    public static string GetInternalMissionName(string mission)
    {
        // The internal naming of quests is very inconsistent, so I need to check if the mission location is one of the weird ones before I send the check.
        // AP item name => Internal mission name
        return mission switch
        {
            "Easy Mode (Satchel)" => "Easy Satchel",
            "Easy Mode (Pochette)" => "Easy Pochette",
            "Easy Mode (Tote)" => "Easy Tote",
            "Easy Mode (CR-8)" => "Easy CR8",
            "Ice Cream (Satchel)" => "Satchel Ice Cream",
            "Ice Cream (Purse)" => "Scaling Energy",
            "Red Tusk" => "Tusk",
            "Double Core" => "CR8 Double Core",
            "Scissors 1" => "Scissors",
            "This One's On Me" => "This Round Is On Me",
            "Builder Bird" => "Builder Bird Mission",
            "Magic Archery" => "Magic Archery 1",
            _ => mission,
        };
    }

    public static string GetInternalItemName(string item)
    {
        // Dungeon items are very inconsistent with capitalization, so that needs to be corrected as well
        // AP item name => Internal item name
        return item switch
        {
            "Poultice" => "poultice",
            "Amethyst Buckler" => "Amethyste Buckler", // roulxs kaard worked on this game, contributed this one internal item name, and left
            "Boo-Hoo Buckler" => "Boo-hoo Buckler",
            "Berserker's Club" => "berserker's club",
            "Assassin's Dagger" => "assassin's dagger",
            "Lucky Shiv" => "LUCKY Shiv",
            "Charging Manastone" => "Charging ManaStone",
            
            _ => item,
        };
    }

    public static string GetInternalBuildingName(string building)
    {
        // AP item name => Internal building name
        return building switch
        {
            "Yellow Hyacinth" => "Yellow hyacinth",
            "Purple Hyacinth" => "Purple hyacinth",
            "Blue Hyacinth" => "Blue hyacinth",
            _ => building,
        };
    }

    public static string GetInternalCostumeName(string costume)
    {
        return costume switch
        {
            "Blue Costume (Purse)" => "Purse Alternate Controller",
            "Rogue Costume (Purse)" => "Purse Rogue",
            "Feral Costume (Purse)" => "Purse Feral",
            "Elder Costume (Purse)" => "Purse Elder",

            _ => "COSTUME UNKNOWN", // None of my costume names match the internal names, so if it gets here, that means there's a problem
        };
    }
}