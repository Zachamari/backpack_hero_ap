using HarmonyLib;

namespace Backpackipelago.Patches;

public static class UIManager
{
    
    private static bool connected = false;

    [HarmonyPatch(typeof(MenuManager), nameof(MenuManager.OpenSaveMenuManager)), HarmonyPrefix]
    public static bool PreventOpeningSaveMenuWhenNotConnected()
    {
        if (connected)
        {
            return true;
        }
        else
        {
            // open connection menu
            return false;
        }
    }

}