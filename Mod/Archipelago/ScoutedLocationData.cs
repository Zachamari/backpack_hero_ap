using System.Collections;
using System;

namespace Backpackipelago.Archipelago;

public class ScoutedLocationData
{
    public string itemName;
    public string locationName;
    public string receivingPlayer;
    public string receivingGame;
    public string itemClass;
    public bool isLocalItem;

    public ScoutedLocationData(string locationName, string itemName, string receivingPlayer, string receivingGame, string itemClass, bool isLocalItem)
    {
        this.locationName = locationName;
        this.itemName = itemName;
        this.receivingPlayer = receivingPlayer;
        this.receivingGame = receivingGame;
        this.itemClass = itemClass;
        this.isLocalItem = isLocalItem;
    }

}