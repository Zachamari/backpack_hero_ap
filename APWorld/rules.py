from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter

from rule_builder.rules import Has, HasAll, HasAny, HasGroup, Rule, CanReachRegion, HasAnyCount, AtLeast, CanReachLocation

if TYPE_CHECKING:
    from .world import BPHWorld


def set_all_rules(world: BPHWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: BPHWorld) -> None:

    library_built = world.get_entrance("Build the Library")
    bounty_built = world.get_entrance("Build the Bounty Board")
    blacksmith_built = world.get_entrance("Build the Blacksmith")
    tavern_built = world.get_entrance("Build the Tavern")
    barracks_built = world.get_entrance("Build the Barracks")
    carpenter_built = world.get_entrance("Build the Carpenter")
    fletcher_built = world.get_entrance("Build the Fletcher")
    mycelium_built = world.get_entrance("Build the Magical Mycelium")
    jeweler_built = world.get_entrance("Build the Jeweler")
    greenhouse_built = world.get_entrance("Build the Greenhouse")
    schoolhouse_built = world.get_entrance("Build the Schoolhouse")

    world.set_rule(library_built, Has("Library"))
    world.set_rule(bounty_built, Has("Bounty Board"))
    world.set_rule(blacksmith_built, Has("Blacksmith"))
    world.set_rule(tavern_built, Has("Tavern"))
    world.set_rule(barracks_built, Has("Barracks"))
    world.set_rule(carpenter_built, Has("Carpenter"))
    world.set_rule(fletcher_built, Has("Fletcher"))
    world.set_rule(mycelium_built, Has("Magical Mycelium"))
    world.set_rule(jeweler_built, Has("Jeweler"))
    world.set_rule(greenhouse_built, Has("Greenhouse"))
    world.set_rule(schoolhouse_built, Has("Schoolhouse"))


    enter_bramble = world.get_entrance("Enter the Bramble")
    enter_caves = world.get_entrance("Enter the Deep Caves")
    enter_swamp = world.get_entrance("Enter the Enchanted Swamp")
    enter_magma = world.get_entrance("Enter the Magma Core")
    enter_frozen = world.get_entrance("Enter the Frozen Heart")

    world.set_rule(enter_bramble, Has("Key to the Bramble"))
    world.set_rule(enter_caves, Has("Key to the Deep Caves"))
    world.set_rule(enter_swamp, Has("Key to the Enchanted Swamp"))
    world.set_rule(enter_magma, Has("Key to the Magma Core"))
    world.set_rule(enter_frozen, Has("Key to the Frozen Heart"))


    satchel_quests_a1 = world.get_entrance("Finish an Area 1 Quest (Satchel)")
    tote_quests_a1 = world.get_entrance("Finish an Area 1 Quest (Tote)")
    pochette_quests_a1 = world.get_entrance("Finish an Area 1 Quest (Pochette)")
    cr8_quests_a1 = world.get_entrance("Finish an Area 1 Quest (CR-8)")

    satchel_quests_a2 = world.get_entrance("Finish an Area 2 Quest (Satchel)")
    tote_quests_a2 = world.get_entrance("Finish an Area 2 Quest (Tote)")
    pochette_quests_a2 = world.get_entrance("Finish an Area 2 Quest (Pochette)")
    cr8_quests_a2 = world.get_entrance("Finish an Area 2 Quest (CR-8)")

    satchel_quests_a3 = world.get_entrance("Finish an Area 3 Quest (Satchel)")
    tote_quests_a3 = world.get_entrance("Finish an Area 3 Quest (Tote)")
    pochette_quests_a3 = world.get_entrance("Finish an Area 3 Quest (Pochette)")
    cr8_quests_a3 = world.get_entrance("Finish an Area 3 Quest (CR-8)")

    world.set_rule(satchel_quests_a1, Has("Satchel"))
    world.set_rule(tote_quests_a1, Has("Tote"))
    world.set_rule(pochette_quests_a1, Has("Pochette"))
    world.set_rule(cr8_quests_a1, Has("CR-8"))

    world.set_rule(satchel_quests_a2, Has("Satchel"))
    world.set_rule(tote_quests_a2, Has("Tote"))
    world.set_rule(pochette_quests_a2, Has("Pochette"))
    world.set_rule(cr8_quests_a2, Has("CR-8"))

    world.set_rule(satchel_quests_a3, Has("Satchel"))
    world.set_rule(tote_quests_a3, Has("Tote"))
    world.set_rule(pochette_quests_a3, Has("Pochette"))
    world.set_rule(cr8_quests_a3, Has("CR-8"))


