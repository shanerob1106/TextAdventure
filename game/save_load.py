import pickle
import os
from characters.Player import Player
from characters.Knight import Knight
from characters.Mage import Mage
from characters.Archer import Archer

save_folder = 'saved_games'
save_path = os.path.join(save_folder, 'save_game.pkl')

def save_game(player):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(save_path, 'wb') as save_file:
        pickle.dump(player, save_file)
        print("Game saved. ")


def load_game():
    try:
        with open(save_path, 'rb') as save_file:
            player = pickle.load(save_file)
            return player
        
    except FileNotFoundError:
        print("No saved game found")
        return None
