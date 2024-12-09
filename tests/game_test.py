import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from unittest.mock import patch, Mock, MagicMock
from src.game import Game


class TestGame:
    @pytest.fixture
    
    def game_class(self):
        return Game  # Provide the Game class as a fixture
    
    def test_startgame_exists(self):
        #create sut variable 
        assert hasattr(Game, 'start_game')

    def test_game_attributes(self):
        sut = Game()
        assert hasattr(sut, 'puzzle') # Checks if constructor has puzzle instance
        assert hasattr(sut, 'game_over') # Checks if constructor has game_over instance
        assert hasattr(sut, 'score') # Checks if constructor has score instance
        assert hasattr(sut, 'lives') # Checks if constructor has lives instance