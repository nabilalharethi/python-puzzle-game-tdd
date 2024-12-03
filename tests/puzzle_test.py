import pytest

from src.puzzle import Puzzle


def test_puzzle_type_genration():
    puzzle = Puzzle()
    Types = ["Math", "Words", "Logic"]
    generated_types = puzzle.generate_types()
    assert generated_types in Types