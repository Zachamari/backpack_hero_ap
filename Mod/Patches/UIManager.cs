using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics.Tracing;
using System.Runtime.CompilerServices;
using Backpackipelago.Archipelago;
using HarmonyLib;
using TMPro;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.EnhancedTouch;
using UnityEngine.UI;
using UnityEngine.UIElements;

namespace Backpackipelago.Patches;

public static class UIManager
{
    
    // NOTE: Connection UI is NOT functional yet, currently it just displays an empty white box upon clicking the button to open the menu
    // This means it's also impossible to connect to the server because of this file, remove this file entirely before compiling if you want to playtest
    // You'll also have to manually put the connection info into BPHAP.OnInitializeMelon() before compiling

    private static bool connected => ArchipelagoClient.Authenticated;
    public static bool showMenu = false;
    public static MenuManager MenuManager;

    [HarmonyPatch(typeof(MenuManager), nameof(MenuManager.ShowButtons)), HarmonyPrefix]
    public static void PreventOpeningSaveMenuWhenNotConnected()
    {
        BPHAP.Log("Opening main menu.");

        // idk if opening a quick run will mess anything up, so i'm disabling the buttons for them just in case
        GameObject startQuickButton = GameObject.Find("Menu Animation/Canvas/Buttons/Start Game Button");
        startQuickButton.SetActive(false);
        
        // I decided to override the Continue Quick Game button for opening the Archipelago menu
        GameObject contQuickButton = GameObject.Find("Menu Animation/Canvas/Buttons/Continue Save Game Button");


        // override the continue button's display text   
        GameObject contQuickButtonText = GameObject.Find("Menu Animation/Canvas/Buttons/Continue Save Game Button/Start Game Button Image/Continue Text");
        TextMeshProUGUI contButtonText = contQuickButtonText.GetComponent<TMPro.TextMeshProUGUI>();
        contButtonText.text = "Archipelago";


        if (!connected) {

            BPHAP.Log("Hiding the story mode button...");
            GameObject storyModeButton = GameObject.Find("Menu Animation/Canvas/Buttons/Story Mode");
            storyModeButton.SetActive(false);

        } else
        {
            
            BPHAP.Log("Bringing the story mode button back...");
            GameObject storyModeButton = GameObject.Find("Menu Animation/Canvas/Buttons/Story Mode");
            storyModeButton.SetActive(true);
        }

    }

    // everything commented out below this is my failed attempt at making an entirely custom UI

    // This function opens the "Continue Quick Game" menu in vanilla
    [HarmonyPatch(typeof(MenuManager), nameof(MenuManager.OpenSaveMenuManager)), HarmonyPrefix]
    public static bool OpenArchipelagoMenu(ref MenuManager __instance)
    {
        // open menu here

        // __instance.HideButtons();
        // SoundManager.main.PlaySFX("menuBlip");
        // menu.transform.localPosition = Vector3.zero;
        // menu.transform.localScale = Vector3.one;

        // GameObject child = UnityEngine.Object.Instantiate<GameObject>(animator, menu.transform);
        // Image menuBorder = child.GetComponent<Image>();
        // // current problem - it just displays a white box upon clicking the button

        layout.fontSize = 500;
        layout.wordWrap = true;
        layout.clipping = TextClipping.Overflow;

        showMenu = true;

        // TODO: Close the main menu, make closing the AP menu reopen the main menu and turn showMenu to false
        GameObject.Find("Menu Animation/Canvas/Buttons").SetActive(false); // this ain't smooth, but it works (the normal closing animation doesn't work when I trigger it for some reason)
        GameObject.Find("Menu Animation/Canvas/Title").SetActive(false);
        MenuManager = __instance;



        return false;
    }

    private static GUIStyle layout = new GUIStyle();


