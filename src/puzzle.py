import random
from typing import Any, Dict


class Puzzle:
    def __init__(self):
        self.Types = ["Math", "Words", "Logic"]
        self.difficulty = None
        self.used_puzzles = set()
        self.puzzle_data = {
            "Easy": [
                {"type": "Math", "content": "2 + 2 = ?", "solution": "4"},
                {"type": "Math", "content": "What is 10 - 4?", "solution": "6"},
                {"type": "Math", "content": "What is 2 * 6?", "solution": "12"},
                
                {"type": "Words", "content": "Synonym for 'happy'", "solution": "joyful"},
                {"type": "Words", "content": "Opposite of 'brave'", "solution": "coward"},
                {"type": "Words", "content": "Fill in the blank: C _ T", "solution": "CAT"},
                
                {"type": "Logic", "content": "If A = B and B = C, then A = ?", "solution": "C"},
                {"type": "Logic", "content": "What comes next? 2, 4, 8, 16, ?", "solution": "32"},
                {"type": "Logic", "content": "What comes next? 2, 4, 6, ?","solution": "8"}

            ],
            "Medium": [
                {"type": "Math", "content": "12 x 11 = ?", "solution": "132"},
                {"type": "Math", "content": "What is 15 * 4?", "solution": "60"},
                {"type": "Math", "content": "What is 144 ÷ 12?", "solution": "12"},
                
                {"type": "Words","content": "Fill in the blanks: _ I _ P _ A _ T","solution": "ELEPHANT"},
                {"type": "Words", "content": "Rearrange 'listen' to form a new word", "solution": "silent"},
                {"type": "Words", "content": "Find a 6-letter word that means 'to move quickly'", "solution": "hustle"},
                
                {"type": "Logic", "content": "If P implies Q, and Q is false, what can be said about P?", "solution": "unknown"},
                {"type": "Logic", "content": "What number should replace the '?' 2, 5, 10, 17, ?", "solution": "26"},
                {"type": "Logic","content": "What comes next? 1, 1, 2, 3, 5, ?","solution": "8"}

            ],
            "Hard": [
                {"type": "Math","content": "What is the result of (15 × 8) + (12 ÷ 4) - 7?","solution": "117"},
                {"type": "Math", "content": "Calculate 17^2 - 8^2", "solution": "225"},
                {"type": "Math", "content": "What is 123 * 4?", "solution": "492"},
                
                {"type": "Words", "content": "Unscramble: P A L E L", "solution": "APPLE"},
                {"type": "Words", "content": "Create an anagram of 'algorithm'", "solution": "logarithm"},
                {"type": "Words", "content": "Find a palindrome word", "solution": "level"},
                
                {"type": "Logic", "content": "If A > B, B > C, what is always true about A and C?", "solution": "A > C"},
                {"type": "Logic", "content": "What comes next? 1, 1, 2, 3, 5, 8, ?", "solution": "13"},
                {"type": "Logic", "content": "Rearrange: D E L I M A", "solution": "MEDIAL"},
                
                

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
        available_puzzles = [puzzle for puzzle in puzzles if puzzle['content'] not in self.used_puzzles]
        
        if len(available_puzzles) == 0:
            return None  
        
        new_puzzle = random.choice(available_puzzles)
        self.used_puzzles.add(new_puzzle['content'])
        
        return new_puzzle
    
    
    def validate_answer(self, puzzle: Dict[str, Any], answer: Any) -> bool:

        if answer is None or answer == "" or answer == []:
            raise ValueError("Invalid answer format")
        cleaned_answer = str(answer).strip()

        
        if isinstance(puzzle["solution"], str):
            solution = puzzle["solution"].strip().lower()
            cleaned_answer = cleaned_answer.lower()  
            return cleaned_answer == solution

       
        if isinstance(puzzle["solution"], (int, float)):
            try:
                cleaned_answer = float(cleaned_answer)  
                return cleaned_answer == float(puzzle["solution"])
            except ValueError:
                return False  

       
    
        return cleaned_answer == str(puzzle["solution"]).strip()

