from game.location import Location

# Create some locations
village = Location(
    name="Village",
    description="A peaceful village with bustling activity.",
    interactions={"move": "You can move to the forest or the cave.",
                  "rest": "You can rest to restore your health.",
                  "shop": "You can visit the shop to buy and sell items.",
                  "talk": "You can talk to the villagers.",
                  "back": "Back to main menu." },
    #items=[Item("Potion", "Restores a small amount of health.")]
)

forest = Location(
    name="Forest",
    description="A dense forest with towering trees.",
    interactions={"search": "You search the area for useful items."},
    #items=[Item("Herb", "A medicinal herb with healing properties.")]
)

cave = Location(
    name="Cave",
    description="A dark and eerie cave entrance.",
    interactions={"enter": "You cautiously enter the cave."},
    #items=[Item("Torch", "Provides light in dark places.")]
)