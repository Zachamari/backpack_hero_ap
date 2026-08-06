using System.Collections.Generic;
using System.Collections;
using Newtonsoft.Json;

namespace Backpackipelago.Archipelago;

public class ArchipelagoData
{
    public string Uri = "localhost:38281";
    public string SlotName = "Player1";
    public string Password = "";
    public int Index = 0;

    public List<long> CheckedLocations;

    /// <summary>
    /// seed for this archipelago data. Can be used when loading a file to verify the session the player is trying to
    /// load is valid to the room it's connecting to.
    /// </summary>
    private string seed = "0";

    private Dictionary<string, object> slotData = new Dictionary<string, object>();

    public bool NeedSlotData => slotData == null;

    public ArchipelagoData()
    {
        Uri = "localhost:38281";
        SlotName = "Player1";
        CheckedLocations = new List<long>();
    }

    public ArchipelagoData(string uri, int port, string slotName, string password)
    {
        Uri = uri;
        SlotName = slotName;
        Password = password;
        CheckedLocations = new List<long>();
    }

    /// <summary>
    /// assigns the slot data and seed to our data handler. any necessary setup using this data can be done here.
    /// </summary>
    /// <param name="roomSlotData">slot data of your slot from the room</param>
    /// <param name="roomSeed">seed name of this session</param>
    public void SetupSession(Dictionary<string, object> roomSlotData, string roomSeed)
    {
        slotData = roomSlotData;
        seed = roomSeed;
    }

    /// <summary>
    /// returns the object as a json string to be written to a file which you can then load
    /// </summary>
    /// <returns></returns>
    public override string ToString()
    {
        return JsonConvert.SerializeObject(this);
    }
}