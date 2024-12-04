

class UI:
    def __init__(self):
        
        pass
    
        
    def display_welcome_message(self):
        
        print("Welcome to the Puzzle Game!")
        
    def get_player_name(self):
        
        name = input("Enter your name: ").strip()
        
        if not name:
            raise ValueError("Player name cannot be empty")
        return name
    