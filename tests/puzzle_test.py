import pytest

from unittest.mock import patch

from src.puzzle import Puzzle



def test_puzzle_type_genration():
    puzzle = Puzzle()
    Types = ["Math", "Words", "Logic"]
    generated_types = puzzle.generate_types()
    assert generated_types in Types

def test_puzzle_unique_content():
    
    puzzle = Puzzle()
    puzzle.set_difficulty(1)
    
    # Generate multiple puzzles and check for uniqueness
    generated_puzzles = set()
    for _ in range(10):
        new_puzzle = puzzle.generate_puzzle()
        
        if new_puzzle is None:
            break
        assert new_puzzle['content'] not in generated_puzzles
    
        generated_puzzles.add(new_puzzle['content'])


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
    assert hard_puzzle["type"] in ["Math", "Words", "Logic"]
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
            
def test_puzzle_answer_validation_edge_cases():
   
    puzzle = Puzzle()
    puzzle.set_difficulty(1)
    
    test_cases = []
    
    for level, puzzles in puzzle.puzzle_data.items():
        for puzzle_data in puzzles:
            solution = puzzle_data['solution']
            content = puzzle_data['content']

           
            if isinstance(solution, str):
                test_cases.append({
                    "input": solution,  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": solution.upper(),  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": solution.lower(),  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": f" {solution} ",  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": "wrong",  
                    "expected": False,
                    "puzzle": puzzle_data
                })

           
            if isinstance(solution, (int, float)):
                test_cases.append({
                    "input": str(solution),  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": f"{solution} ",  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": str(float(solution)),  
                    "expected": False,  
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": "4.0",  
                    "expected": False,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": "wrong number", 
                    "expected": False,
                    "puzzle": puzzle_data
                })

            
            if isinstance(solution, str):
                test_cases.append({
                    "input": solution,  
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": solution.upper(), 
                    "expected": True,
                    "puzzle": puzzle_data
                })
                test_cases.append({
                    "input": "wrong answer",  
                    "expected": False,
                    "puzzle": puzzle_data
                })
    
    
    test_puzzle = next(p for p in puzzle.puzzle_data["Easy"] if p['type'] == "Math")
    
    for case in test_cases:
        assert puzzle.validate_answer(test_puzzle, case['input']) == case['expected']