class Location: 
    def __init__(self, name, description, interactions=None, items=None):
        self.name = name
        self.description = description
        self.interactions = interactions or {}
        self.items = items or []

    def add_interaction(self, interaction_name, interaction_description):
        self.interactions[interaction_name] = interaction_description
    
    def add_item(self, item):
        self.items.append(item)

    def move(self, new_location):
        self.player_location = new_location

    def avalible_locations(self, current_location, avalible_locations):
        return [location for location in avalible_locations if location != current_location]