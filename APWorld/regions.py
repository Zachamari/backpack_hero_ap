from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region


if TYPE_CHECKING:
    from .world import BPHWorld


def create_and_connect_regions(world: BPHWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BPHWorld) -> None:
    # Generic region to help connect everything more easily
    haversack_hills = Region("Haversack Hills", world.player, world.multiworld)


    purse_quests_a1 = Region("Purse Quests (Area 1)", world.player, world.multiworld)
    satchel_quests_a1 = Region("Satchel Quests (Area 1)", world.player, world.multiworld)
    tote_quests_a1 = Region("Tote Quests (Area 1)", world.player, world.multiworld)
    pochette_quests_a1 = Region("Pochette Quests (Area 1)", world.player, world.multiworld)
    cr8_quests_a1 = Region("CR-8 Quests (Area 1)", world.player, world.multiworld)

    purse_quests_a2 = Region("Purse Quests (Area 2)", world.player, world.multiworld)
    satchel_quests_a2 = Region("Satchel Quests (Area 2)", world.player, world.multiworld)
    tote_quests_a2 = Region("Tote Quests (Area 2)", world.player, world.multiworld)
    pochette_quests_a2 = Region("Pochette Quests (Area 2)", world.player, world.multiworld)
    cr8_quests_a2 = Region("CR-8 Quests (Area 2)", world.player, world.multiworld)

    purse_quests_a3 = Region("Purse Quests (Area 3)", world.player, world.multiworld)
    satchel_quests_a3 = Region("Satchel Quests (Area 3)", world.player, world.multiworld)
    tote_quests_a3 = Region("Tote Quests (Area 3)", world.player, world.multiworld)
    pochette_quests_a3 = Region("Pochette Quests (Area 3)", world.player, world.multiworld)
    cr8_quests_a3 = Region("CR-8 Quests (Area 3)", world.player, world.multiworld)

    quest_regions = [purse_quests_a1, satchel_quests_a1, tote_quests_a1, pochette_quests_a1, cr8_quests_a1, purse_quests_a2, satchel_quests_a2, tote_quests_a2, pochette_quests_a2, cr8_quests_a2, purse_quests_a3, satchel_quests_a3, tote_quests_a3, pochette_quests_a3, cr8_quests_a3]


    crypt = Region("The Crypt", world.player, world.multiworld)
    deep_caves = Region("The Deep Caves", world.player, world.multiworld)
    bramble = Region("The Bramble", world.player, world.multiworld)
    magma_core = Region("The Magma Core", world.player, world.multiworld)
    frozen_heart = Region("The Frozen Heart", world.player, world.multiworld)
    enchanted_swamp = Region("The Enchanted Swamp", world.player, world.multiworld)

    area_1 = Region("Area 1", world.player, world.multiworld) # unnecessary, but I'm making it for consistency's sake
    area_2 = Region("Area 2", world.player, world.multiworld)
    area_3 = Region("Area 3", world.player, world.multiworld)

    dungeon_regions = [crypt, deep_caves, bramble, magma_core, frozen_heart, enchanted_swamp, area_1, area_2, area_3]


    library = Region("Library Research", world.player, world.multiworld)
    bounty_board = Region("Bounty Board Research", world.player, world.multiworld)
    blacksmith = Region("Blacksmith Research", world.player, world.multiworld)
    tavern = Region("Tavern Research", world.player, world.multiworld)
    barracks = Region("Barracks Research", world.player, world.multiworld)
    carpenter = Region("Carpenter Research", world.player, world.multiworld)
    fletcher = Region("Fletcher Research", world.player, world.multiworld)
    mycelium = Region("Magical Mycelium Research", world.player, world.multiworld)
    jeweler = Region("Jeweler Research", world.player, world.multiworld)
    greenhouse = Region("Greenhouse Research", world.player, world.multiworld)
    schoolhouse = Region("Schoolhouse Research", world.player, world.multiworld)

    research_regions = [library, bounty_board, blacksmith, tavern, barracks, carpenter, fletcher, mycelium, jeweler, greenhouse, schoolhouse]


    louis = Region("Louis", world.player, world.multiworld)
    mayor = Region("Mayor Quillswish", world.player, world.multiworld)
    vivienne = Region("Vivienne", world.player, world.multiworld)
    matthew = Region("Matthew", world.player, world.multiworld)
    pasha = Region("Pasha", world.player, world.multiworld)
    nora = Region("Nora", world.player, world.multiworld)
    parcel = Region("Parcel", world.player, world.multiworld)
    wartsley = Region("Sir Wartsley", world.player, world.multiworld)
    fisher = Region("Fish Enthusiast", world.player, world.multiworld)
    constance = Region("Constance", world.player, world.multiworld)
    zaar = Region("Zaar", world.player, world.multiworld)
    archer = Region("Master Archer", world.player, world.multiworld)
    burrough = Region("Miss Burrough", world.player, world.multiworld)
    doug = Region("Doug", world.player, world.multiworld)

    npc_regions = [louis, mayor, vivienne, matthew, pasha, nora, parcel, wartsley, fisher, constance, zaar, archer, burrough, doug]


    # Note to self: whenever I add the option to not shuffle quest rewards, make the quest regions only be added to the list if that option is off

    regions = [haversack_hills]
    regions += quest_regions
    regions += dungeon_regions
    regions += research_regions
    regions += npc_regions
      
    world.multiworld.regions += regions



