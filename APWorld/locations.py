from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

from rule_builder.rules import Has

if TYPE_CHECKING:
    from .world import BPHWorld


RESEARCH_OFFSET_BOUNTY = 0
RESEARCH_OFFSET_SMITH = 100
RESEARCH_OFFSET_TAV = 200
RESEARCH_OFFSET_BAR = 300
RESEARCH_OFFSET_CARP = 400
RESEARCH_OFFSET_FLETCH = 500
RESEARCH_OFFSET_MAGIC = 600
RESEARCH_OFFSET_JEWEL = 700
RESEARCH_OFFSET_LIB = 800
RESEARCH_OFFSET_GREEN = 900
RESEARCH_OFFSET_OTHER = 1000

QUEST_OFFSET_PURSE = 1500
QUEST_OFFSET_SATCHEL = 1600
QUEST_OFFSET_TOTE = 1700
QUEST_OFFSET_POCHETTE = 1800
QUEST_OFFSET_CR8 = 1900

NPC_LOCATION_OFFSET_LOUIS = 2000
NPC_LOCATION_OFFSET_MAYOR = 2050
NPC_LOCATION_OFFSET_VIV = 2100
NPC_LOCATION_OFFSET_ZAAR = 2150
NPC_LOCATION_OFFSET_MATT = 2200
NPC_LOCATION_OFFSET_MS_B = 2250
NPC_LOCATION_OFFSET_ARCHER = 2300
NPC_LOCATION_OFFSET_FISHER = 2350
NPC_LOCATION_OFFSET_CONST = 2400
NPC_LOCATION_OFFSET_WART = 2450
NPC_LOCATION_OFFSET_DOUG = 2500
NPC_LOCATION_OFFSET_PASHA = 2550
NPC_LOCATION_OFFSET_NORA = 2600
NPC_LOCATION_OFFSET_PARCEL = 2650
NPC_LOCATION_OFFSET_OTHER = 2700 # there WILL be more later because I forgot some, reorganize as needed and put any single-item NPCs in this category
DUNGEON_LOCATION_OFFSET = 3000



