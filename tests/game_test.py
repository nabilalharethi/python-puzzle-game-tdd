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
    
    def test_game_initialize_puzzle(self):
        # Patch 'start_game' on the Game class
        with patch.object(Game, 'start_game', autospec=True) as mock_start_game:
            # Instantiate the Game class
            sut = Game()

            # Assert that 'start_game' was called once during initialization
            mock_start_game.assert_called_once()

    def test_rnd(self):  # Ensure all test methods start with "test_"
        pass
