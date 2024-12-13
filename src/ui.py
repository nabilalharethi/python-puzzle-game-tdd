

class UI:
    def __init__(self):
        
        pass
      
    def display_welcome_message(self):
        
        print("🧩 Welcome to Puzzle Challenge! 🧩")
        print("Test your skills across Math, Words, and Logic Puzzles!")
        print("-" * 40)
        
    def get_player_name(self):
        
        name = input("Enter your name: ").strip()
        
        if not name:
            raise ValueError("Player name cannot be empty")
        
        if len(name) < 2:
            raise ValueError("Player name must be at least 2 characters")
        
        return name
    
    def show_message(self, message):
        
        print(message)
        
    def prompt_input(self, prompt):

        return input(prompt).strip()
    
    def display_puzzle(self, puzzle):
        print(f"Puzzle: {puzzle['content']}")