class MenuOption:
    def __init__(self, name, description, interactions=None):
        self.name = name
        self.description = description
        self.interactions = interactions or {}
        
    def add_interaction(self, interaction_name, interaction_description):
        self.interactions[interaction_name] = interaction_description