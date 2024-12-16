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
        sut.ui = Mock()
        call_count = 0

        def mock_play_turn_side_effect():
            nonlocal call_count
            call_count += 1
            if call_count == 3:  # Stop the loop after 3 iterations
                sut.game_over = True

    # Mock `play_turn` with the side effect
        with patch.object(sut, 'play_turn', side_effect=mock_play_turn_side_effect) as mock_play_turn:
            sut.ui.prompt_input.return_value = "no"  # Ensure the loop exits gracefully
            sut.start_game()

        # Assert
            assert mock_play_turn.call_count == 3, "play_turn should be called 3 times before game_over is True"

    
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

        sut.ui.prompt_input.return_value = "2"  # Simulate user input for difficulty

        sut.play_turn()

    # Assert that generate_puzzle was called
        mock_puzzle.generate_puzzle.assert_called_once()

    
    def test_play_turn_validates_difficulty_input(self):
        sut = Game()
        sut.ui = Mock()
        sut.puzzle = Mock()

        # Simulate invalid inputs for difficulty and one valid answer
        sut.ui.prompt_input.side_effect = ["0", "4", "2", "dummy_answer"]

        sut.play_turn()

        # Assert that the valid difficulty was set
        sut.puzzle.set_difficulty.assert_called_once_with(2)


    def test_play_turn_displays_puzzle(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        sut.puzzle = mock_puzzle

        # Mock user inputs: difficulty and puzzle answer
        sut.ui.prompt_input.side_effect = ["2", "dummy_answer"]

        sut.play_turn()

        # Assert that display_puzzle was called with the generated puzzle
        sut.ui.display_puzzle.assert_called_once_with(generated_puzzle)

    def test_play_turn_validates_player_answer(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        sut.ui.prompt_input.side_effect = ["2", "4"]  # First for difficulty, second for answer
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        sut.puzzle = mock_puzzle

        sut.play_turn()

        mock_puzzle.validate_answer.assert_called_once_with(generated_puzzle, "4")


    def test_play_turn_updates_score_on_correct_answer(self):
        sut = Game()
        sut.ui = Mock()
        mock_puzzle = Mock()
        sut.puzzle = mock_puzzle

        generated_puzzle = {"content": "2 + 2 = ?", "solution": "4"}
        mock_puzzle.generate_puzzle.return_value = generated_puzzle
        mock_puzzle.validate_answer.return_value = True  # Simulate correct answer

        sut.ui.prompt_input.side_effect = ["2", "4"]  # Difficulty input, then correct answer

        sut.play_turn()

        # Assert score was updated
        assert sut.score.get_current_score()== 20


    def test_reset_game_resets_game_attributes(self):
        # Arrange
        sut = Game()
        sut.score.add_points(50)
        sut.lives = 1
        sut.game_over = True
        sut.puzzle.used_puzzles = {"Puzzle1"}

        # Act
        sut.reset_game()

        # Assert
        assert sut.score.get_current_score() == 0, "Score should reset to 0"
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
        sut.ui.display_welcome_message()
        sut.play_turn.assert_called_once()
