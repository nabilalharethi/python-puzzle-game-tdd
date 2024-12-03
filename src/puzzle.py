import random


class Puzzle:
    def __init__(self):
        self.Types = ["Math", "Words", "Logic"]
        self.difficulty = None
        
    def generate_types(self):
        return random.choice(self.Types)
    
    def set_difficulty(self, level):
        levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        if level not in levels:
            raise ValueError("Invalid difficulty level")
        self.difficulty = levels[level]