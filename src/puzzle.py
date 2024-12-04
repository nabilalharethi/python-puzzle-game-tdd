import random


class Puzzle:
    def __init__(self):
        self.Types = ["Math", "Words", "Logic"]
        self.difficulty = None
        self.puzzle_data = {
            "Easy": [
                {"type": "Math", "content": "2 + 2 = ?", "solution": 4},
                {"type": "Words", "content": "Fill in the blank: C _ T", "solution": "CAT"},
                 {"type": "Logic", "content": "What comes next? 2, 4, 6, ?","solution": 8}

            ],
            "Medium": [
                {"type": "Math", "content": "12 x 11 = ?", "solution": 132},
                {"type": "Words","content": "Fill in the blanks: _ I _ P _ A _ T","solution": "ELEPHANT"},
                {"type": "Logic","content": "What comes next? 1, 1, 2, 3, 5, ?","solution": 8}

            ],
            "Hard": [
                {"type": "Math","content": "What is the result of (15 × 8) + (12 ÷ 4) - 7?","solution": 117},
                {"type": "Logic", "content": "Rearrange: D E L I M A", "solution": "MEDIAL"},
                {"type": "Words", "content": "Unscramble: P A L E L", "solution": "APPLE"},
                

            ]
        }
        
    def generate_types(self):
        return random.choice(self.Types)
    
    def set_difficulty(self, level):
        levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        if level not in levels:
            raise ValueError("Invalid difficulty level")
        self.difficulty = levels[level]
        
    def generate_puzzle(self):

        if not self.difficulty:
            raise ValueError("Difficulty is not set. Call set_difficulty(level) first.")
        
        puzzles = self.puzzle_data[self.difficulty]
        return random.choice(puzzles)