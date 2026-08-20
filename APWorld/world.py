from collections.abc import Mapping

from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world

from . import options as bph_options

# Shoutouts to APQuest 

class BPHWorld(World):
    """
    Backpack Hero is an inventory management roguelike created by TheJaspel. 
    You can only become as powerful as whatever you can cram into your backpack!
    """

    game = "Backpack Hero"

    web = web_world.BPHWebWorld()

    options_dataclass = bph_options.BPHOptions
    options: bph_options.BPHOptions # type: ignore

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.get_item_name_to_id()

    # location_name_groups = locations.get_location_groups()
    item_name_groups = items.get_item_groups()

    origin_region_name = "Haversack Hills"

    ut_can_gen_without_yaml = False # change once this is added
    glitches_item_name = "Possible OOL"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BPHItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "quest_rewards", "shuffle_costumes"
        )