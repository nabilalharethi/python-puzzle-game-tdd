import pytest

import src.puzzle import Puzzle


def test_puzzle_type_genration():
    puzzle = Puzzle()
    Types = ["Math", "Words", "Logic"]
    assert puzzle.generate_types in Types