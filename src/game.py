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
        puzzle = self.puzzle.generate_puzzle()
        pass