from game.location import Location

shared_interactions = {
    "move": "You can move to a new area.",
    "back": "Back to main menu."
}

shared_village_interactions ={
    "rest": "You can rest to restore your health.",
    "shop": "You can visit the shop to buy and sell items.",
    "talk": "You can talk to the villagers."
}

# Create some locations
@classmethod
def create_location(cls, village_name):
    return cls(
        name=village_name,
        description="A new village: {village_name}",
        interactions={
            **shared_interactions,
            "rest": "You can rest to restore your health.",
        }
    )


# Create some locations
village = Location(
    name="Village",
    description="A peaceful village with bustling activity.",
    interactions={
        **shared_interactions,
        **shared_village_interactions,
    }
    #items=[Item("Potion", "Restores a small amount of health.")]
)

forest = Location(
    name="Forest",
    description="A dense forest with towering trees.",
    interactions={
        **shared_interactions,
        "search": "You search the area for useful items."},
    #items=[Item("Herb", "A medicinal herb with healing properties.")]
)

cave = Location(
    name="Cave",
    description="A dark and eerie cave entrance.",
    interactions={
        **shared_interactions,
        "enter": "You cautiously enter the cave."},
    #items=[Item("Torch", "Provides light in dark places.")]
)