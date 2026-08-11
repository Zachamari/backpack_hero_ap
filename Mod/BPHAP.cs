using System;
using System.Collections;
using MelonLoader;
using HarmonyLib;
using Backpackipelago;
using Backpackipelago.Archipelago;
using Backpackipelago.Patches;


[assembly: MelonInfo(typeof(BPHAP), "Backpackipelago", BPHAP.Version, "Zachamari")]
[assembly: MelonGame("TheJaspel", "Backpack Hero")]

namespace Backpackipelago
{
    public class BPHAP : MelonMod
    {
        public const string Version = "0.0.0"; 

        public static ArchipelagoClient APClient;

        public static APWorldIDs APIDs = new APWorldIDs();

        public override void OnInitializeMelon()
        {

            // Mod startup logic goes here

            APClient = new ArchipelagoClient();
            ArchipelagoClient.ServerData.Uri = "localhost:38281";
            ArchipelagoClient.ServerData.SlotName = "Player1";
            ArchipelagoClient.ServerData.Password = "";
            // APClient.Connect();

            HarmonyLib.Harmony.CreateAndPatchAll(typeof(LocationChecked));
            HarmonyLib.Harmony.CreateAndPatchAll(typeof(GameInstance));

            Log($"Backpackipelago v{Version} successfully loaded!");

            base.OnInitializeMelon();
        }


        public static void LogError(string message) {
            MelonLogger.Error(message);
        }
        public static void Log(string message) {
            MelonLogger.Msg(message);
        }
        public static void LogWarning(string message) {
            MelonLogger.Warning(message);
        }
    }
}
