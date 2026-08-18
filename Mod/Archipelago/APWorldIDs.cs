using System.Collections.Generic;
using System.IO;
using MelonLoader.TinyJSON;
using System.Text;
using Newtonsoft.Json;
using UnityEngine.InputSystem;
using System.Runtime.InteropServices;
using System.Linq;

namespace Backpackipelago.Archipelago;
public class APWorldIDs
{
    public Dictionary<string, int> ItemNameToID { get; }
    public Dictionary<string, int> InternalUnlockToLocationID { get; }
    
    public APWorldIDs()
    {
        BPHAP.Log("Reading JSON Data...");
        using (StreamReader reader = new StreamReader("UserData/bph_item_table.json"))
        {  
            BPHAP.Log("Reading item data...");
            string contents = reader.ReadToEnd();
            this.ItemNameToID = JsonConvert.DeserializeObject<Dictionary<string, int>>(contents);
        }

        Dictionary<string, int> LocationNameToID;

        using (StreamReader reader = new StreamReader("UserData/bph_location_table.json"))
        {
            BPHAP.Log("Reading location data...");
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

            BPHAP.Log($"Adding location {specificLocation} (full location name: {location})");

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
                    if (item == "Ice Cream")
                    {
                        // The string "Ice Cream" is present in 3 locations (1 item unlock, 2 quest unlocks), so we need to account for that
                        if (!specificLocation.Contains("Purse") && !specificLocation.Contains("Satchel"))
                        {
                            temp.Add("Ice Cream", LocationNameToID[location]);
                            break;
                        } 
                        else { continue; }
                    }
                    if (item == "Tusk")
                    {
                        // "Tusk" is also present in both Quest: Red Tusk and Tusk. 
                        // Additionally, the internal name for Quest: Red Tusk is "Tusk", which is the same as the item name, so there's double overlap here.
                        if (location.Contains("Red Tusk"))
                        {
                            temp.Add("Red Tusk", LocationNameToID[location]);
                            break;  
                        } else
                        {
                            temp.Add("Tusk", LocationNameToID[location]);
                            break;
                        }
                    }
                    if (item == "Farm")
                    {
                        if (specificLocation.Contains("Farmland"))
                        {
                            temp.Add("Farmland", LocationNameToID[location]);
                            break;
                        }
                    }
                    if (item == "House")
                    {
                        if (specificLocation.Contains("Purse's House"))
                        {
                            temp.Add("Purse's House", LocationNameToID[location]);
                            break;
                        }
                    }
                    if (item == "Satchel" || item == "Tote" || item == "Pochette")
                    {
                        if (!specificLocation.Contains("Recruit"))
                        {
                            continue;
                        }
                    }
                    if (item == "Purse")
                    {
                        continue; // There is no vanilla Purse unlock location
                        // (The only reason she's in the item list in the first place is bc i think it's cool to have it show her as a starting item on the website tracker)
                    }
                    if (item == "CR-8")
                    {
                        if (specificLocation != "CR-8")
                        {
                            continue;
                            // CR-8 is a research location, so it has to be separate from the other 3 unlockable characters b/c no "Recruit" in name
                        }
                    }
                    if (item.Contains("Quest:"))
                    {

                        string missionName = GetInternalMissionName(item.Split([": "], System.StringSplitOptions.None)[1]);

                        temp.Add(missionName, LocationNameToID[location]);
                        break;
    
                    }
                    if (item.Contains("Hyacinth") || item.Contains("Item Pedestal") || item.Contains("Beehives"))
                    {
                        // literally only the hyacinths and item pedestal have capitalization mismatches between AP and internal. All the other buildings are fine
                        temp.Add(GetInternalBuildingName(item), LocationNameToID[location]); 
                        break;
                    }
                    temp.Add(GetInternalItemName(item), LocationNameToID[location]); 
                    break;
                }
            }

            if (temp.Values.Contains(LocationNameToID[location]))
            {
                // nested foreach statements suck, there's probably a better way to do this
                continue;
            }

            // The progressive quest items are formatted differently, so they're not caught by the above foreach loop and need to be added independently
            // I could probably automate this, but there's so few of them that it's not a big difference to just do it manually
            if (location.Contains("Quest: Coral 1"))
            {
                temp.Add("Coral 1", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Coral 2"))
            {
                temp.Add("Coral 2", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Windmill 1"))
            {
                temp.Add("windmill 1", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Windmill 2"))
            {
                temp.Add("windmill 2", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Hourglass 1"))
            {
                temp.Add("Hourglass 1", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Hourglass 2"))
            {
                temp.Add("Hourglass 2", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Scissors 1"))
            {
                temp.Add("Scissors", LocationNameToID[location]);
                continue;
            }
            if (location.Contains("Quest: Scissors 2"))
            {
                temp.Add("Scissors 2", LocationNameToID[location]); // Might be wrong
                continue;
            }
            if (location.Contains("Quest: Hourglass 1"))
            {
                temp.Add("Hourglass 1", LocationNameToID[location]);
                continue;
            }
            BPHAP.LogWarning($"WARNING: Location {location} was unable to be added to the dictionary.");
        }


        this.InternalUnlockToLocationID = temp; // Dictionary should contain items in the form of, ex. {"Dagger": ID} with no other extraneous information


        BPHAP.Log($"Total number of items in dict: {ItemNameToID.Count}");
        foreach(KeyValuePair<string, int> item in ItemNameToID)
        {
            BPHAP.Log($"Logged Item Name: {item.Key} - ID: {item.Value}");
        }
        BPHAP.Log($"Total number of locations in dict: {InternalUnlockToLocationID.Count}");
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
            "Duo Core" => "CR8 Double Core",
            "Scissors 1" => "Scissors",
            "This One's On Me" => "This Round is On Me",
            "Builder Bird" => "Builder Bird Mission",
            "Magic Archery" => "Magic Archery 1",
            "Windmill 1" => "windmill 1",
            "Wizard's School" => "Wizard School",
            "Master of Whetstones" => "Whetstone",
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
            "Boo-Hoo Buckler" => "Boo-hoo Buckler ", // yes the extra space is required
            "Berserker's Club" => "berserker's club",
            "Assassin's Dagger" => "assassin's dagger",
            "Lucky Shiv" => "LUCKY Shiv",
            "Charging Manastone" => "Charging ManaStone",
            "Golden Star" => "Golden Shuriken",
            "Alpha Star" => "Alpha Shuriken",
            "Unstable Manastone" => "Unstable Mana",
            "Bowblade" => "BowBlade",
            "Rare Herb" => "Rare herb",
            "Energy Wand" => "Ethereal Wand",
            
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
            "Item Pedestal" => "item pedestal",
            "Beehives" => "BeeHives",
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