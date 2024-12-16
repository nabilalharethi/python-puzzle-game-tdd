
import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.game import Game

def main():
    """
    Main function to start the Puzzle Challenge game.
    """
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()