LOCATION_NAME_TO_ID = {
    "Bounty Board Research - Quest: Red Tusk": 1 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Ice Cream (Purse)": 2 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Ice Cream (Satchel)": 3 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Red Root": 4 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Red Flame": 5 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Red Cotton": 6 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Pacifist": 7 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Micro Build": 8 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Magnetized": 9 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Hourglass 1": 10 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Fragile Tribe": 11 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Effigies": 12 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Easy Mode (Satchel)": 13 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Easy Mode (Tote)": 14 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Easy Mode (Pochette)": 15 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Easy Mode (CR-8)": 16 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Scissors": 17 + RESEARCH_OFFSET_BOUNTY,
    "Bounty Board Research - Quest: Duo Core": 18 + RESEARCH_OFFSET_BOUNTY,

    "Blacksmith Research - Plate Armor": 1 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Ninja Costume": 2 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Hercule Pavise": 3 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Wild Buckler": 4 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Tattered Collar": 5 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Swamp Buckler": 6 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Steel Boots": 7 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Slats Shield": 8 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Right Gauntlet": 9 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Left Gauntlet": 10 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Mirror Shield": 11 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Li'l Buckler": 12 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Knight's Shield": 13 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Knight's Armor": 14 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - King's Shield": 15 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Iron Helmet": 16 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Greaves": 17 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Glove of Knives": 18 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Feather Cap": 19 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Chainmail": 20 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Brass Knuckles": 21 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Boo-Hoo Buckler": 22 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Amethyst Buckler": 23 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Tower Shield": 24 + RESEARCH_OFFSET_SMITH,
    "Blacksmith Research - Aged Shield": 25 + RESEARCH_OFFSET_SMITH,

    "Tavern Research - Speedy Leaf": 1 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Rare Herb": 2 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Magical Herb": 3 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Quest: This One's On Me": 4 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Quest: Treats Only": 5 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Yellow Rose": 6 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Tea": 7 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Steak": 8 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Star Potion": 9 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Spoiled Milk": 10 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Poultice": 11 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Liquid Luck": 12 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Glitched Potion": 13 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Fish Sword": 14 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Double Poison Potion": 15 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Dodge Potion": 16 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Cool Drink": 17 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Cleansing Potion": 18 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Cleansing Bomb": 19 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Cave Shark": 20 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Cave Fish": 21 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Bluefin": 22 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Blue Rose": 23 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Flowers": 24 + RESEARCH_OFFSET_TAV,
    "Tavern Research - Angler Fish": 25 + RESEARCH_OFFSET_TAV,

    "Barracks Research - Ace Cleaver": 1 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Golden Star": 2 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Quest: Warrior Bird": 3 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Row Chain Star": 4 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Alpha Star": 5 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Crow Hammer": 6 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Wooden Knife": 7 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Weapon Rack": 8 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Vorpal Blade": 9 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Venom Sword": 10 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Spiky Club": 11 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Smoke Dagger": 12 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Rapier": 13 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Mace": 14 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Lucky Shiv": 15 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Lizard King Sword": 16 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Quest: Reaper": 17 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Stacking Star": 18 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Wooden Blade": 19 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Assassin's Dagger": 20 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Golden Shiv": 21 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Flame Hammer": 22 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Dueling Sword": 23 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Doru": 24 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Dagger": 25 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Copy Star": 26 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Column Chain Star": 27 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Claw Hammer": 28 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Chipped Sword": 29 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Brutal Spear": 30 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Jack Cleaver": 31 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Queen Cleaver": 32 + RESEARCH_OFFSET_BAR,
    "Barracks Research - King Cleaver": 33 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Hatchet": 34 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Grapple": 35 + RESEARCH_OFFSET_BAR,
    "Barracks Research - Berserker's Club": 36 + RESEARCH_OFFSET_BAR,

    "Carpenter Research - Signpost": 1 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Beehives": 2 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Quest: Builder Bird": 3 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Washbin": 4 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Sconce": 5 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Quarry": 6 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Mary Statue": 7 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Market Stand A": 8 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Kate Statue": 9 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Greenhouse": 10 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Gravestone": 11 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Cart": 12 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Candelabra": 13 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Camp Stove": 14 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Barricade": 15 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Bank": 16 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Trough": 17 + RESEARCH_OFFSET_CARP,
    "Carpenter Research - Anna Statue": 18 + RESEARCH_OFFSET_CARP,

    "Fletcher Research - Quest: Archery Mastery": 1 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Archer's Wand": 2 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Bowblade": 3 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Brick Arrow": 4 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Electric Arrow": 5 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Expert Bow": 6 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Fire Arrow": 7 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Golden Bow": 8 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Manastone Bow": 9 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Mouse Bow": 10 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Poison Arrow": 11 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Target": 12 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Quest: Magic Archery": 13 + RESEARCH_OFFSET_FLETCH,
    "Fletcher Research - Explosive Arrow": 14 + RESEARCH_OFFSET_FLETCH,
    
    "Magical Mycelium Research - Charging Manastone": 1 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Fire Staff": 2 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Quest: Magic Expedition": 3 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Quest: Mushroom Friend": 4 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Quest: Sap Primer": 5 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Bird Chant": 6 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Blade Summoner": 7 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Dark Wand": 8 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Ethereal Staff": 9 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Energy Wand": 10 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Fire Wand": 11 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Metallic Wand": 12 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Necronomicon": 13 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Skull Wand": 14 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Warrior's Spellbook": 15 + RESEARCH_OFFSET_MAGIC,
    "Magical Mycelium Research - Wizard Staff": 16 + RESEARCH_OFFSET_MAGIC,
    
    "Jeweler Research - Velvet Bag": 1 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Ninja Bag": 2 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Quest: Bumpy Ride": 3 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Ruby": 4 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Ring of Rage": 5 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Ring of Doom": 6 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Red Pearl": 7 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Magic Star Bag": 8 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Large Heart Ring": 9 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Emerald": 10 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Electric Stone": 11 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Diamond": 12 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Crab Cactus": 13 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Berserker's Ring": 14 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Bag of Shurikens": 15 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Shuriken Forge": 16 + RESEARCH_OFFSET_JEWEL,
    "Jeweler Research - Amethyst": 17 + RESEARCH_OFFSET_JEWEL,
    
    "Library Research - Quest: Throw the Book at Them": 1 + RESEARCH_OFFSET_LIB,
    "Library Research - Cleansing Flame": 2 + RESEARCH_OFFSET_LIB,
    "Library Research - Fluffy Cotton": 3 + RESEARCH_OFFSET_LIB,
    "Library Research - Ice Cream": 4 + RESEARCH_OFFSET_LIB,
    "Library Research - Reverse Hourglass": 5 + RESEARCH_OFFSET_LIB,
    "Library Research - Spicy Ginger": 6 + RESEARCH_OFFSET_LIB,
    "Library Research - Tusk": 7 + RESEARCH_OFFSET_LIB,

    "Greenhouse Research - Barrel": 1 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Blue Hyacinth": 2 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Boulder": 3 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Bush": 4 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Cosmo": 5 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Dianthus": 6 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Garden Bed": 7 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Pine Tree": 8 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Primrose": 9 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Purple Hyacinth": 10 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Rock": 11 + RESEARCH_OFFSET_GREEN,
    "Greenhouse Research - Yellow Hyacinth": 12 + RESEARCH_OFFSET_GREEN,

    "Schoolhouse Research - Quest: Cramped": 1 + RESEARCH_OFFSET_OTHER,

    "Matthew Research - Key to the Deep Caves": 2 + RESEARCH_OFFSET_OTHER,
    "Matthew Research - Key to the Bramble": 3 + RESEARCH_OFFSET_OTHER,
    "Matthew Research - Key to the Magma Core": 4 + RESEARCH_OFFSET_OTHER,
    "Matthew Research - Key to the Frozen Heart": 5 + RESEARCH_OFFSET_OTHER,
    "Matthew Research - Key to the Enchanted Swamp": 6 + RESEARCH_OFFSET_OTHER,

    "Pasha Research - Stone Path": 7 + RESEARCH_OFFSET_OTHER,
    "Pasha Research - Farmland": 8 + RESEARCH_OFFSET_OTHER,
    "Pasha Research - Brick Path": 9 + RESEARCH_OFFSET_OTHER,

    "Constance Research - CR-8": 10 + RESEARCH_OFFSET_OTHER,
    "Constance Research - Beacon": 11 + RESEARCH_OFFSET_OTHER,


    "Louis - Quest: Protector": 1 + NPC_LOCATION_OFFSET_LOUIS,

    "Pasha - First Meeting Gift (Bounty Board)": 1 + NPC_LOCATION_OFFSET_PASHA,

    "Nora - Proto Manastone Reward 1 (Magical Mycelium)": 1 + NPC_LOCATION_OFFSET_NORA,
    "Nora - Proto Manastone Reward 2 (Quest: Wizard's School)": 2 + NPC_LOCATION_OFFSET_NORA,
    # "Nora - Built Magical Mycelium Reward (Tote's Totem)": 3 + NPC_LOCATION_OFFSET_NORA,
    
    "Zaar - Built Store Reward (Quest: Energy Delivery)": 1 + NPC_LOCATION_OFFSET_ZAAR,
    "Zaar - Finished 3 Runs Reward 1 (Crate)": 2 + NPC_LOCATION_OFFSET_ZAAR,
    "Zaar - Finished 3 Runs Reward 2 (Pot)": 3 + NPC_LOCATION_OFFSET_ZAAR,
    "Zaar - Finished 4 Runs Reward 1 (Quest: Coral 1)": 4 + NPC_LOCATION_OFFSET_ZAAR,
    "Zaar - Finished 4 Runs Reward 2 (Quest: Windmill 1)": 5 + NPC_LOCATION_OFFSET_ZAAR,

    "Mayor Quillswish - First Meeting Gift 1 (Farm)": 1 + NPC_LOCATION_OFFSET_MAYOR,
    "Mayor Quillswish - First Meeting Gift 2 (House)": 2 + NPC_LOCATION_OFFSET_MAYOR,
    "Mayor Quillswish - Mayor Quillswish Plush Reward (Quest: Campaign Trail)": 3 + NPC_LOCATION_OFFSET_MAYOR,

    "Sir Wartsley - First Meeting Gift 1 (Jeweler)": 1 + NPC_LOCATION_OFFSET_WART,
    "Sir Wartsley - First Meeting Gift 2 (Item Pedestal)": 2 + NPC_LOCATION_OFFSET_WART,

    "Vivienne - First Meeting Gift (Library)": 1 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - 1 Etching Reward (Purse Costume)": 2 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - 2 Etchings Reward (Purse Costume)": 3 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - 3 Etchings Reward (Purse Costume)": 4 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - 4 Etchings Reward (Purse Costume)": 5 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - 5 Etchings Reward (Purse Costume)": 6 + NPC_LOCATION_OFFSET_VIV,

    "Vivienne - First Hymn Reward (Satchel Costume)": 10 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - Second Hymn Reward (Satchel Costume)": 11 + NPC_LOCATION_OFFSET_VIV,

    "Vivienne - First Rune Reward (Tote Costume)": 15 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - Second Rune Reward (Tote Costume)": 16 + NPC_LOCATION_OFFSET_VIV,

    "Vivienne - First Sigil Reward (Pochette Costume)": 20 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - Second Sigil Reward (Pochette Costume)": 21 + NPC_LOCATION_OFFSET_VIV,
    
    "Vivienne - First Floppy Disk Reward (CR-8 Costume)": 25 + NPC_LOCATION_OFFSET_VIV,
    "Vivienne - Second Floppy Disk Reward (CR-8 Costume)": 26 + NPC_LOCATION_OFFSET_VIV,
    # Fix these names once I figure out the vanilla unlock conditions

    "Parcel - First Meeting Gift (Pouch)": 1 + NPC_LOCATION_OFFSET_PARCEL, # Likely will move this check to "OTHER", I don't think he gives you anything else

    "Master Archer - Town Meeting Gift (Quest: Archery Lessons)": 1 + NPC_LOCATION_OFFSET_ARCHER,

    "Miss Burrough - First Meeting Gift (Schoolhouse)": 1 + NPC_LOCATION_OFFSET_MS_B,

    "Doug - First Meeting Gift (Sawmill)": 1 + NPC_LOCATION_OFFSET_DOUG,

    "Fish Enthusiast - First Meeting Gift (Fishing Hook)": 1 + NPC_LOCATION_OFFSET_FISHER,
    "Fish Enthusiast - Fish Reward 1 (Quest: Fishy Business)": 2 + NPC_LOCATION_OFFSET_FISHER,
    "Fish Enthusiast - Fish Reward 2 (Fishing Shack)": 3 + NPC_LOCATION_OFFSET_FISHER,

    # More locations go here once I remember that they exist

    # I don't remember where these locations are unlocked, but I should be able to send them clientside anyway until I figure out when they get sent
    "??? - ??? (Quest: Ghostly!)": 1 + NPC_LOCATION_OFFSET_OTHER, # this might be that one ghost character in town?
    "??? - ??? (Quest: Master of Whetstones)": 2 + NPC_LOCATION_OFFSET_OTHER,


    "Purse Quest Reward - Coral 1 (Quest: Coral 2)": 1 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Ghostly! (Spectral Orb)": 2 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Ghostly! (Ghost Gem)": 3 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Ghostly! (Ghost Glove)": 4 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Hourglass 1 (Minute Hand)": 5 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Hourglass 1 (Quest: Hourglass 2)": 6 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Hourglass 2 (Hour Hand)": 7 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Magic Expedition (Charging Manastone)": 8 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Master of Whetstones (Golden Whetstone)": 9 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Windmill 1 (Verdant Energy)": 10 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Windmill 1 (Quest: Windmill 2)": 11 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Windmill 2 (Crimson Energy)": 12 + QUEST_OFFSET_PURSE,
    "Purse Quest Reward - Wizard's School (Unstable Manastone)": 13 + QUEST_OFFSET_PURSE,

    "Satchel Quest Reward - Pacifist (Pacifist's Ring)": 1 + QUEST_OFFSET_SATCHEL,
    "Satchel Quest Reward - Builder Bird (Monad's Mjolnir)": 2 + QUEST_OFFSET_SATCHEL,
    "Satchel Quest Reward - Scissors 1 (Quest: Scissors 2)": 3 + QUEST_OFFSET_SATCHEL,

    # No Tote quests give unique rewards. Sad. (Once I figure out how to make all quests give rewards, those locations will be added here)

    "Pochette Quest Reward - Fragile Tribe (Quest: Everyone Comes Home)": 1 + QUEST_OFFSET_POCHETTE,

    "CR-8 Quest Reward - Duo Core (Quest: Quad Core)": 1 + QUEST_OFFSET_CR8,
    "CR-8 Quest Reward - Quad Core (Quest: Spinning Core)": 2 + QUEST_OFFSET_CR8,

    
    "Area 2 - Recruit Satchel": 1 + DUNGEON_LOCATION_OFFSET,
    "Area 2 - Recruit Tote": 2 + DUNGEON_LOCATION_OFFSET,
    "Area 3 - Recruit Pochette": 3 + DUNGEON_LOCATION_OFFSET,

}

