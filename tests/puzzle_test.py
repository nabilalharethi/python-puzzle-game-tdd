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

def test_difficulty():
    puzzle = Puzzle()
    puzzle.set_difficulty(1)
    difficulty = puzzle.difficulty
    assert difficulty == "Easy"
    
    puzzle.set_difficulty(2)
    difficulty = puzzle.difficulty
    assert difficulty == "Medium"
    
    puzzle.set_difficulty(3)
    difficulty = puzzle.difficulty
    assert difficulty == "Hard"
    
    with pytest.raises(ValueError):
        puzzle.set_difficulty(0)
        
        
def test_genrating_based_on_difficulty():
    
    puzzle = Puzzle()
    
    puzzle.set_difficulty(1)
    easy_puzzle = puzzle.generate_puzzle()
    assert easy_puzzle["type"] in ["Math", "Words", "Logic"]
    assert "content" in easy_puzzle
    assert "solution" in easy_puzzle
    
    puzzle.set_difficulty(2)
    medium_puzzle = puzzle.generate_puzzle()
    assert medium_puzzle["type"] in ["Math", "Words", "Logic"]
    assert "content" in medium_puzzle
    assert "solution" in medium_puzzle
    
    puzzle.set_difficulty(3)
    hard_puzzle = puzzle.generate_puzzle()
    assert hard_puzzle["type"] in ["Math", "words", "Logic"]
    assert "content" in hard_puzzle
    assert "solution" in hard_puzzle
    
    
def test_generating_without_difficulty():
    puzzle = Puzzle()
    
    with pytest.raises(ValueError):
        puzzle.generate_puzzle()
    
    
def test_answer_validation_math():
    
    puzzle = Puzzle()
    for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
        puzzle.set_difficulty(difficulty_level)
        
        puzzles_at_level = puzzle.puzzle_data[puzzle.difficulty]
        
        math_puzzles = [p for p in puzzles_at_level if p["type"] == "Math"]
        assert math_puzzles, f"No Math puzzles found in {puzzle.difficulty} difficulty"
        
        for math_puzzle in math_puzzles:
            puzzle.validate_answer(math_puzzle, math_puzzle["solution"])
            
        
def test_answer_validation_words():
    
    puzzle = Puzzle()
    for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
        puzzle.set_difficulty(difficulty_level)
        
        puzzles_at_level = puzzle.puzzle_data[puzzle.difficulty]
        
        math_puzzles = [p for p in puzzles_at_level if p["type"] == "Words"]
        assert math_puzzles, f"No Words  puzzles found in {puzzle.difficulty} difficulty"
        
        for math_puzzle in math_puzzles:
            puzzle.validate_answer(math_puzzle, math_puzzle["solution"])
            
def test_answer_validation_logic():
    
    puzzle = Puzzle()
    for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
        puzzle.set_difficulty(difficulty_level)
        
        puzzles_at_level = puzzle.puzzle_data[puzzle.difficulty]
        
        math_puzzles = [p for p in puzzles_at_level if p["type"] == "Logic"]
        assert math_puzzles, f"No logic  puzzles found in {puzzle.difficulty} difficulty"
        
        for math_puzzle in math_puzzles:
            puzzle.validate_answer(math_puzzle, math_puzzle["solution"])