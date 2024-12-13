import pytest
from unittest.mock import Mock, patch
from io import StringIO
from src.ui import UI 

class TestUI:
    def setup_method(self):
        self.ui = UI()


    def test_display_welcome_message(self):
        
        
        with patch('builtins.print') as mock_print:
            self.ui.display_welcome_message()
            
            assert mock_print.call_count == 3
            calls = mock_print.call_args_list
            assert "🧩 Welcome to Puzzle Challenge! 🧩" in calls[0][0][0]
            assert "Test your skills across Math, Words, and Logic Puzzles!" in calls[1][0][0]
            assert calls[2][0][0] == "-" * 40

            
    def test_get_player_name(self):

        with patch('builtins.input', return_value="PlayerTest") as mock_input:
            player_name = self.ui.get_player_name()
            mock_input.assert_called_once_with("Enter your name: ")
            assert player_name == "PlayerTest"

    
    def test_get_player_name_empty_input(self):
        with patch('builtins.input', return_value="") as mock_input:
            
            with pytest.raises(ValueError, match="Player name cannot be empty"):
                self.ui.get_player_name()
           
            
   
    def test_get_player_name_short_input(self):
        with patch('builtins.input', return_value="A") as mock_input:
            with pytest.raises(ValueError, match="Player name must be at least 2 characters"):
                self.ui.get_player_name()
    
    def test_show_message(self):
       
        with patch('builtins.print') as mock_print:
            test_message = "this is a message"
            self.ui.show_message(test_message)
            mock_print.assert_called_once_with(test_message)
            
    
    def test_prompt_input(self):

        with patch('builtins.input', return_value="Test Input") as mock_input:
            prompt = "Enter something: "
            result = self.ui.prompt_input(prompt)
            
            mock_input.assert_called_once_with(prompt)
            assert result == "Test Input"
            
    def test_prompt_input_strips_whitespace(self):
        
        with patch('builtins.input', return_value="  Whitespace Test  ") as mock_input:
            result = self.ui.prompt_input("Prompt: ")
            
            assert result == "Whitespace Test"
    
    def test_prompt_input_empty_input(self):
       
        with patch('builtins.input', return_value="") as mock_input:
            result = self.ui.prompt_input("Prompt: ")
            
            assert result == ""

    def test_display_puzzle(self):
        ui = UI()
        puzzle = {"content": "What is 2 + 2?", "solution": "4"}

        # Use patch to capture the output of print
        with patch("sys.stdout", new=StringIO()) as fake_out:
            ui.display_puzzle(puzzle)
            # Assert that the printed output matches the expected string
            assert fake_out.getvalue().strip() == "Puzzle: What is 2 + 2?"