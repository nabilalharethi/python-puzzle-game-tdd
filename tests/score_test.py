
import pytest

from unittest.mock import patch

from src.score import Score
class TestScore:
    def setup_method(self):

        self.score = Score()
    
    def test_initial_score(self):

        assert self.score.get_current_score() == 0
        assert self.score.get_high_score() == 0
        
    def test_add_points(self):

        self.score.add_points(10)
        assert self.score.get_current_score() == 10