def set_all_location_rules(world: BPHWorld) -> None:

    world.set_rule(world.get_location("Bounty Board Research - Quest: Ice Cream (Satchel)"), Has("Satchel"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Pacifist"), Has("Satchel"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Micro Build"), Has("CR-8"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Magnetized"), Has("CR-8"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Fragile Tribe"), Has("Pochette"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Effigies"), Has("Pochette"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Easy Mode (Satchel)"), Has("Satchel"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Easy Mode (Tote)"), Has("Tote"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Easy Mode (Pochette)"), Has("Pochette"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Easy Mode (CR-8)"), Has("CR-8"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Scissors 1"), Has("Satchel"))
    world.set_rule(world.get_location("Bounty Board Research - Quest: Duo Core"), Has("CR-8"))

    world.set_rule(world.get_location("Blacksmith Research - Plate Armor"), Has("Chainmail"))
    world.set_rule(world.get_location("Blacksmith Research - Hercule Pavise"), HasAll("Li'l Buckler", "Wild Buckler", "Amethyst Buckler", "Tote"))
    world.set_rule(world.get_location("Blacksmith Research - Tattered Collar"), Has("Glove of Knives"))
    world.set_rule(world.get_location("Blacksmith Research - Swamp Buckler"), Has("Li'l Buckler"))
    world.set_rule(world.get_location("Blacksmith Research - Knight's Armor"), Has("Knight's Shield"))
    world.set_rule(world.get_location("Blacksmith Research - King's Shield"), Has("Knight's Shield"))
    world.set_rule(world.get_location("Blacksmith Research - Greaves"), Has("Chainmail"))
    # world.set_rule(world.get_location("Blacksmith Research - Feather Cap"), Has("Leather Cap")) # I think Leather Cap is unlocked by default
    world.set_rule(world.get_location("Blacksmith Research - Amethyst Buckler"), HasAll("Li'l Buckler", "Amethyst"))

    world.set_rule(world.get_location("Tavern Research - Quest: Treats Only"), Has("Pochette"))
    # world.set_rule(world.get_location("Tavern Research - Dodge Potion"), Has("Debuff Potion")) # Not sure if Debuff Potion is unlocked by default
    
    world.set_rule(world.get_location("Barracks Research - Ace Cleaver"), HasAll("Jack Cleaver", "King Cleaver", "Queen Cleaver"))
    world.set_rule(world.get_location("Barracks Research - Quest: Warrior Bird"), Has("Satchel"))
    world.set_rule(world.get_location("Barracks Research - Alpha Star"), HasAll("Column Chain Star", "Row Chain Star"))
    world.set_rule(world.get_location("Barracks Research - Crow Hammer"), Has("Satchel"))
    world.set_rule(world.get_location("Barracks Research - Wooden Knife"), Has("Wooden Blade"))
    world.set_rule(world.get_location("Barracks Research - Vorpal Blade"), Has("Smoke Dagger"))
    # world.set_rule(world.get_location("Barracks Research - Lizard King Sword"), Has("Lizard Blade")) # not sure about this one
    world.set_rule(world.get_location("Barracks Research - Quest: Reaper"), Has("Pochette"))
    world.set_rule(world.get_location("Barracks Research - Assassin's Dagger"), Has("Dagger"))
    world.set_rule(world.get_location("Barracks Research - Copy Star"), Has("Stacking Star"))
    world.set_rule(world.get_location("Barracks Research - Claw Hammer"), Has("Satchel"))
    world.set_rule(world.get_location("Barracks Research - Brutal Spear"), Has("Hatchet"))
    world.set_rule(world.get_location("Barracks Research - Hatchet"), Has("Spiky Club"))
    
    world.set_rule(world.get_location("Carpenter Research - Quest: Builder Bird"), Has("Satchel"))
    
    world.set_rule(world.get_location("Fletcher Research - Quest: Archery Mastery"), Has("Lost Spark", count=17))
    world.set_rule(world.get_location("Fletcher Research - Electric Arrow"), Has("Electric Stone"))
    world.set_rule(world.get_location("Fletcher Research - Manastone Bow"), HasAll("Fire Arrow", "Poison Arrow"))
    world.set_rule(world.get_location("Fletcher Research - Quest: Magic Archery"), Has("Tote"))
    
    world.set_rule(world.get_location("Magical Mycelium Research - Quest: Magic Expedition"), Has("Lost Spark", count=17) & Has("Tote"))
    world.set_rule(world.get_location("Magical Mycelium Research - Quest: Mushroom Friend"), Has("Tote"))
    world.set_rule(world.get_location("Magical Mycelium Research - Quest: Sap Primer"), Has("Tote"))
    world.set_rule(world.get_location("Magical Mycelium Research - Metallic Wand"), Has("Skull Wand"))
    world.set_rule(world.get_location("Magical Mycelium Research - Energy Wand"), CanReachRegion("Area 2")) # This is a Legendary-rarity item, so I logically require access to area 2 to prevent early horrible grinding

    world.set_rule(world.get_location("Jeweler Research - Velvet Bag"), HasAll("Bag of Shurikens", "Magic Star Bag", "Shuriken Forge"))
    world.set_rule(world.get_location("Jeweler Research - Quest: Bumpy Ride"), Has("CR-8"))
    world.set_rule(world.get_location("Jeweler Research - Ring of Doom"), Has("Ring of Rage"))
    world.set_rule(world.get_location("Jeweler Research - Berserker's Ring"), Has("Spiky Club"))
    
    world.set_rule(world.get_location("Library Research - Quest: Throw the Book at Them"), Has("Tote"))
    world.set_rule(world.get_location("Library Research - Cleansing Flame"), CanReachLocation("(Event) Quest Complete: Red Flame"))
    world.set_rule(world.get_location("Library Research - Fluffy Cotton"), CanReachLocation("(Event) Quest Complete: Red Cotton"))
    world.set_rule(world.get_location("Library Research - Ice Cream"), CanReachLocation("(Event) Quest Complete: Ice Cream (Purse)") | CanReachLocation("(Event) Quest Complete: Ice Cream (Satchel)"))
    world.set_rule(world.get_location("Library Research - Reverse Hourglass"), CanReachLocation("(Event) Quest Complete: Hourglass 1"))
    world.set_rule(world.get_location("Library Research - Spicy Ginger"), CanReachLocation("(Event) Quest Complete: Red Root"))
    world.set_rule(world.get_location("Library Research - Tusk"), CanReachLocation("(Event) Quest Complete: Red Tusk"))

    world.set_rule(world.get_location("Matthew Research - Key to the Deep Caves"), Has("Lost Spark", count=17))
    world.set_rule(world.get_location("Matthew Research - Key to the Bramble"), Has("Lost Spark", count=17))
    world.set_rule(world.get_location("Matthew Research - Key to the Magma Core"), Has("Lost Spark", count=17))
    world.set_rule(world.get_location("Matthew Research - Key to the Frozen Heart"), Has("Lost Spark", count=17))
    world.set_rule(world.get_location("Matthew Research - Key to the Enchanted Swamp"), Has("Lost Spark", count=17))
    
    world.set_rule(world.get_location("Pasha Research - Brick Path"), CanReachRegion("Area 2")) # Brickwall sucks to get early (Uncommon item that takes up 2 spaces and isn't at all useful unless you're going for a very specific build), so I'm logically putting this behind reaching Area 2 so you don't have to grind for this at the start of every run

    world.set_rule(world.get_location("Mayor Quillswish Research - Tavern"), Has("House"))
    world.set_rule(world.get_location("Mayor Quillswish Research - Barracks"), Has("House"))
    world.set_rule(world.get_location("Mayor Quillswish Research - Blacksmith"), Has("House"))
    
    world.set_rule(world.get_location("Louis - Large Town Gift (Purse's House)"), Has("House")) # possibly more required

    # world.set_rule(world.get_location("Nora - Built Magical Mycelium Reward (Tote's Totem)"), Has("Magical Mycelium"))

    world.set_rule(world.get_location("Mayor Quillswish - Expanding Town Reward 1 (Town Hall)"), HasAll("House", "Tavern", "Barracks", "Blacksmith"))
    world.set_rule(world.get_location("Mayor Quillswish - Expanding Town Reward 2 (Dirt Path)"), HasAll("House", "Tavern", "Barracks", "Blacksmith"))
    world.set_rule(world.get_location("Mayor Quillswish - Mayor Quillswish Plush Reward (Quest: Campaign Trail)"), HasAll("House", "Tavern", "Barracks", "Blacksmith"))

    # Logically locking some of these behind Area 2 to prevent early required grinding
    world.set_rule(world.get_location("Vivienne - 3 Etchings/Sigils Reward (Purse Costume)"), CanReachRegion("Area 2")) # Maybe add some number of Purse Quests as well
    world.set_rule(world.get_location("Vivienne - 4 Etchings/Sigils Reward (Purse Costume)"), CanReachRegion("Area 3")) # Maybe add some number of Purse Quests as well
    world.set_rule(world.get_location("Vivienne - 5 Etchings/Sigils Reward (Purse Costume)"), CanReachRegion("Area 3")) # Maybe add some number of Purse Quests as well

    world.set_rule(world.get_location("Vivienne - First Hymn Reward (Satchel Costume)"), Has("Satchel") & CanReachRegion("Area 2"))
    world.set_rule(world.get_location("Vivienne - Second Hymn Reward (Satchel Costume)"), Has("Satchel") & CanReachRegion("Area 3"))

    world.set_rule(world.get_location("Vivienne - First Rune Reward (Tote Costume)"), Has("Tote") & CanReachRegion("Area 2"))
    world.set_rule(world.get_location("Vivienne - Second Rune Reward (Tote Costume)"), Has("Tote") & CanReachRegion("Area 3"))
    
    world.set_rule(world.get_location("Vivienne - First ??? Reward (Pochette Costume)"), Has("Pochette") & CanReachRegion("Area 2"))
    world.set_rule(world.get_location("Vivienne - Second ??? Reward (Pochette Costume)"), Has("Pochette") & CanReachRegion("Area 3"))
    
    world.set_rule(world.get_location("Vivienne - First Floppy Disk Reward (CR-8 Costume)"), Has("CR-8") & CanReachRegion("Area 2"))
    world.set_rule(world.get_location("Vivienne - Second Floppy Disk Reward (CR-8 Costume)"), Has("CR-8") & CanReachRegion("Area 3"))

    world.set_rule(world.get_location("Purse Quest Reward - Coral 1 (Quest: Coral 2)"), CanReachLocation("(Event) Quest Complete: Coral 1")) 
    world.set_rule(world.get_location("Purse Quest Reward - Ghostly! (Spectral Orb)"), CanReachLocation("(Event) Quest Complete: Ghostly!")) 
    world.set_rule(world.get_location("Purse Quest Reward - Ghostly! (Ghost Gem)"), CanReachLocation("(Event) Quest Complete: Ghostly!")) 
    world.set_rule(world.get_location("Purse Quest Reward - Ghostly! (Ghost Glove)"), CanReachLocation("(Event) Quest Complete: Ghostly!")) 
    world.set_rule(world.get_location("Purse Quest Reward - Hourglass 1 (Quest: Hourglass 2)"), CanReachLocation("(Event) Quest Complete: Hourglass 1"))
    world.set_rule(world.get_location("Purse Quest Reward - Hourglass 1 (Minute Hand)"), CanReachLocation("(Event) Quest Complete: Hourglass 1"))
    world.set_rule(world.get_location("Purse Quest Reward - Hourglass 2 (Hour Hand)"), CanReachLocation("(Event) Quest Complete: Hourglass 2")) 
    world.set_rule(world.get_location("Purse Quest Reward - Magic Expedition (Charging Manastone)"), CanReachLocation("(Event) Quest Complete: Magic Expedition"))
    world.set_rule(world.get_location("Purse Quest Reward - Master of Whetstones (Golden Whetstone)"), CanReachLocation("(Event) Quest Complete: Master of Whetstones"))
    world.set_rule(world.get_location("Purse Quest Reward - Windmill 1 (Verdant Energy)"), CanReachLocation("(Event) Quest Complete: Windmill 1"))
    world.set_rule(world.get_location("Purse Quest Reward - Windmill 1 (Quest: Windmill 2)"), CanReachLocation("(Event) Quest Complete: Windmill 1")) 
    world.set_rule(world.get_location("Purse Quest Reward - Windmill 2 (Crimson Energy)"), CanReachLocation("(Event) Quest Complete: Windmill 2"))
    world.set_rule(world.get_location("Purse Quest Reward - Wizard's School (Unstable Manastone)"), CanReachLocation("(Event) Quest Complete: Wizard's School"))
    
    world.set_rule(world.get_location("Satchel Quest Reward - Pacifist (Pacifist's Ring)"), CanReachLocation("(Event) Quest Complete: Pacifist"))
    world.set_rule(world.get_location("Satchel Quest Reward - Builder Bird (Monad's Mjolnir)"), CanReachLocation("(Event) Quest Complete: Builder Bird"))
    world.set_rule(world.get_location("Satchel Quest Reward - Scissors 1 (Quest: Scissors 2)"), CanReachLocation("(Event) Quest Complete: Scissors 1"))
    
    world.set_rule(world.get_location("Pochette Quest Reward - Fragile Tribe (Quest: Everyone Comes Home)"), CanReachLocation("(Event) Quest Complete: Fragile Tribe"))
    
    world.set_rule(world.get_location("CR-8 Quest Reward - Duo Core (Quest: Quad Core)"), CanReachLocation("(Event) Quest Complete: Duo Core"))
    world.set_rule(world.get_location("CR-8 Quest Reward - Quad Core (Quest: Spinning Core)"), CanReachLocation("(Event) Quest Complete: Quad Core"))



def set_completion_condition(world: BPHWorld) -> None:
    world.set_completion_rule(Has("Area 3 Clear", count=5) & Has("Beacon"))