def connect_regions(world: BPHWorld) -> None:

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



    haversack_hills.connect(louis, "Talk to Louis")
    haversack_hills.connect(mayor, "Talk to Mayor Quillswish")
    haversack_hills.connect(vivienne, "Talk to Vivienne")
    haversack_hills.connect(matthew, "Talk to Matthew")
    haversack_hills.connect(pasha, "Talk to Pasha")
    haversack_hills.connect(nora, "Talk to Nora")
    haversack_hills.connect(parcel, "Talk to Parcel")
    haversack_hills.connect(wartsley, "Talk to Sir Wartsley")
    haversack_hills.connect(fisher, "Talk to Fish Enthusiast")
    haversack_hills.connect(constance, "Talk to Constance")
    haversack_hills.connect(zaar, "Talk to Zaar")
    haversack_hills.connect(archer, "Talk to Master Archer")
    haversack_hills.connect(burrough, "Talk to Miss Burrough")
    haversack_hills.connect(doug, "Talk to Doug")

    haversack_hills.connect(library, "Build the Library")
    haversack_hills.connect(bounty_board, "Build the Bounty Board")
    haversack_hills.connect(blacksmith, "Build the Blacksmith")
    haversack_hills.connect(tavern, "Build the Tavern")
    haversack_hills.connect(barracks, "Build the Barracks")
    haversack_hills.connect(carpenter, "Build the Carpenter")
    haversack_hills.connect(fletcher, "Build the Fletcher")
    haversack_hills.connect(mycelium, "Build the Magical Mycelium")
    haversack_hills.connect(jeweler, "Build the Jeweler")
    haversack_hills.connect(greenhouse, "Build the Greenhouse")
    haversack_hills.connect(schoolhouse, "Build the Schoolhouse")

    area_1.connect(purse_quests_a1, "Finish an Area 1 Quest (Purse)")
    area_1.connect(satchel_quests_a1, "Finish an Area 1 Quest (Satchel)")
    area_1.connect(tote_quests_a1, "Finish an Area 1 Quest (Tote)")
    area_1.connect(pochette_quests_a1, "Finish an Area 1 Quest (Pochette)")
    area_1.connect(cr8_quests_a1, "Finish an Area 1 Quest (CR-8)")

    area_2.connect(purse_quests_a2, "Finish an Area 2 Quest (Purse)")
    area_2.connect(satchel_quests_a2, "Finish an Area 2 Quest (Satchel)")
    area_2.connect(tote_quests_a2, "Finish an Area 2 Quest (Tote)")
    area_2.connect(pochette_quests_a2, "Finish an Area 2 Quest (Pochette)")
    area_2.connect(cr8_quests_a2, "Finish an Area 2 Quest (CR-8)")

    area_3.connect(purse_quests_a3, "Finish an Area 3 Quest (Purse)")
    area_3.connect(satchel_quests_a3, "Finish an Area 3 Quest (Satchel)")
    area_3.connect(tote_quests_a3, "Finish an Area 3 Quest (Tote)")
    area_3.connect(pochette_quests_a3, "Finish an Area 3 Quest (Pochette)")
    area_3.connect(cr8_quests_a3, "Finish an Area 3 Quest (CR-8)")

    haversack_hills.connect(crypt, "Enter the Crypt")
    haversack_hills.connect(bramble, "Enter the Bramble")
    crypt.connect(area_1, "Clear the Crypt")
    bramble.connect(area_1, "Clear the Bramble")

    area_1.connect(deep_caves, "Enter the Deep Caves")
    area_1.connect(enchanted_swamp, "Enter the Enchanted Swamp")
    deep_caves.connect(area_2, "Clear the Deep Caves")
    enchanted_swamp.connect(area_2, "Clear the Enchanted Swamp")
    
    area_2.connect(magma_core, "Enter the Magma Core")
    area_2.connect(frozen_heart, "Enter the Frozen Heart")
    magma_core.connect(area_3, "Clear the Magma Core")
    frozen_heart.connect(area_3, "Clear the Frozen Heart")
