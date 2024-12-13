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
    
    def test_start_game_calls_ui_message(self):
        sut = Game()
        sut.ui = Mock()
        
        def mock_play_turn():
            sut.game_over = True
        
        sut.play_turn = Mock(side_effect=mock_play_turn)

        sut.start_game()

        sut.ui.display_welcome_message.assert_called_once()

    def test_play_turn_calls_generate_puzzle(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        sut.puzzle = mock_puzzle

        with patch("builtins.input", return_value="2"):
            sut.play_turn()

        mock_puzzle.generate_puzzle.assert_called_once()
    
    def test_play_turn_validates_difficulty_input(self):
        sut = Game()
        sut.ui = Mock()
        sut.puzzle = Mock()

        with patch("builtins.input", side_effect=["0", "4", "2"]):  # Invalid, invalid, valid
            sut.play_turn()
        sut.puzzle.set_difficulty.assert_called_once_with(2)

    def test_play_turn_displays_puzzle(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        sut.puzzle = mock_puzzle

        with patch("builtins.input", return_value="2"):
            sut.play_turn()

        sut.ui.display_puzzle.assert_called_once_with(generated_puzzle)

    def test_play_turn_validates_player_answer(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        sut.ui.get_input.return_value = "4"  # Mock user input
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        sut.puzzle = mock_puzzle

        with patch("builtins.input", return_value="2"):
            sut.play_turn()

        mock_puzzle.validate_answer.assert_called_once_with(generated_puzzle, "4")

    def test_play_turn_updates_score_on_correct_answer(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        sut.puzzle = mock_puzzle
        sut.score = 0
        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        mock_puzzle.validate_answer.return_value = True  # Simulate correct answer

        with patch("builtins.input", return_value="2"):
            sut.play_turn()
        assert sut.score == 10, "Score should increase by 10 for a correct answer"

    def test_reset_game_resets_game_attributes(self):
        # Arrange
        sut = Game()
        sut.score = 50
        sut.lives = 1
        sut.game_over = True
        sut.puzzle.used_puzzles = {"Puzzle1"}

        # Act
        sut.reset_game()

        # Assert
        assert sut.score == 0, "Score should reset to 0"
        assert sut.lives == 3, "Lives should reset to 3"
        assert not sut.game_over, "game_over should be False"
        assert not sut.puzzle.used_puzzles, "used_puzzles should be empty"

    def test_start_game_resets_game_and_starts_loop(self):
        sut = Game()
        sut.ui = Mock()
        sut.reset_game = Mock()  # Mock reset_game to track calls
        sut.play_turn = Mock(side_effect=lambda: setattr(sut, "game_over", True))

    # Act
        sut.start_game()

    # Assert
        sut.reset_game.assert_called_once()
        sut.ui.display_message.assert_called_once_with("Welcome to the Puzzle Game!")
        sut.play_turn.assert_called_once()
