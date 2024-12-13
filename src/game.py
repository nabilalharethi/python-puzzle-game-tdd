import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.puzzle import Puzzle
from src.ui import UI

class Game:
    def __init__(self):
        self.puzzle = Puzzle()
        self.game_over = False
        self.score = 0 # would be later changed to instance of score class
        self.lives = 3
        self.ui = UI()

    def start_game(self):
        self.ui.display_welcome_message()
        while self.game_over is False:
            self.play_turn()

    def play_turn(self):
        while True:
            try:
                difficulty = int(input("Choose Difficulty (1-3): "))
                if not (1 <= difficulty <= 3):
                    raise ValueError("Invalid difficulty")
                break
            except ValueError:
                self.ui.display_message("Please choose a valid difficulty (1, 2, or 3).")

        self.puzzle.set_difficulty(difficulty)
        puzzle = self.puzzle.generate_puzzle()
        if not puzzle:
            self.ui.display_message("No puzzles left!")
            self.game_over = True
            return
        self.ui.display_puzzle(puzzle)
        
        player_answer = self.ui.get_input("Enter your answer: ")
        if self.puzzle.validate_answer(puzzle, player_answer):
            self.ui.display_message("Correct!")
        else:
            self.ui.display_message("Incorrect!")
        pass