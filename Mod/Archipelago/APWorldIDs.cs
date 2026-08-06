using System.Collections.Generic;
using System.IO;
using MelonLoader.TinyJSON;
using System.Text;
using Newtonsoft.Json;
using UnityEngine.InputSystem;

namespace Backpackipelago.Archipelago;
public class APWorldIDs
{
    public Dictionary<string, int> ItemNameToID { get; }
    public Dictionary<string, int> LocationNameToID { get; set; }
    public Dictionary<string, string> InternalUnlockToLocationName = new Dictionary<string, string>();
    
    public APWorldIDs()
    {

        using (StreamReader reader = new StreamReader("apworld_item_name_to_id.json"))
        {
            string contents = reader.ReadToEnd();
            ItemNameToID = JsonConvert.DeserializeObject<Dictionary<string, int>>(contents);
        }

        using (StreamReader reader = new StreamReader("apworld_location_name_to_id.json"))
        {
            string contents = reader.ReadToEnd();
            LocationNameToID = JsonConvert.DeserializeObject<Dictionary<string, int>>(contents);
        }

        foreach (string location in LocationNameToID.Keys)
        {
            if (location.Contains("Research - "))
            {
                if (!location.Contains("Quest:")) {
                    InternalUnlockToLocationName.Add(location.Split(["Research - "], System.StringSplitOptions.RemoveEmptyEntries)[1], location);
                    continue;
                } else
                {
                    //
                    continue;
                }
            }
            
            InternalUnlockToLocationName.Add(location.Split('(')[1].Split(')')[0], location);
            
        }

    }

}