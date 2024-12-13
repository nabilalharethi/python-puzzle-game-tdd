import pytest
from unittest.mock import Mock, patch
from src.ui import UI 

class TestUI:
    def setup_method(self):
        self.ui = UI()


    def test_display_welcome_message(self):
        
        ui = UI()
        with patch('builtins.print') as mock_print:
            ui.display_welcome_message()
            mock_print.assert_called_once()
            assert "Welcome" in mock_print.call_args[0][0]
            
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

