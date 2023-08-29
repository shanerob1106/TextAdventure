# Import different classes for character creation
from characters.Knight import Knight
from characters.Mage import Mage
from characters.Archer import Archer
from characters.Player import Player

# Locations
from game.locations import village, forest, cave

# Save and load methods
from game.save_load import save_game, load_game

# Introduction
def intro(player):
    print(f"Welcome {player.player_name}!")
    print(f"You are currently exploring, {player.player_location.name}. ")
    print(f"{player.player_location.description} ")
    player_input(player)

# Character creation
def choose_character():

    starting_location = village

    player_name = input("What's your name?: ")

    print("\n--- Class ---")
    print("1. Knight \t Health: 100 \t Attack Power: 10")
    print("2. Mage \t Health: 80 \t Attack Power: 15")
    print("3. Archer \t Health: 90 \t Attack Power: 12")

    choice = int(input("What class do you want to be?: "))

    if choice == 1:
        starting_location = village
        return Player(player_name, Knight(), starting_location)
    elif choice == 2:
        starting_location = cave
        return Player(player_name, Mage(), starting_location )
    elif choice == 3:
        starting_location = forest
        return Player(player_name, Archer(), starting_location )
    else:
        print("Invalid choice. Choose a valid option. ")
        return choose_character()

# Location interactions
def explore_location(player):
    print(f"\nYou are currently exploring, {player.player_location.name}. ")
    print(f"{player.player_location.description} ")

    while True:
        print(f"\n--- Options for {player.player_location.name} ---")
        for interaction_name, interaction_description in player.player_location.interactions.items():
            print(f"{interaction_name.capitalize()} - {interaction_description} ")
        
        action_input = input("\nWhat do you want to do?: ")

        if action_input == 'exit':
            break
        elif action_input in player.player_location.interactions:
            world_interactions(player, action_input)

# Perform interactions
def world_interactions(player, interaction_name):
    interaction_description = player.player_location.interactions.get(interaction_name)
    if interaction_description: 
        print(interaction_description)

        if interaction_name == 'move':
            move_to_new_location(player)
        elif interaction_name == 'rest':
            print("Cannot rest yet.")
            #player.rest()
        elif interaction_name == 'shop':
            print("Cannot shop yet.")
            #player.shop()
        elif interaction_name == 'talk':
            print("Cannot talk to villagers yet.")
            # player.talk()
        else:
            print(f"Unknown interaction {interaction_name}")
        
# Move to new location
def move_to_new_location(player):
    new_location_name = input("Enter the name of the location you want to move to: ")

    if new_location_name == player.player_location.name.lower():
        print("You are already in this location. ")
    else:
        new_location = player.player_location.move(new_location_name)
        if new_location:
            player.move_to(new_location)
            print(f"You are now in {player.player_location.name}. ")
        else:
            print("That location is not available. ")

# Get location by name
def get_location_by_name(location_name):
    for location in [village, forest, cave]:
        if location.name.lower() == location_name:
            return location
    return None

def menu_interactions(player, interaction_name):
    interaction_description = player.interactions.get(interaction_name)
    if interaction_description: 
        print(interaction_description)

        if interaction_name == 'explore':
            explore_location(player)
        elif interaction_name == 'inventory':
            print("Cannot open inventory yet.")
            #player.inventory()
        elif interaction_name == 'skills':
            print("Cannot open skills yet.")
            #player.skills()
        elif interaction_name == 'save':
            save_game(player)
            player_input(player)
        elif interaction_name == 'quit':
            quit()
        else:
            print(f"Unknown interaction {interaction_name}")

# Player input
def player_input(player):
    while True: 
        print("\n--- Options ----")
        print("1. Explore - Explore the current location.")
        print("2. Inventory - Opens the inventory. ")
        print("3. Skills - Open the skills menu. ")
        print("4. Save - Saves the game. ")
        print("5. Quit - Exit the game without saving. ")

        choice = int(input("\nDecision: "))
        if choice == 1:
            explore_location(player)
        elif choice == 2:
            print("You can't open your inventory yet.")
            #player.inventory()
        elif choice == 3:
            print("You can't open your skills yet.")
            #player.skills()
        elif choice == 4:
            save_game(player)
            player_input(player)
        elif choice == 5:
            quit()
        else:
            print("Invalid choice. Choose a valid option. ")

# Main menu
def main_menu():
    print("Welcome to your Text adventure!")
    print("1. Start New Game")
    print("2. Load a save. ")
    print("3. Quit. ")

    mainMenu = int(input("\nChoice: "))

    if mainMenu == 1:
        player = choose_character()
        save_game(player)
        intro(player)
    elif mainMenu == 2:
        player = load_game()
        print(f"\nWelcome back, {player.player_name}")
        print(f"You are currently exploring, {player.player_location.name}")
        player_input(player)
    elif mainMenu == 3: 
        quit()
    else: 
        mainMenu

# Main   
if __name__ == "__main__":
    main_menu()