class BPHLocation(Location):
    game = "Backpack Hero"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BPHWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BPHWorld) -> None:
    
    haversack_hills = world.get_region("Haversack Hills")
    
    purse_quests_a1 = world.get_region("Purse Quests (Area 1)")
    satchel_quests_a1 = world.get_region("Satchel Quests (Area 1)")
    tote_quests_a1 = world.get_region("Tote Quests (Area 1)")
    pochette_quests_a1 = world.get_region("Pochette Quests (Area 1)")
    cr8_quests_a1 = world.get_region("CR-8 Quests (Area 1)")

    purse_quests_a2 = world.get_region("Purse Quests (Area 2)")
    satchel_quests_a2 = world.get_region("Satchel Quests (Area 2)")
    tote_quests_a2 = world.get_region("Tote Quests (Area 2)")
    pochette_quests_a2 = world.get_region("Pochette Quests (Area 2)")
    cr8_quests_a2 = world.get_region("CR-8 Quests (Area 2)")

    purse_quests_a3 = world.get_region("Purse Quests (Area 3)")
    satchel_quests_a3 = world.get_region("Satchel Quests (Area 3)")
    tote_quests_a3 = world.get_region("Tote Quests (Area 3)")
    pochette_quests_a3 = world.get_region("Pochette Quests (Area 3)")
    cr8_quests_a3 = world.get_region("CR-8 Quests (Area 3)")

    crypt = world.get_region("The Crypt")
    deep_caves = world.get_region("The Deep Caves")
    bramble = world.get_region("The Bramble")
    magma_core = world.get_region("The Magma Core")
    frozen_heart = world.get_region("The Frozen Heart")
    enchanted_swamp = world.get_region("The Enchanted Swamp")

    area_1 = world.get_region("Area 1")
    area_2 = world.get_region("Area 2")
    area_3 = world.get_region("Area 3")

    library = world.get_region("Library Research")
    bounty_board = world.get_region("Bounty Board Research")
    blacksmith = world.get_region("Blacksmith Research")
    tavern = world.get_region("Tavern Research")
    barracks = world.get_region("Barracks Research")
    carpenter = world.get_region("Carpenter Research")
    fletcher = world.get_region("Fletcher Research")
    mycelium = world.get_region("Magical Mycelium Research")
    jeweler = world.get_region("Jeweler Research")
    greenhouse = world.get_region("Greenhouse Research")
    schoolhouse = world.get_region("Schoolhouse Research")

    louis = world.get_region("Louis")
    mayor = world.get_region("Mayor Quillswish")
    vivienne = world.get_region("Vivienne")
    matthew = world.get_region("Matthew")
    pasha = world.get_region("Pasha")
    nora = world.get_region("Nora")
    parcel = world.get_region("Parcel")
    wartsley = world.get_region("Sir Wartsley")
    fisher = world.get_region("Fish Enthusiast")
    constance = world.get_region("Constance")
    zaar = world.get_region("Zaar")
    archer = world.get_region("Master Archer")
    burrough = world.get_region("Miss Burrough")
    doug = world.get_region("Doug")


    # This might be really slow on gen, please lmk if there's an accepted "better way" to do this (bc I really don't wanna do all this manually)
    for location in LOCATION_NAME_TO_ID:

        if location.startswith("Bounty Board"):
            bounty_board.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Blacksmith"):
            blacksmith.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Tavern"):
            tavern.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Barracks"):
            barracks.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Carpenter"):
            carpenter.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Fletcher"):
            fletcher.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Magical"):
            mycelium.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Jeweler"):
            jeweler.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Library"):
            library.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Greenhouse"):
            greenhouse.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


        if location.startswith("Matthew"):
            matthew.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Pasha"):
            pasha.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Constance"):
            constance.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Zaar"):
            zaar.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Mayor"):
            mayor.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Vivienne"):
            vivienne.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Louis"):
            louis.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Nora"):
            nora.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Sir Wartsley"):
            wartsley.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Fish Enthusiast"):
            fisher.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


            # NOTE: Below logic will not work, fix later after getting a list of all quest end points
        if location.startswith("Purse Quest"):
            purse_quests_a1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Satchel Quest"):
            satchel_quests_a1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("CR-8 Quest"):
            cr8_quests_a1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Pochette Quest"):
            pochette_quests_a1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Tote Quest"):
            tote_quests_a1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


        if location.startswith("Area 1"):
            area_1.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Area 2"):
            area_2.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Area 3"):
            area_3.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


        # These regions only have 1 location each, so I put them at the end so it wouldn't have to iterate through all of them for all the larger regions
        if location.startswith("Master Archer"):
            archer.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Miss Burrough"):
            burrough.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Parcel"):
            parcel.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Schoolhouse"):
            schoolhouse.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("Doug"):
            doug.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


        if location.startswith("The Crypt"):
            crypt.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("The Bramble"):
            bramble.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("The Deep Caves"):
            deep_caves.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("The Enchanted Swamp"):
            enchanted_swamp.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("The Magma Core"):
            magma_core.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue
        if location.startswith("The Frozen Heart"):
            frozen_heart.add_locations(get_location_names_with_ids([location]), BPHLocation)
            continue


    
