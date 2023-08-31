class Player: 
    def __init__(self, player_name, player_class, player_location, player_menu=None):
        self.player_name = player_name
        self.player_class = player_class
        self.health = 100
        self.player_location = player_location
        self.player_menu = player_menu or {}
        self.discovered_towns = []

    def introduce(self):
        return f"Hello, my name is {self.player_name} and I am a {self.player_class}. "
    
    def move(self, new_location):
        self.player_location = new_location
    
    def describle_current_location(self): 
        if self.current_location:
            return str(self.current_location)
        else:
            return "You are not currently in a location. "
    
    def inventory(self):
        return f"Inventory: {self.player_class.inventory} "
    
    def skills(self):
        return f"Skills: {self.player_class.skills} "
    
    def save_discovered_towns(self): 
        return ','.join (self.discovered_towns)
    
    def load_discovered_towns(self, towns_str):
        self.discovered_towns = towns_str.split(',')