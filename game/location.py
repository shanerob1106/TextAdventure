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