def create_events(world: BPHWorld) -> None:
    
    purse_quests_a1 = world.get_region("Purse Quests (Area 1)")
    satchel_quests_a1 = world.get_region("Satchel Quests (Area 1)")
    tote_quests_a1 = world.get_region("Tote Quests (Area 1)")
    pochette_quests_a1 = world.get_region("Pochette Quests (Area 1)")
    cr8_quests_a1 = world.get_region("CR-8 Quests (Area 1)")

    purse_quests_a2 = world.get_region("Purse Quests (Area 2)")
    satchel_quests_a2 = world.get_region("Satchel Quests (Area 2)")
    tote_quests_a2 = world.get_region("Tote Quests (Area 2)")
    pochette_quests_a2 = world.get_region("Pochette Quests (Area 2)")
    cr8_quests_a2 = world.get_region("CR-8 Quests (Area 2)")

    purse_quests_a3 = world.get_region("Purse Quests (Area 3)")
    satchel_quests_a3 = world.get_region("Satchel Quests (Area 3)")
    tote_quests_a3 = world.get_region("Tote Quests (Area 3)")
    pochette_quests_a3 = world.get_region("Pochette Quests (Area 3)")
    cr8_quests_a3 = world.get_region("CR-8 Quests (Area 3)")

    purse_quests_a3.add_event(
        "Clear Area 3 with Purse", "Area 3 Clear", location_type=BPHLocation, item_type=items.BPHItem
    )
    satchel_quests_a3.add_event(
        "Clear Area 3 with Satchel", "Area 3 Clear", location_type=BPHLocation, item_type=items.BPHItem
    )
    tote_quests_a3.add_event(
        "Clear Area 3 with Tote", "Area 3 Clear", location_type=BPHLocation, item_type=items.BPHItem
    )
    pochette_quests_a3.add_event(
        "Clear Area 3 with Pochette", "Area 3 Clear", location_type=BPHLocation, item_type=items.BPHItem
    )
    cr8_quests_a3.add_event(
        "Clear Area 3 with CR-8", "Area 3 Clear", location_type=BPHLocation, item_type=items.BPHItem
    )

    # Checking for which quests can be completed at any given time

    purse_quests_a1.add_event("(Event) Quest Complete: Archery Lessons", rule=Has("Quest: Archery Lessons"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Coral 1", rule=Has("Progressive Quest: Coral", 1), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Coral 2", rule=Has("Progressive Quest: Coral", 2), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Hourglass 1", rule=Has("Progressive Quest: Hourglass", 1), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Hourglass 2", rule=Has("Progressive Quest: Hourglass", 2), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Windmill 1", rule=Has("Progressive Quest: Windmill", 1), location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Windmill 2", rule=Has("Progressive Quest: Windmill", 2), location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Cramped", rule=Has("Quest: Cramped"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Energy Delivery", rule=Has("Quest: Energy Delivery"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Fishy Business", rule=Has("Quest: Fishy Business"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Ghostly!", rule=Has("Quest: Ghostly!"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Magic Expedition", rule=Has("Quest: Magic Expedition"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Meditation", rule=Has("Quest: Meditation"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Protector", rule=Has("Quest: Protector"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Red Cotton", rule=Has("Quest: Red Cotton"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Red Root", rule=Has("Quest: Red Root"), location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Ice Cream (Purse)", rule=Has("Quest: Ice Cream (Purse)"), location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Red Tusk", rule=Has("Quest: Red Tusk"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Master of Whetstones", rule=Has("Quest: Master of Whetstones"), location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a1.add_event("(Event) Quest Complete: Wizard's School", rule=Has("Quest: Wizard's School"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a3.add_event("(Event) Quest Complete: Campaign Trail", rule=Has("Quest: Campaign Trail"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: Red Flame", rule=Has("Quest: Red Flame"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    purse_quests_a2.add_event("(Event) Quest Complete: This One's On Me", rule=Has("Quest: This One's On Me"), location_type=BPHLocation, item_type=items.BPHItem)
    
    satchel_quests_a3.add_event("(Event) Quest Complete: Builder Bird", rule=Has("Quest: Builder Bird"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem) # No end point is given in the menu, not sure if this actually ends at area 3 or if it just ends earlier if you don't have area 3 access
    satchel_quests_a2.add_event("(Event) Quest Complete: Scissors 1", rule=Has("Progressive Quest: Scissors", 1), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    satchel_quests_a3.add_event("(Event) Quest Complete: Scissors 2", rule=Has("Progressive Quest: Scissors", 2), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    satchel_quests_a3.add_event("(Event) Quest Complete: Easy Mode (Satchel)", rule=Has("Quest: Easy Mode (Satchel)"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    satchel_quests_a2.add_event("(Event) Quest Complete: Pacifist", rule=Has("Quest: Pacifist"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    satchel_quests_a2.add_event("(Event) Quest Complete: Ice Cream (Satchel)", rule=Has("Quest: Ice Cream (Satchel)"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)

    tote_quests_a3.add_event("(Event) Quest Complete: Easy Mode (Tote)", rule=Has("Quest: Easy Mode (Tote)"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    tote_quests_a3.add_event("(Event) Quest Complete: Magic Archery", rule=Has("Quest: Magic Archery"), location_type=BPHLocation, item_type=items.BPHItem)
    tote_quests_a3.add_event("(Event) Quest Complete: Mushroom Friend", rule=Has("Quest: Mushroom Friend"), location_type=BPHLocation, item_type=items.BPHItem)
    tote_quests_a3.add_event("(Event) Quest Complete: Sap Primer", rule=Has("Quest: Sap Primer"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    tote_quests_a3.add_event("(Event) Quest Complete: Throw the Book at Them", rule=Has("Quest: Throw the Book at Them"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)

    pochette_quests_a3.add_event("(Event) Quest Complete: Easy Mode (Pochette)", rule=Has("Quest: Easy Mode (Pochette)"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    pochette_quests_a3.add_event("(Event) Quest Complete: Effigies", rule=Has("Quest: Effigies"), location_type=BPHLocation, item_type=items.BPHItem)
    pochette_quests_a3.add_event("(Event) Quest Complete: Fragile Tribe", rule=Has("Quest: Fragile Tribe"), location_type=BPHLocation, item_type=items.BPHItem)
    pochette_quests_a3.add_event("(Event) Quest Complete: Reaper", rule=Has("Quest: Reaper"), location_type=BPHLocation, item_type=items.BPHItem)
    pochette_quests_a3.add_event("(Event) Quest Complete: Treats Only", rule=Has("Quest: Treats Only"), location_type=BPHLocation, item_type=items.BPHItem)

    cr8_quests_a3.add_event("(Event) Quest Complete: Easy Mode (CR-8)", rule=Has("Quest: Easy Mode (CR-8)"), item_name="Lost Spark", location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Bumpy Ride", rule=Has("Quest: Bumpy Ride"), location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Magnetized", rule=Has("Quest: Magnetized"), location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Micro Build", rule=Has("Quest: Micro Build"), location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Duo Core", rule=Has("Quest: Duo Core"), location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Quad Core", rule=Has("Quest: Quad Core"), location_type=BPHLocation, item_type=items.BPHItem)
    cr8_quests_a3.add_event("(Event) Quest Complete: Spinning Core", rule=Has("Quest: Spinning Core"), location_type=BPHLocation, item_type=items.BPHItem)