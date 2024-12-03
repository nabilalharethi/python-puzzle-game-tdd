import pytest

from unittest.mock import patch

from src.puzzle import Puzzle


def test_puzzle_type_genration():
    puzzle = Puzzle()
    Types = ["Math", "Words", "Logic"]
    generated_types = puzzle.generate_types()
    assert generated_types in Types
    


def test_mock_generate_type():
    with patch("random.choice", return_value="Math"):
        puzzle = Puzzle()
        generated_types = puzzle.generate_types()
        assert generated_types  == "Math"
