import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.puzzle import Puzzle
from src.ui import UI
from src.score import Score

class Game:
    def __init__(self):
        self.puzzle = Puzzle()
        self.game_over = False
        self.lives = 3
        self.ui = UI()
        self.score = Score()

    def start_game(self):
        while True:
            self.ui.display_welcome_message()
            self.reset_game()

            while not self.game_over:
                self.play_turn()

            replay = self.ui.prompt_input("Would you like to play again? (yes/no): ")
            if replay != "yes":
                self.ui.show_message("Thanks for playing!")
                self.ui.show_message(f"High Score: {self.score.get_high_score()}")
                break


    def play_turn(self):
        while True:
            try:
                difficulty = int(self.ui.prompt_input("Choose Difficulty (1-3): "))
                if not (1 <= difficulty <= 3):
                    raise ValueError("Invalid difficulty")
                break
            except ValueError:
                self.ui.show_message("Please choose a valid difficulty (1, 2, or 3).")

        self.puzzle.set_difficulty(difficulty)
        puzzle = self.puzzle.generate_puzzle()
        if not puzzle:
            self.ui.show_message("No puzzles left!")
            self.game_over = True
            return

        self.ui.display_puzzle(puzzle)
        player_answer = self.ui.prompt_input("Enter your answer: ")
        if self.puzzle.validate_answer(puzzle, player_answer):
            points = 10 * difficulty
            self.score.add_points(points)
            self.ui.show_message(f"Correct! +{points} points")
        else:
            self.lives -= 1
            self.ui.show_message("Incorrect!")
            if self.lives <= 0:
                self.game_over = True
                self.ui.show_message("Game Over!")

    
    def reset_game(self):
        self.score.reset_score()
        
        self.lives = 3
        self.game_over = False
        self.puzzle.used_puzzles.clear()
        
        self.score.set_high_score()