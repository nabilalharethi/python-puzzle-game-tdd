
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
        
    def test_reset_score(self):

        self.score.add_points(50)
        self.score.reset_score()
        assert self.score.get_current_score() == 0
        
    
    
    def test_high_score(self):

        self.score.add_points(100)
        self.score.set_high_score()
        assert self.score.get_high_score() == 100

        self.score.reset_score()
        self.score.add_points(50)
        self.score.set_high_score()
        assert self.score.get_high_score() == 100
        
    
    def test_score_multiplier(self):

        self.score.set_score_multiplier(2)
        self.score.add_points(10)
        assert self.score.get_current_score() == 20
