from __future__ import annotations

from typing import TYPE_CHECKING, Set

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BPHWorld


ITEM_OFFSET = 0
QUEST_OFFSET = 1000
QUEST_OFFSET_PROGRESSIVE = 1500
BUILDING_OFFSET_PROG = 2000
BUILDING_OFFSET_USEFUL = 2100
BUILDING_OFFSET_DECOR = 2200
BUILDING_OFFSET_TILE = 2300
AREA_KEYS_OFFSET = 2500
CHARACTERS_OFFSET = 2550
OTHER_PROGRESSION_OFFSET = 2600
ALTERNATE_COSTUMES_OFFSET = 2800
GENERIC_FILLER_OFFSET = 3000

ITEM_NAME_TO_ID_AND_CLASSIFICATION = {

    "Plate Armor": [1 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Clothing", "Armor", "Rare Items"]],
    "Ninja Costume": [2 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Clothing", "Armor", "Legendary Items"]],
    "Hercule Pavise": [3 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Legendary Items"]],
    "Wild Buckler": [4 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shields", "Uncommon Items"]],
    "Tattered Collar": [5 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Swamp Buckler": [6 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Rare Items"]],
    "Steel Boots": [7 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Armor", "Footwear", "Legendary Items"]],
    "Slats Shield": [8 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Common Items"]],
    "Right Gauntlet": [9 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Gloves", "Armor", "Rare Items"]],
    "Left Gauntlet": [10 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Gloves", "Armor", "Rare Items"]],
    "Mirror Shield": [11 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Legendary Items"]],
    "Li'l Buckler": [12 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shields", "Uncommon Items"]],
    "Knight's Shield": [13 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shields", "Common Items"]],
    "Knight's Armor": [14 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Armor", "Clothing", "Uncommon Items"]],
    "King's Shield": [15 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Legendary Items"]],
    "Iron Helmet": [16 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Armor", "Helmets", "Uncommon Items"]],
    "Greaves": [17 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Armor", "Footwear", "Legendary Items"]],
    "Glove of Knives": [18 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Gloves", "Armor", "Melee", "Weapons", "Uncommon Items"]],
    "Feather Cap": [19 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Helmets", "Armor", "Legendary Items"]],
    "Chainmail": [20 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Armor", "Clothing", "Uncommon Items"]],
    "Brass Knuckles": [21 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Rare Items"]],
    "Boo-Hoo Buckler": [22 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Uncommon Items"]],
    "Amethyst Buckler": [23 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shields", "Gems", "Rare Items"]],
    "Tower Shield": [24 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Rare Items"]],
    "Aged Shield": [25 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shields", "Common Items"]], # May be required if quests don't work without it if you normally start with it

    "Speedy Leaf": [26 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Rare Herb": [27 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Rare Items"]],
    "Magical Herb": [28 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Magic Items", "Common Items"]],
    "Yellow Rose": [29 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Plants" "Accessories", "Rare Items"]],
    "Tea": [30 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Uncommon Items"]],
    "Steak": [31 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Rare Items"]],
    "Star Potion": [32 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Potions", "Consumables", "Uncommon Items"]],
    "Spoiled Milk": [33 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Potions", "Consumables", "Common Items"]],
    "Poultice": [34 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Common Items"]],
    "Liquid Luck": [35 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Uncommon Items"]],
    "Glitched Potion": [36 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Potions", "Rare Items"]],
    "Fish Sword": [37 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Fish", "Melee", "Weapons", "Legendary Items"]],
    "Double Poison Potion": [38 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Potions", "Common Items"]],
    "Dodge Potion": [39 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Potions", "Uncommon Items"]],
    "Cool Drink": [40 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Common Items"]],
    "Cleansing Potion": [41 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Potions", "Common Items"]],
    "Cleansing Bomb": [42 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Potions", "Common Items"]],
    "Cave Shark": [43 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Fish", "Rare Items"]],
    "Cave Fish": [44 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Fish", "Common Items"]],
    "Bluefin": [45 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Fish", "Common Items"]],
    "Blue Rose": [46 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Plants", "Accessories", "Uncommon Items"]],
    "Flowers": [47 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Plants", "Common Items"]],
    "Angler Fish": [48 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Consumables", "Fish", "Rare Items"]],

    "Ace Cleaver": [49 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Cleavers", "Melee", "Weapons", "Legendary Items"]],
    "Golden Star": [50 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shurikens", "Weapons", "Rare Items"]],
    "Row Chain Star": [51 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shurikens", "Weapons", "Rare Items"]],
    "Alpha Star": [52 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shurikens", "Weapons", "Legendary Items"]],
    "Crow Hammer": [53 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Hammers", "Melee", "Weapons", "Rare Items"]],
    "Wooden Knife": [54 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Common Items"]],
    "Vorpal Blade": [55 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Venom Sword": [56 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Spiky Club": [57 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Melee", "Weapons", "Uncommon Items"]],
    "Smoke Dagger": [58 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Melee", "Weapons", "Rare Items"]],
    "Rapier": [59 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Mace": [60 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Rare Items"]],
    "Lucky Shiv": [61 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Rare Items"]],
    "Lizard King Sword": [62 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Stacking Star": [63 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shurikens", "Weapons", "Common Items"]],
    "Wooden Blade": [64 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Melee", "Weapons", "Common Items"]],
    "Assassin's Dagger": [65 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Golden Shiv": [66 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Rare Items"]],
    "Flame Hammer": [67 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Hammers", "Melee", "Weapons", "Rare Items"]],
    "Dueling Sword": [68 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Rare Items"]],
    "Doru": [69 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Legendary Items"]],
    "Dagger": [70 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Melee", "Weapons", "Common Items"]],
    "Copy Star": [71 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Shurikens", "Weapons", "Uncommon Items"]],
    "Column Chain Star": [72 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Shurikens", "Weapons", "Rare Items"]],
    "Claw Hammer": [73 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Hammers", "Melee", "Weapons", "Uncommon Items"]],
    "Chipped Sword": [74 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Uncommon Items"]],
    "Brutal Spear": [75 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Uncommon Items"]],
    "Queen Cleaver": [76 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Cleavers", "Melee", "Weapons", "Rare Items"]],
    "King Cleaver": [77 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Cleavers", "Melee", "Weapons", "Rare Items"]],
    "Hatchet": [78 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Melee", "Weapons", "Common Items"]],
    "Grapple": [79 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Uncommon Items"]],

    "Archer's Wand": [80 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Wands", "Magic Items", "Rare Items"]],
    "Bowblade": [81 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Bows", "Common Items"]],
    "Brick Arrow": [82 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Structures", "Arrows", "Weapons", "Uncommon Items"]],
    "Electric Arrow": [83 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Arrows", "Weapons", "Rare Items"]],
    "Expert Arrow": [84 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Bows", "Legendary Items"]],
    "Fire Arrow": [85 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Arrows", "Weapons", "Uncommon Items"]],
    "Golden Arrow": [86 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Bows", "Rare Items"]],
    "Manastone Bow": [87 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Manastones", "Bows", "Uncommon Items"]],
    "Mouse Bow": [88 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Bows", "Uncommon Items"]],
    "Poison Arrow": [89 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Arrows", "Weapons", "Uncommon Items"]],
    "Explosive Arrow": [90 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Arrows", "Weapons", "Rare Items"]],

    "Charging Manastone": [91 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Manastones", "Rare Items"]],
    "Fire Staff": [92 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Magic Items", "Wands", "Legendary Items"]],
    "Bird Chant": [93 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Magic Items", "Uncommon Items"]],
    "Blade Summoner": [94 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Legendary Items"]],
    "Dark Wand": [95 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Weapons", "Uncommon Items"]],
    "Ethereal Staff": [96 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Legendary Items"]],
    "Energy Wand": [97 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Legendary Items"]],
    "Fire Wand": [98 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Weapons", "Legendary Items"]],
    "Metallic Wand": [99 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Weapons", "Legendary Items"]],
    "Necronomicon": [100 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Books", "Accessories", "Legendary Items"]],
    "Skull Wand": [101 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Magic Items", "Wands", "Rare Items"]],
    "Warrior's Spellbook": [102 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Books", "Accessories", "Legendary Items"]],
    "Wizard Staff": [103 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Magic Items", "Wands", "Melee", "Weapons", "Uncommon Items"]],

    "Velvet Bag": [104 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Ninja Bag": [105 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Ruby": [106 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gems", "Legendary Items"]],
    "Ring of Rage": [107 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Magic Items", "Rings", "Rare Items"]],
    "Ring of Doom": [108 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Magic Items", "Rings", "Legendary Items"]],
    "Red Pearl": [109 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gems", "Legendary Items"]],
    "Magic Star Bag": [110 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Large Heart Ring": [111 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Rings", "Rare Items"]],
    "Emerald": [112 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gems", "Rare Items"]],
    "Electric Stone": [113 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Gems", "Uncommon Items"]],
    "Diamond": [114 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gems", "Rare Items"]],
    "Crab Cactus": [115 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Berserker's Ring": [116 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Rings", "Legendary Items"]],
    "Bag of Shurikens": [117 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Shuriken Forge": [118 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Rare Items"]],
    "Amethyst": [119 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Accessories", "Gems", "Rare Items"]],

    "Cleansing Flame": [120 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],
    "Fluffy Cotton": [121 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],
    "Ice Cream": [122 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],
    "Reverse Hourglass": [123 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],
    "Spicy Ginger": [124 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],
    "Tusk": [125 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Relics"]],

    "Spectral Orb": [126 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Ghost Gem": [127 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gems", "Rare Items"]],
    "Ghost Glove": [128 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Gloves", "Uncommon Items"]],
    "Minute Hand": [129 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Common Items"]],
    "Hour Hand": [130 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Golden Whetstone": [131 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Verdant Energy": [132 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Crimson Energy": [133 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Legendary Items"]],
    "Unstable Manastone": [134 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Manastones", "Consumables", "Uncommon Items"]],
    "Pacifist's Ring": [135 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Rings", "Legendary Items"]],
    "Monad's Mjolnir": [136 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Hammers", "Melee", "Weapons", "Legendary Items"]],

    # skipped a few IDs just in case I missed some quest items
    "Pouch": [150 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Accessories", "Uncommon Items"]],
    "Fishing Hook": [151 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Uncommon Items"]],
    "Jack Cleaver": [152 + ITEM_OFFSET, ItemClassification.progression_deprioritized, ["Dungeon Items", "Cleavers", "Melee", "Weapons", "Uncommon Items"]], # I somehow skipped this item when going through Barracks research, so that's why its ID is way further than all the other ones in that building
    "Berserker's Club": [153 + ITEM_OFFSET, ItemClassification.useful, ["Dungeon Items", "Melee", "Weapons", "Uncommon Items"]], # same with this one
    


    "Quest: Red Tusk": [1 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Ice Cream (Purse)": [2 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Ice Cream (Satchel)": [3 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests"]],
    "Quest: Red Root": [4 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Red Flame": [5 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Red Cotton": [6 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Pacifist": [7 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests"]],
    "Quest: Micro Build": [8 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: Magnetized": [9 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: Fragile Tribe": [10 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests"]],
    "Quest: Effigies": [11 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests"]],
    "Quest: Easy Mode (Satchel)": [12 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests", "Easy Mode"]],
    "Quest: Easy Mode (Tote)": [13 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Tote Quests", "Easy Mode"]],
    "Quest: Easy Mode (Pochette)": [14 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests", "Easy Mode"]],
    "Quest: Easy Mode (CR-8)": [15 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests", "Easy Mode"]],
    "Quest: Duo Core": [16 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: Quad Core": [17 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: Spinning Core": [18 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: This One's On Me": [19 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Treats Only": [20 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests"]],
    "Quest: Warrior Bird": [21 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests"]],
    "Quest: Builder Bird": [22 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests"]],
    "Quest: Reaper": [23 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests"]],
    "Quest: Archery Mastery": [24 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Magic Archery": [25 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Tote Quests"]],
    "Quest: Magic Expedition": [26 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Mushroom Friend": [27 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Tote Quests"]],
    "Quest: Sap Primer": [28 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Tote Quests"]],
    "Quest: Bumpy Ride": [29 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "CR-8 Quests"]],
    "Quest: Throw the Book at Them": [30 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Tote Quests"]],
    "Quest: Cramped": [31 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],

    "Quest: Protector": [32 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Wizard's School": [33 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Energy Delivery": [34 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Campaign Trail": [35 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Archery Lessons": [36 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Fishy Business": [37 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Ghostly!": [38 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Master of Whetstones": [39 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Quest: Everyone Comes Home": [40 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Pochette Quests"]],
    "Quest: Meditation": [41 + QUEST_OFFSET, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],

    "Progressive Quest: Hourglass": [1 + QUEST_OFFSET_PROGRESSIVE, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Progressive Quest: Scissors": [2 + QUEST_OFFSET_PROGRESSIVE, ItemClassification.progression_deprioritized, ["Quests", "Satchel Quests"]],
    "Progressive Quest: Coral": [3 + QUEST_OFFSET_PROGRESSIVE, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],
    "Progressive Quest: Windmill": [4 + QUEST_OFFSET_PROGRESSIVE, ItemClassification.progression_deprioritized, ["Quests", "Purse Quests"]],


    "Bounty Board": [1 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Blacksmith": [2 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Tavern": [3 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Barracks": [4 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings", "Resource-Generating Buildings"]],
    "Carpenter": [5 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Fletcher": [6 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings", "Resource-Generating Buildings"]],
    "Magical Mycelium": [7 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings", "Resource-Generating Buildings"]],
    "Jeweler": [8 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Library": [9 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Greenhouse": [10 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Schoolhouse": [11 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Research Buildings"]],
    "Town Hall": [12 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Important Buildings"]],
    "House": [13 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Important Buildings"]],
    "Farm": [14 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Resource-Generating Buildings"]], # I think you need this for one of Mayor's requests iirc,
    "Beacon": [15 + BUILDING_OFFSET_PROG, ItemClassification.progression, ["Buildings", "Important Buildings"]],

    "Quarry": [1 + BUILDING_OFFSET_USEFUL, ItemClassification.useful, ["Buildings", "Resource-Generating Buildings"]],
    "Bank": [2 + BUILDING_OFFSET_USEFUL, ItemClassification.useful, ["Buildings"]],
    "Sawmill": [3 + BUILDING_OFFSET_USEFUL, ItemClassification.useful, ["Buildings", "Resource-Generating Buildings"]],
    "Fishing Shack": [4 + BUILDING_OFFSET_USEFUL, ItemClassification.useful, ["Buildings", "Resource-Generating Buildings"]],

    "Weapon Rack": [1 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Signpost": [2 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Beehives": [3 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Washbin": [4 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Sconce": [5 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Mary Statue": [6 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Market Stand A": [7 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Kate Statue": [8 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Gravestone": [9 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Cart": [10 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Candelabra": [11 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Camp Stove": [12 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Barricade": [13 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Trough": [14 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Anna Statue": [15 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Target": [16 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Barrel": [17 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Blue Hyacinth": [18 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Boulder": [19 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Bush": [20 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Cosmo": [21 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Dianthus": [22 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Garden Bed": [23 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Pine Tree": [24 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Primrose": [25 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Purple Hyacinth": [26 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Rock": [27 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Yellow Hyacinth": [28 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Crate": [29 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Pot": [30 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],
    "Item Pedestal": [31 + BUILDING_OFFSET_DECOR, ItemClassification.filler, ["Decorations"]],


    "Stone Path": [1 + BUILDING_OFFSET_TILE, ItemClassification.filler, ["Decorations", "Paths"]],
    "Farmland": [2 + BUILDING_OFFSET_TILE, ItemClassification.filler, ["Decorations", "Paths"]],
    "Brick Path": [3 + BUILDING_OFFSET_TILE, ItemClassification.filler, ["Decorations", "Paths"]],


    "Key to the Bramble": [1 + AREA_KEYS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Dungeon Area Keys"]],
    "Key to the Deep Caves": [2 + AREA_KEYS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Dungeon Area Keys"]],
    "Key to the Enchanted Swamp": [3 + AREA_KEYS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Dungeon Area Keys"]],
    "Key to the Magma Core": [4 + AREA_KEYS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Dungeon Area Keys"]],
    "Key to the Frozen Heart": [5 + AREA_KEYS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Dungeon Area Keys"]],


    "Satchel": [1 + CHARACTERS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Playable Characters"]],
    "Tote": [2 + CHARACTERS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Playable Characters"]],
    "Pochette": [3 + CHARACTERS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Playable Characters"]],
    "CR-8": [4 + CHARACTERS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Playable Characters"]],
    "Purse": [5 + CHARACTERS_OFFSET, ItemClassification.progression | ItemClassification.useful, ["Playable Characters"]],


    "Tote's Totem": [1 + OTHER_PROGRESSION_OFFSET, ItemClassification.progression_deprioritized, ["Other Progression Items"]], # not sure if this can be shuffled yet,


    "Blue Costume (Purse)": [1 + ALTERNATE_COSTUMES_OFFSET, ItemClassification.filler, ["Alternate Costumes"]],
    "Rogue Costume (Purse)": [2 + ALTERNATE_COSTUMES_OFFSET, ItemClassification.filler, ["Alternate Costumes"]],
    "Feral Costume (Purse)": [3 + ALTERNATE_COSTUMES_OFFSET, ItemClassification.filler, ["Alternate Costumes"]],
    "Elder Costume (Purse)": [4 + ALTERNATE_COSTUMES_OFFSET, ItemClassification.filler, ["Alternate Costumes"]],
    # Other costume names needed


    "Cornucopia": [1 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    "Golden Cheese": [2 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    "Golden Feather": [3 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    "Golden Gear": [4 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    "Golden Seed": [5 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    "Golden Shell": [6 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # Apparently I literally don't have every loot item discovered in my save file, and I don't really feel like writing code that will show them to me
    # "Huge Bag of Coins": [7 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Old Coins": [8 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Supplies": [9 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Box of Nails": [10 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Bowl of Fruit": [11 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Bag of Treasure": [12 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],
    # "Coin Purse": [13 + GENERIC_FILLER_OFFSET, ItemClassification.filler, ["Loot"]],

}

def get_item_name_to_id() -> dict[str, int]:
    ITEM_NAME_TO_ID = {}
    for item in ITEM_NAME_TO_ID_AND_CLASSIFICATION:
        ITEM_NAME_TO_ID.update({item: ITEM_NAME_TO_ID_AND_CLASSIFICATION[item][0]})
    return ITEM_NAME_TO_ID


def get_item_classifications() -> dict[str, ItemClassification]:
    DEFAULT_ITEM_CLASSIFICATIONS = {}
    for item in ITEM_NAME_TO_ID_AND_CLASSIFICATION:
        DEFAULT_ITEM_CLASSIFICATIONS.update({item: ITEM_NAME_TO_ID_AND_CLASSIFICATION[item][1]})
    return DEFAULT_ITEM_CLASSIFICATIONS


class BPHItem(Item):
    game = "Backpack Hero"


def get_item_groups() -> dict[str, Set[str]]:
    item_groups = {}
    for item in ITEM_NAME_TO_ID_AND_CLASSIFICATION:
        item_groups.update({item: ITEM_NAME_TO_ID_AND_CLASSIFICATION[item][2]})
    return item_groups



def get_random_filler_item_name(world: BPHWorld) -> str:
    
    match world.random.randint(0, 6):
        case 0:
            return "Cornucopia"
        case 1:
            return "Golden Cheese"
        case 2:
            return "Golden Feather"
        case 3:
            return "Golden Gear"
        case 4:
            return "Golden Seed"
        case 5:
            return "Golden Shell"
    
    return "Dev Is Stupid And Doesn't Know How The RandInt Function Works" # python has inclusive on one end and exclusive on the other, and it always fucks me up, so I just put this here to catch if I made a dumb mistake with the randint function


def create_item_with_correct_classification(world: BPHWorld, name: str) -> BPHItem:
    
    classification = ITEM_NAME_TO_ID_AND_CLASSIFICATION[name][1]
    
    # classification changing shenanigans go here

    return BPHItem(name, classification, ITEM_NAME_TO_ID_AND_CLASSIFICATION[name][0], world.player)


def create_all_items(world: BPHWorld) -> None:

    itempool: list[Item] = [
        
        world.create_item("Plate Armor"),
        world.create_item("Ninja Costume"),
        world.create_item("Hercule Pavise"),
        world.create_item("Wild Buckler"),
        world.create_item("Tattered Collar"),
        world.create_item("Swamp Buckler"),
        world.create_item("Steel Boots"),
        world.create_item("Slats Shield"),
        world.create_item("Right Gauntlet"),
        world.create_item("Left Gauntlet"),
        world.create_item("Mirror Shield"),
        world.create_item("Li'l Buckler"),
        world.create_item("Knight's Shield"),
        world.create_item("Knight's Armor"),
        world.create_item("King's Shield"),
        world.create_item("Iron Helmet"),
        world.create_item("Greaves"),
        world.create_item("Glove of Knives"),
        world.create_item("Feather Cap"),
        world.create_item("Chainmail"),
        world.create_item("Brass Knuckles"),
        world.create_item("Boo-Hoo Buckler"),
        world.create_item("Amethyst Buckler"),
        world.create_item("Tower Shield"),
        world.create_item("Aged Shield"),
        
        world.create_item("Speedy Leaf"),
        world.create_item("Rare Herb"),
        world.create_item("Magical Herb"),
        world.create_item("Yellow Rose"),
        world.create_item("Tea"),
        world.create_item("Steak"),
        world.create_item("Star Potion"),
        world.create_item("Spoiled Milk"),
        world.create_item("Poultice"),
        world.create_item("Liquid Luck"),
        world.create_item("Glitched Potion"),
        world.create_item("Fish Sword"),
        world.create_item("Double Poison Potion"),
        world.create_item("Dodge Potion"),
        world.create_item("Cool Drink"),
        world.create_item("Cleansing Potion"),
        world.create_item("Cleansing Bomb"),
        world.create_item("Cave Shark"),
        world.create_item("Cave Fish"),
        world.create_item("Bluefin"),
        world.create_item("Blue Rose"),
        world.create_item("Flowers"),
        world.create_item("Angler Fish"),

        world.create_item("Ace Cleaver"),
        world.create_item("Golden Star"),
        world.create_item("Row Chain Star"),
        world.create_item("Alpha Star"),
        world.create_item("Crow Hammer"),
        world.create_item("Wooden Knife"),
        world.create_item("Vorpal Blade"),
        world.create_item("Venom Sword"),
        world.create_item("Spiky Club"),
        world.create_item("Smoke Dagger"),
        world.create_item("Rapier"),
        world.create_item("Mace"),
        world.create_item("Lucky Shiv"),
        world.create_item("Lizard King Sword"),
        world.create_item("Stacking Star"),
        world.create_item("Wooden Blade"),
        world.create_item("Assassin's Dagger"),
        world.create_item("Golden Shiv"),
        world.create_item("Flame Hammer"),
        world.create_item("Dueling Sword"),
        world.create_item("Doru"),
        world.create_item("Dagger"),
        world.create_item("Copy Star"),
        world.create_item("Column Chain Star"),
        world.create_item("Claw Hammer"),
        world.create_item("Chipped Sword"),
        world.create_item("Brutal Spear"),
        world.create_item("Jack Cleaver"),
        world.create_item("Queen Cleaver"),
        world.create_item("King Cleaver"),
        world.create_item("Hatchet"),
        world.create_item("Grapple"),
        world.create_item("Berserker's Club"),
        
        world.create_item("Archer's Wand"),
        world.create_item("Bowblade"),
        world.create_item("Brick Arrow"),
        world.create_item("Electric Arrow"),
        world.create_item("Expert Arrow"),
        world.create_item("Fire Arrow"),
        world.create_item("Golden Arrow"),
        world.create_item("Manastone Bow"),
        world.create_item("Mouse Bow"),
        world.create_item("Poison Arrow"),
        world.create_item("Explosive Arrow"),
        
        world.create_item("Charging Manastone"),
        world.create_item("Fire Staff"),
        world.create_item("Bird Chant"),
        world.create_item("Blade Summoner"),
        world.create_item("Dark Wand"),
        world.create_item("Ethereal Staff"),
        world.create_item("Energy Wand"),
        world.create_item("Fire Wand"),
        world.create_item("Metallic Wand"),
        world.create_item("Necronomicon"),
        world.create_item("Skull Wand"),
        world.create_item("Warrior's Spellbook"),
        world.create_item("Wizard Staff"),

        world.create_item("Velvet Bag"),
        world.create_item("Ninja Bag"),
        world.create_item("Ruby"),
        world.create_item("Ring of Rage"),
        world.create_item("Ring of Doom"),
        world.create_item("Red Pearl"),
        world.create_item("Magic Star Bag"),
        world.create_item("Large Heart Ring"),
        world.create_item("Emerald"),
        world.create_item("Electric Stone"),
        world.create_item("Diamond"),
        world.create_item("Crab Cactus"),
        world.create_item("Berserker's Ring"),
        world.create_item("Bag of Shurikens"),
        world.create_item("Shuriken Forge"),
        world.create_item("Amethyst"),

        world.create_item("Cleansing Flame"),
        world.create_item("Fluffy Cotton"),
        world.create_item("Ice Cream"),
        world.create_item("Reverse Hourglass"),
        world.create_item("Spicy Ginger"),
        world.create_item("Tusk"),
        
        world.create_item("Spectral Orb"),
        world.create_item("Ghost Gem"),
        world.create_item("Ghost Glove"),
        world.create_item("Minute Hand"),
        world.create_item("Hour Hand"),
        world.create_item("Golden Whetstone"),
        world.create_item("Verdant Energy"),
        world.create_item("Crimson Energy"),
        world.create_item("Unstable Manastone"),
        world.create_item("Pacifist's Ring"),
        world.create_item("Monad's Mjolnir"),

        world.create_item("Pouch"),
        world.create_item("Fishing Hook"),

        
        world.create_item("Bounty Board"),
        world.create_item("Blacksmith"),
        world.create_item("Tavern"),
        world.create_item("Barracks"),
        world.create_item("Carpenter"),
        world.create_item("Fletcher"),
        world.create_item("Magical Mycelium"),
        world.create_item("Jeweler"),
        world.create_item("Library"),
        world.create_item("Greenhouse"),
        world.create_item("Schoolhouse"),
        world.create_item("Town Hall"),
        world.create_item("House"),
        world.create_item("Farm"),
        world.create_item("Beacon"),

        world.create_item("Quarry"),
        world.create_item("Bank"),
        world.create_item("Sawmill"),
        world.create_item("Fishing Shack"),


        world.create_item("Stone Path"),
        world.create_item("Farmland"),
        world.create_item("Brick Path"),

        world.create_item("Key to the Bramble"),
        world.create_item("Key to the Deep Caves"),
        world.create_item("Key to the Enchanted Swamp"),
        world.create_item("Key to the Magma Core"),
        world.create_item("Key to the Frozen Heart"),


        world.create_item("Satchel"),
        world.create_item("Tote"),
        world.create_item("Pochette"),
        world.create_item("CR-8"),

        world.create_item("Tote's Totem"),


    ]


    # TODO: Add a reference to a yaml option here
    quests: list[Item] = [

        world.create_item("Quest: Red Tusk"),
        world.create_item("Quest: Ice Cream (Purse)"),
        world.create_item("Quest: Ice Cream (Satchel)"),
        world.create_item("Quest: Red Root"),
        world.create_item("Quest: Red Flame"),
        world.create_item("Quest: Red Cotton"),
        world.create_item("Quest: Pacifist"),
        world.create_item("Quest: Micro Build"),
        world.create_item("Quest: Magnetized"),
        world.create_item("Quest: Fragile Tribe"),
        world.create_item("Quest: Effigies"),
        world.create_item("Quest: Easy Mode (Satchel)"),
        world.create_item("Quest: Easy Mode (Tote)"),
        world.create_item("Quest: Easy Mode (Pochette)"),
        world.create_item("Quest: Easy Mode (CR-8)"),
        world.create_item("Quest: Duo Core"),
        world.create_item("Quest: Quad Core"),
        world.create_item("Quest: Spinning Core"),
        world.create_item("Quest: This One's On Me"),
        world.create_item("Quest: Treats Only"),
        world.create_item("Quest: Warrior Bird"),
        world.create_item("Quest: Builder Bird"),
        world.create_item("Quest: Reaper"),
        world.create_item("Quest: Archery Mastery"),
        world.create_item("Quest: Magic Archery"),
        world.create_item("Quest: Magic Expedition"),
        world.create_item("Quest: Mushroom Friend"),
        world.create_item("Quest: Sap Primer"),
        world.create_item("Quest: Bumpy Ride"),
        world.create_item("Quest: Throw the Book at Them"),
        world.create_item("Quest: Cramped"),

        world.create_item("Quest: Protector"),
        world.create_item("Quest: Wizard's School"),
        world.create_item("Quest: Energy Delivery"),
        world.create_item("Quest: Campaign Trail"),
        world.create_item("Quest: Archery Lessons"),
        world.create_item("Quest: Fishy Business"),
        world.create_item("Quest: Ghostly!"),
        world.create_item("Quest: Master of Whetstones"),
        world.create_item("Quest: Everyone Comes Home"),
        world.create_item("Quest: Meditation"),

        world.create_item("Progressive Quest: Hourglass"),
        world.create_item("Progressive Quest: Scissors"),
        world.create_item("Progressive Quest: Coral"),
        world.create_item("Progressive Quest: Windmill"),

        world.create_item("Progressive Quest: Hourglass"),
        world.create_item("Progressive Quest: Scissors"),
        world.create_item("Progressive Quest: Coral"),
        world.create_item("Progressive Quest: Windmill"),

    ]

    for i in quests:
        itempool.append(i)


    # TODO: Add setting here
    costumes: list[Item] = [
        
        world.create_item("Blue Costume (Purse)"),
        world.create_item("Rogue Costume (Purse)"),
        world.create_item("Feral Costume (Purse)"),
        world.create_item("Elder Costume (Purse)"),
        # TODO: add more here
    ]

    for i in costumes:
        itempool.append(i)


    # Checking that num. items == num. locations and correcting if necessary

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    filler_decor: list[str] = [

        "Weapon Rack",
        "Signpost",
        "Beehives",
        "Washbin",
        "Sconce",
        "Mary Statue",
        "Market Stand A",
        "Kate Statue",
        "Gravestone",
        "Cart",
        "Candelabra",
        "Camp Stove",
        "Barricade",
        "Trough",
        "Anna Statue",
        "Target",
        "Barrel",
        "Blue Hyacinth",
        "Boulder",
        "Bush",
        "Cosmo",
        "Dianthus",
        "Garden Bed",
        "Pine Tree",
        "Primrose",
        "Purple Hyacinth",
        "Rock",
        "Yellow Hyacinth",
        "Crate",
        "Pot",
        "Item Pedestal",

    ]

    needed_number_of_filler_items_if_all_decor_added = needed_number_of_filler_items - len(filler_decor)

    if needed_number_of_filler_items_if_all_decor_added < 0: # if adding every decor item would lead to items > locations (likely to happen while still figuring out where locations are, may be able to be removed later)
        loops = needed_number_of_filler_items
        while loops > 0:
            decor_selected = filler_decor[world.random.randint(0, len(filler_decor) - 1)]
            itempool.append(world.create_item(decor_selected))
            loops -= 1
    else:
        if needed_number_of_filler_items_if_all_decor_added == 0:
            for i in filler_decor:
                itempool.append(world.create_item(i))
        else: # here, needed_number_of_filler_items_if_all_decor_added > 0
            for i in filler_decor:
                itempool.append(world.create_item(i))
            itempool += [world.create_filler() for _ in range(needed_number_of_filler_items_if_all_decor_added)]

    # Items should now equal locations

    world.multiworld.itempool += itempool

    world.push_precollected(world.create_item("Purse")) # might as well add her as a starting item to make the web tracker a bit easier to read

