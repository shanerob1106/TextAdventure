from game.menu_option import MenuOption

menu_options = MenuOption(
    name="Menu",
    description="A simple Menu to control the game",
    interactions={"explore": "You can explore new areas.",
                  "inventory": "View your inventory and items.",
                  "skills": "Check your character's skills and abilities.",
                  "save": "Save your progress in the game.",
                  "quit": "Quit the game."},
)
