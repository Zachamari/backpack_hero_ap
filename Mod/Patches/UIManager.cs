using System;
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

namespace Backpackipelago.Patches;

public static class UIManager
{
    
    private static bool connected = false;

    [HarmonyPatch(typeof(MenuManager), nameof(MenuManager.ShowButtons)), HarmonyPrefix]
    public static void PreventOpeningSaveMenuWhenNotConnected()
    {
        BPHAP.Log("Opening main menu.");

        // idk if opening a quick run will mess anything up, so i'm disabling the buttons for them just in case
        GameObject startQuickButton = GameObject.Find("Menu Animation/Canvas/Buttons/Start Game Button");
        startQuickButton.SetActive(false);
        
        // I decided to override the Continue Quick Game button for the Archipelago menu. This is all that:
        GameObject contQuickButton = GameObject.Find("Menu Animation/Canvas/Buttons/Continue Save Game Button");


        // override the continue button's display text   
        GameObject contQuickButtonText = GameObject.Find("Menu Animation/Canvas/Buttons/Continue Save Game Button/Start Game Button Image/Continue Text");
        TextMeshProUGUI contButtonText = contQuickButtonText.GetComponent<TMPro.TextMeshProUGUI>();
        contButtonText.text = "Connect to Archipelago";


        if (!connected) {

            BPHAP.Log("Hiding the story mode button...");
            GameObject storyModeButton = GameObject.Find("Menu Animation/Canvas/Buttons/Story Mode");
            storyModeButton.SetActive(false);

        }

    }


    // This function opens the "Continue Quick Game" menu in vanilla
    [HarmonyPatch(typeof(MenuManager), nameof(MenuManager.OpenSaveMenuManager)), HarmonyPrefix]
    public static bool OpenArchipelagoMenu(ref MenuManager __instance)
    {
        BPHAP.Log("Open AP Menu Here");

        __instance.HideButtons();
        SoundManager.main.PlaySFX("menuBlip");
        GameObject menu = UnityEngine.Object.Instantiate<GameObject>(APMenu, Vector3.zero, Quaternion.identity, UnityEngine.Object.FindObjectOfType<Canvas>().transform);
        menu.transform.localPosition = Vector3.zero;
        menu.transform.localScale = Vector3.one;

        GameObject child = UnityEngine.Object.Instantiate<GameObject>(animator, menu.transform);
        Image menuBorder = child.GetComponent<Image>();
        // current problem - it just displays a white box upon clicking the button

        return false;
    }

    private static GameObject APMenu = new GameObject(
        "Archipelago Menu", 
        [
            typeof(RectTransform), 
            typeof(CanvasRenderer), 
            typeof(APOptions), 
            // typeof(SingleUI), 
            typeof(DigitalCursorInterface), 
            typeof(CanvasGroup)
        ]
    );

    private static GameObject animator = new GameObject(
        "Animation",
        [
            typeof(RectTransform),
            typeof(CanvasGroup),
            typeof(Animator),
            typeof(AnimationEvent),
            typeof(CanvasRenderer),
            typeof(UnityEngine.UI.Image),
        ]
    );


}

public class APOptions : MonoBehaviour
{
    private void Start()
    {
        this.mask.enabled = true;
        // EventSystem.current.SetSelectedGameObject(this.slotName.gameObject);

        // set all options to their defaults or stored values

        slotName.characterLimit = 16;
        slotName.lineType = TMP_InputField.LineType.SingleLine;
        slotName.text = "Player1";
        slotName.onSubmit.AddListener(slotName_OnSubmit);
        slotName.ActivateInputField();

        server.lineType = TMP_InputField.LineType.SingleLine;
        server.text = "archipelago.gg:38281";
        server.ActivateInputField();

        password.lineType = TMP_InputField.LineType.SingleLine;
        password.inputType = TMP_InputField.InputType.Password;
        password.text = "";
        password.ActivateInputField();




    }

    void slotName_OnSubmit()
    {
        BPHAP.Log("Slot Name submitted!");
    }

    void scouts_OnValueChanged()
    {
        BPHAP.Log("Scout hints toggled!");
    }

    private UnityAction<string> slotNameListener;

    private TMPro.TMP_InputField slotName;
    private TMP_InputField server;
    private TMP_InputField password;
    private UnityEngine.GameObject connectButton;
    private UnityEngine.UI.Toggle scoutHints;
    private UnityEngine.UI.Slider resourceGainMult;
    private UnityEngine.UI.Slider resourceLossMult;
    private UnityEngine.UI.Toggle bonusFreeItems;
    private Mask mask;
}