    public static void OnGUI()
    {
                // This part is all copied from OnGUI() in alwaysintreble's bepinex template because i gave up on ui (for now)
        
        // show the mod is currently loaded in the corner

        GUI.backgroundColor = new Color(44, 30, 16, 1); // color of the background in vanilla menus
        GUI.contentColor = Color.white;

        GUI.Box(new Rect(Screen.width/4, Screen.height/4, Screen.width/2, (Screen.height/2) - 60), "ARCHIPELAGO OPTIONS");
        GUILayout.BeginArea(new Rect(Screen.width/4, Screen.height/4, Screen.width/2, (Screen.height/2) - 60), layout);

        GUILayout.Label($"Backpackipelago v{BPHAP.Version}");
        
        
        // ArchipelagoConsole.DisplayGUI();


        string statusMessage;

        GUILayout.Space(20);


        if (!ArchipelagoClient.Authenticated) {
            
            statusMessage = "Status: Disconnected";

            GUILayout.BeginHorizontal();
            GUILayout.Label("Host: ");
            ArchipelagoClient.ServerData.Uri = GUILayout.TextField(ArchipelagoClient.ServerData.Uri);
            GUILayout.EndHorizontal();

            GUILayout.BeginHorizontal();
            GUILayout.Label("Player Name: ");
            ArchipelagoClient.ServerData.SlotName = GUILayout.TextField(ArchipelagoClient.ServerData.SlotName);  
            GUILayout.EndHorizontal();

            GUILayout.BeginHorizontal();  
            GUILayout.Label("Password: ");
            ArchipelagoClient.ServerData.Password = GUILayout.TextField(ArchipelagoClient.ServerData.Password);
            GUILayout.EndHorizontal();

        } else
        {
            statusMessage = "Status: Connected";

            GUILayout.BeginHorizontal();
            GUILayout.Label("Host: ");
            GUILayout.FlexibleSpace();
            GUILayout.Label(ArchipelagoClient.ServerData.Uri);
            GUILayout.EndHorizontal();

            GUILayout.BeginHorizontal();
            GUILayout.Label("Player Name: ");
            GUILayout.FlexibleSpace();
            GUILayout.Label(ArchipelagoClient.ServerData.SlotName); 
            GUILayout.EndHorizontal();

            GUILayout.BeginHorizontal();  
            GUILayout.Label("Password: ");
            GUILayout.FlexibleSpace();
            GUILayout.Label(ArchipelagoClient.ServerData.Password);
            GUILayout.EndHorizontal();

        }

        GUILayout.Label(statusMessage);

        GUILayout.Space(40);



        // Settings buttons

        scoutHints = GUILayout.Toggle(scoutHints, new GUIContent("Scout Research Locations [?]", "Sends a server-side hint for each research location you haven't found when closing a building's research menu."));
        freeInventoryItemCopy = GUILayout.Toggle(freeInventoryItemCopy, new GUIContent("Bonus Inventory Items [?]", "Adds a free copy of every item you receive from AP to your inventory in Haversack Hill."));

        GUILayout.BeginHorizontal();

        GUILayout.Label(new GUIContent("Resource Gain Multiplier (percentage, default 100%): [?]", "Multiplies all resources gained (such as by selling items or traversing in the dungeon) by the given percentage."));
        MultiplierPercentPositive = GUILayout.TextField(MultiplierPercentPositive);
        MultiplierPercentPositive = GUILayout.HorizontalSlider(InventoryManagement.MultiplierPercentPositive, 50, 1000).ToString();

        GUILayout.EndHorizontal();

        GUILayout.BeginHorizontal();

        GUILayout.Label(new GUIContent("Resource Loss Multiplier (percentage, default 100%): [?]", "Multiplies all resources lost (such as by constructing buildings or buying research) by the given percentage."));
        MultiplierPercentNegative = GUILayout.TextField(MultiplierPercentNegative);
        MultiplierPercentNegative = GUILayout.HorizontalSlider(InventoryManagement.MultiplierPercentNegative, 0, 200).ToString();

        GUILayout.EndHorizontal();

        GUILayout.FlexibleSpace();

        GUILayout.Label(GUI.tooltip); // unfortunately the tooltip has to be down here or else it gets called before it gets set (and thus doesn't display at all)

        GUILayout.BeginHorizontal();


        if (GUILayout.Button("Close Menu"))
        {

            UIManager.showMenu = false;
            GameObject.Find("Menu Animation/Canvas/Buttons").SetActive(true);
            GameObject.Find("Menu Animation/Canvas/Title").SetActive(true);


            // override the continue button's display text again  
            GameObject contQuickButtonText = GameObject.Find("Menu Animation/Canvas/Buttons/Continue Save Game Button/Start Game Button Image/Continue Text");
            TextMeshProUGUI contButtonText = contQuickButtonText.GetComponent<TMPro.TextMeshProUGUI>();
            contButtonText.text = "Archipelago";

            if (!connected) {

                BPHAP.Log("Hiding the story mode button...");
                GameObject storyModeButton = GameObject.Find("Menu Animation/Canvas/Buttons/Story Mode");
                storyModeButton.SetActive(false);

            } else
            {
                
                BPHAP.Log("Bringing the story mode button back...");
                GameObject storyModeButton = GameObject.Find("Menu Animation/Canvas/Buttons/Story Mode");
                storyModeButton.SetActive(true);
            }

        }


        if (!ArchipelagoClient.Authenticated)
        {
            // requires that the player at least puts *something* in the slot name
            if (GUILayout.Button("Connect to Server") && !string.IsNullOrWhiteSpace(ArchipelagoClient.ServerData.SlotName))
            {
                BPHAP.APClient.Connect();
            }
        } else
        {
            if (GUILayout.Button("Disconnect from Server"))
            {
                BPHAP.APClient.Disconnect();
            }
        }


        GUILayout.EndHorizontal();

        GUILayout.EndArea();

    }



