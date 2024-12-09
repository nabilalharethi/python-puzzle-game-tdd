import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.puzzle import Puzzle

class Game:
    def __init__(self):
        self.puzzle = Puzzle()
        self.game_over = False
        self.score = 0 # would be later changed to instance of score class
        self.lives = 3

    def start_game(self):
        pass

    def play_turn(self):
        pass