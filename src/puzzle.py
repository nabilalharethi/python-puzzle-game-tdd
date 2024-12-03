import random


class Puzzle:
    def __init__(self):
        self.Types = ["Math", "Words", "Logic"]
        
    def generate_types(self):
        return random.choice(self.Types)