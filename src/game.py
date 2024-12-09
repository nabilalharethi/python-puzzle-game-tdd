from src.puzzle import Puzzle

class Game:
    def __init__(self):
        self.puzzle = Puzzle()
        self.game_over = False
        self.score = 0 # would be later changed to instance of score class
        self.lives = 3

    def start_game():
        pass