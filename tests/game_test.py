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
        sut = Game()
        assert hasattr(sut, 'start_game')

    def test_game_attributes(self):
        sut = Game()
        assert hasattr(sut, 'puzzle') # Checks if constructor has puzzle instance
        assert hasattr(sut, 'game_over') # Checks if constructor has game_over instance
        assert hasattr(sut, 'score') # Checks if constructor has score instance
        assert hasattr(sut, 'lives') # Checks if constructor has lives instance
        assert hasattr(sut, 'ui') # Checks if constructor has UI instance

    def test_start_game_calls_play_turn_until_game_over(self):
        sut = Game()
        call_count = 0 

        def mock_play_turn_side_effect():
        # Stop the game after the first call to simulate the loop stopping
            nonlocal call_count
            call_count += 1
            if call_count == 3:
                sut.game_over = True  # Stop the loop
        
        with patch.object(sut, 'play_turn', side_effect=mock_play_turn_side_effect) as mock_play_turn:
            sut.start_game()
            assert mock_play_turn.call_count == 3, "play_turn should be called until game_over is True"