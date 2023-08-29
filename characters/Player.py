class Player: 
    def __init__(self, player_name, player_class, player_location):
        self.player_name = player_name
        self.player_class = player_class
        self.health = 100
        self.player_location = player_location

    def introduce(self):
        return f"Hello, my name is {self.player_name} and I am a {self.player_class}. "
    
    def move(self, new_location):
        self.player_location = new_location
    
    def wherePlayer(self): 
        return f"Hmm... I think I'm in {self.player_location}. Yeah that seems right. "
    
    def inventory(self):
        return f"Inventory: {self.player_class.inventory} "
    
    def skills(self):
        return f"Skills: {self.player_class.skills} "