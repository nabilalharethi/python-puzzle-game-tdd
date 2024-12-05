import pytest

from unittest.mock import patch

from src.puzzle import Puzzle


class TestPuzzle:
    @pytest.fixture
    def Puzzle(self):
        
        return Puzzle()
    
    def test_puzzle_type_genration(self, Puzzle):
        
        Types = ["Math", "Words", "Logic"]
        generated_types = Puzzle.generate_types()
        assert generated_types in Types

    def test_puzzle_unique_content(self, Puzzle):
        
        Puzzle.set_difficulty(1)
        
        # Generate multiple puzzles and check for uniqueness
        generated_puzzles = set()
        for _ in range(10):
            new_puzzle = Puzzle.generate_puzzle()
            
            if new_puzzle is None:
                break
            assert new_puzzle['content'] not in generated_puzzles
        
            generated_puzzles.add(new_puzzle['content'])

    def test_mock_generate_type(self, Puzzle):
        with patch("random.choice", return_value="Math"):
            
            generated_types = Puzzle.generate_types()
            assert generated_types  == "Math"

    def test_difficulty(self, Puzzle):
        
        Puzzle.set_difficulty(1)
        difficulty = Puzzle.difficulty
        assert difficulty == "Easy"
        
        Puzzle.set_difficulty(2)
        difficulty = Puzzle.difficulty
        assert difficulty == "Medium"
        
        Puzzle.set_difficulty(3)
        difficulty = Puzzle.difficulty
        assert difficulty == "Hard"
        
        with pytest.raises(ValueError):
            Puzzle.set_difficulty(0)
            
            
    def test_genrating_based_on_difficulty(self, Puzzle):
        
        Puzzle.set_difficulty(1)
        easy_puzzle = Puzzle.generate_puzzle()
        assert easy_puzzle["type"] in ["Math", "Words", "Logic"]
        assert "content" in easy_puzzle
        assert "solution" in easy_puzzle
        
        Puzzle.set_difficulty(2)
        medium_puzzle = Puzzle.generate_puzzle()
        assert medium_puzzle["type"] in ["Math", "Words", "Logic"]
        assert "content" in medium_puzzle
        assert "solution" in medium_puzzle
        
        Puzzle.set_difficulty(3)
        hard_puzzle = Puzzle.generate_puzzle()
        assert hard_puzzle["type"] in ["Math", "Words", "Logic"]
        assert "content" in hard_puzzle
        assert "solution" in hard_puzzle       
        
    def test_generating_without_difficulty(self, Puzzle):
        
        with pytest.raises(ValueError):
            Puzzle.generate_puzzle()
                
    def test_answer_validation_math(self, Puzzle):
        
        for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
            Puzzle.set_difficulty(difficulty_level)
            
            puzzles_at_level = Puzzle.puzzle_data[Puzzle.difficulty]
            
            math_puzzles = [p for p in puzzles_at_level if p["type"] == "Math"]
            assert math_puzzles, f"No Math puzzles found in {Puzzle.difficulty} difficulty"
            
            for math_puzzle in math_puzzles:
                Puzzle.validate_answer(math_puzzle, math_puzzle["solution"])
                
            
    def test_answer_validation_words(self, Puzzle):
        
        
        for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
            Puzzle.set_difficulty(difficulty_level)
            
            puzzles_at_level = Puzzle.puzzle_data[Puzzle.difficulty]
            
            math_puzzles = [p for p in puzzles_at_level if p["type"] == "Words"]
            assert math_puzzles, f"No Words  puzzles found in {Puzzle.difficulty} difficulty"
            
            for math_puzzle in math_puzzles:
                Puzzle.validate_answer(math_puzzle, math_puzzle["solution"])
                
    def test_answer_validation_logic(self, Puzzle):
        
        
        for difficulty_level in [1, 2, 3]:  # 1 = Easy, 2 = Medium, 3 = Hard
            Puzzle.set_difficulty(difficulty_level)
            
            puzzles_at_level = Puzzle.puzzle_data[Puzzle.difficulty]
            
            math_puzzles = [p for p in puzzles_at_level if p["type"] == "Logic"]
            assert math_puzzles, f"No logic  puzzles found in {Puzzle.difficulty} difficulty"
            
            for math_puzzle in math_puzzles:
                Puzzle.validate_answer(math_puzzle, math_puzzle["solution"])
                
    def test_puzzle_answer_validation_edge_cases(self, Puzzle):
    
        Puzzle.set_difficulty(1)
        
        test_cases = []
        
        for level, puzzles in Puzzle.puzzle_data.items():
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
        
        
        
        for case in test_cases:
            assert Puzzle.validate_answer(case["puzzle"], case["input"]) == case["expected"], f"Failed for puzzle: {case['puzzle']['content']} with input {case['input']}"
        
    def test_puzzle_time_limit(self, Puzzle):
    
        Puzzle.set_difficulty(2)
        
        for _ in range(10):
            new_puzzle = Puzzle.generate_puzzle()
               
            if new_puzzle is None:
                break
            
            # Add time limit to puzzle dictionary
            assert "time_limit" in new_puzzle, "Puzzle should have a time limit"
            assert isinstance(new_puzzle["time_limit"], int), "Time limit should be an integer"
            assert new_puzzle["time_limit"] > 0, "Time limit should be positive"