    public static bool scoutHints = true;
    public static bool freeInventoryItemCopy = true;
    public static string MultiplierPercentPositive
    {
        get
        {
            return InventoryManagement.MultiplierPercentPositive.ToString();
        }
        set
        {
            try
            {
                float num = float.Parse(value);
                if (num > 1000)
                {
                    InventoryManagement.MultiplierPercentPositive = 1000;
                    return;
                }
                if (num < 50)
                {
                    InventoryManagement.MultiplierPercentPositive = 50;
                    return;
                }
                InventoryManagement.MultiplierPercentPositive = num;
            } catch { }
        }
    }
    public static string MultiplierPercentNegative
    {
        get
        {
            return InventoryManagement.MultiplierPercentNegative.ToString();
        }
        set
        {
            try
            {
                float num = float.Parse(value);
                if (num > 200)
                {
                    InventoryManagement.MultiplierPercentNegative = 200;
                    return;
                }
                if (num < 0)
                {
                    InventoryManagement.MultiplierPercentNegative = 0;
                    return;
                }
                InventoryManagement.MultiplierPercentNegative = num;
            } catch { }
        }
    }


    // private static GameObject APMenu = new GameObject(
    //     "Archipelago Menu", 
    //     [
    //         typeof(RectTransform), 
    //         typeof(CanvasRenderer), 
    //         // typeof(APOptions), 
    //         typeof(SingleUI), 
    //         typeof(DigitalCursorInterface), 
    //         typeof(CanvasGroup)
    //     ]
    // );

    // private static GameObject animator = new GameObject(
    //     "Animation",
    //     [
    //         typeof(RectTransform),
    //         typeof(CanvasGroup),
    //         typeof(Animator),
    //         typeof(AnimationEvent),
    //         typeof(CanvasRenderer),
    //         typeof(UnityEngine.UI.Image),
    //     ]
    // );


}

// public class APOptions : MonoBehaviour
// {
//     private void Start()
//     {
//         this.mask.enabled = true;
//         // EventSystem.current.SetSelectedGameObject(this.slotName.gameObject);

//         // set all options to their defaults or stored values

//         slotName.characterLimit = 16;
//         slotName.lineType = TMP_InputField.LineType.SingleLine;
//         slotName.text = "Player1";
//         // slotName.onSubmit.AddListener(slotName_OnSubmit);
//         slotName.ActivateInputField();

//         server.lineType = TMP_InputField.LineType.SingleLine;
//         server.text = "archipelago.gg:38281";
//         server.ActivateInputField();

//         password.lineType = TMP_InputField.LineType.SingleLine;
//         password.inputType = TMP_InputField.InputType.Password;
//         password.text = "";
//         password.ActivateInputField();


//     }

//     void slotName_OnSubmit()
//     {
//         BPHAP.Log("Slot Name submitted!");
//     }

//     void scouts_OnValueChanged()
//     {
//         BPHAP.Log("Scout hints toggled!");
//     }

//     private UnityAction<string> slotNameListener;

//     private TMPro.TMP_InputField slotName;
//     private TMP_InputField server;
//     private TMP_InputField password;
//     private UnityEngine.GameObject connectButton;
//     private UnityEngine.UI.Toggle scoutHints;
//     private UnityEngine.UI.Slider resourceGainMult;
//     private UnityEngine.UI.Slider resourceLossMult;
//     private UnityEngine.UI.Toggle bonusFreeItems;
//     private Mask mask;
// }


// shamelessly stolen (and modified) from alwaysInteble's default bepinex Unity AP template

