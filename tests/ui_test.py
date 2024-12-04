import pytest
from unittest.mock import Mock, patch
from src.ui import UI 


def test_display_welcome_message():
    
    ui = UI()
    with patch('builtins.print') as mock_print:
        ui.display_welcome_message()
        mock_print.assert_called_once()
        assert "Welcome" in mock_print.call_args[0][0]
        
def test_get_player_name():
    
    ui = UI()
    with patch('builtins.input', return_value="PlayerTest") as mock_input:
        player_name = ui.get_player_name()
        mock_input.assert_called_once_with("Enter your name: ")
        assert player_name == "PlayerTest"