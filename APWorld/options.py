from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class QuestRewards(Choice):
    """
    Whether rewards from side quests should be shuffled into the pool.
    Vanilla: Quests are shuffled into the pool, but will give their vanilla rewards. (NOT IMPLEMENTED YET)
    Skipped: Quests will be completely removed from the item pool. Items normally unlocked from quests (including Lost Sparks) will be shuffled into the item pool instead. (NOT IMPLEMENTED YET)
    Unlocks: Quests that normally give item or quest unlocks will instead give an item from the multiworld, and their respective unlocks will be shuffled into the multiworld.
    Unlocks_and_Sparks: In addition to item and quest unlocks, Lost Sparks from quests will also be shuffled into the item pool, and quests that normally give Lost Sparks will instead give multiworld items. (NOT IMPLEMENTED YET)
    Everything: Item unlocks, Lost Sparks, and loot received as quest rewards will all be shuffled into the pool.
    """

    display_name = "Shuffle Quest Rewards"

    option_vanilla = 0
    option_skipped = 1
    option_unlocks = 2
    option_unlocks_and_sparks = 3
    option_everything = 4

class ShuffleCostumes(Toggle):
    """
    Whether alternate costumes will be shuffled into the pool.
    Alternate costumes are normally unlocked by bringing special items back to Haversack Hill and showing them to Vivienne.
    When enabled, this option adds 18 locations and 18 filler items.
    """
    #TODO: shuffle the etchings and such into the pool as well (after adding more locations)
    display_name = "Shuffle Alternate Costumes"



@dataclass
class BPHOptions(PerGameCommonOptions):
    quest_rewards: QuestRewards
    shuffle_costumes: ShuffleCostumes


option_groups = [
    OptionGroup(
        "Randomization Options",
        [QuestRewards, ShuffleCostumes],
    )
]