// shamelessly stolen from oc2-modding https://github.com/toasterparty/oc2-modding/blob/main/OC2Modding/GameLog.cs
public static class ArchipelagoConsole
{
    public static bool Hidden = true;

    private static List<string> logLines = new();
    private static Vector2 scrollView;
    private static Rect window;
    private static Rect scroll;
    private static Rect text;
    private static Rect hideShowButton;

    private static GUIStyle textStyle = new();
    private static string scrollText = "";
    private static float lastUpdateTime = Time.time;
    private const int MaxLogLines = 80;
    private const float HideTimeout = 15f;

    private static string CommandText = "!help";
    private static Rect CommandTextRect;
    private static Rect SendCommandButton;

    public static void Awake()
    {
        UpdateWindow();
    }

    public static void LogMessage(string message)
    {
        if (string.IsNullOrWhiteSpace(message)) return;

        if (logLines.Count == MaxLogLines)
        {
            logLines.RemoveAt(0);
        }
        logLines.Add(message);
        BPHAP.Log(message);
        lastUpdateTime = Time.time;
        UpdateWindow();
    }

    public static void DisplayGUI()
    {
        if (logLines.Count == 0) return;

        if (!Hidden || Time.time - lastUpdateTime < HideTimeout)
        {
            scrollView = GUI.BeginScrollView(window, scrollView, scroll);
            GUI.Box(text, "");
            GUI.Box(text, scrollText, textStyle);
            GUI.EndScrollView();
        }

        if (GUI.Button(hideShowButton, Hidden ? "Show" : "Hide"))
        {
            Hidden = !Hidden;
            UpdateWindow();
        }
        
        // draw client/server commands entry
        if (Hidden || !ArchipelagoClient.Authenticated) return;

        CommandText = GUI.TextField(CommandTextRect, CommandText);
        if (!string.IsNullOrWhiteSpace(CommandText) && GUI.Button(SendCommandButton, "Send"))
        {
            BPHAP.APClient.SendMessage(CommandText);
            CommandText = "";
        }
    }

    public static void UpdateWindow()
    {
        scrollText = "";

        if (Hidden)
        {
            if (logLines.Count > 0)
            {
                scrollText = logLines[logLines.Count - 1];
            }
        }
        else
        {
            for (var i = 0; i < logLines.Count; i++)
            {
                scrollText += "> ";
                scrollText += logLines.ElementAt(i);
                if (i < logLines.Count - 1)
                {
                    scrollText += "\n\n";
                }
            }
        }

        var width = (int)(Screen.width * 0.4f);
        int height;
        int scrollDepth;
        if (Hidden)
        {
            height = (int)(Screen.height * 0.03f);
            scrollDepth = height;
        }
        else
        {
            height = (int)(Screen.height * 0.3f);
            scrollDepth = height * 10;
        }

        window = new Rect(Screen.width / 2 - width / 2, 0, width, height);
        scroll = new Rect(0, 0, width * 0.9f, scrollDepth);
        scrollView = new Vector2(0, scrollDepth);
        text = new Rect(0, 0, width, scrollDepth);

        textStyle.alignment = TextAnchor.LowerLeft;
        textStyle.fontSize = Hidden ? (int)(Screen.height * 0.0165f) : (int)(Screen.height * 0.0185f);
        textStyle.normal.textColor = Color.white;
        textStyle.wordWrap = !Hidden;

        var xPadding = (int)(Screen.width * 0.01f);
        var yPadding = (int)(Screen.height * 0.01f);

        textStyle.padding = Hidden
            ? new RectOffset(xPadding / 2, xPadding / 2, yPadding / 2, yPadding / 2)
            : new RectOffset(xPadding, xPadding, yPadding, yPadding);

        var buttonWidth = (int)(Screen.width * 0.12f);
        var buttonHeight = (int)(Screen.height * 0.03f);

        hideShowButton = new Rect(Screen.width / 2 + width / 2 + buttonWidth / 3, Screen.height * 0.004f, buttonWidth,
            buttonHeight);

        // draw server command text field and button
        width = (int)(Screen.width * 0.4f);
        var xPos = (int)(Screen.width / 2.0f - width / 2.0f);
        var yPos = (int)(Screen.height * 0.307f);
        height = (int)(Screen.height * 0.022f);

        CommandTextRect = new Rect(xPos, yPos, width, height);

        width = (int)(Screen.width * 0.035f);
        yPos += (int)(Screen.height * 0.03f);
        SendCommandButton = new Rect(xPos, yPos, width, height);
    }
}