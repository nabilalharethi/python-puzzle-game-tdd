
class Score:
    def __init__(self):
        self._current_score = 0
        self._high_score = 0
        
    def get_current_score(self):

        return self._current_score
    

    def get_high_score(self):

        return self._high_score
    
    def add_points(self, points):

        if not isinstance(points, int):
            raise ValueError("Points must be an integer")
        
        if points < 0:
            raise ValueError("Points cannot be negative")
        
        self._current_score += points
        
    def reset_score(self):

        self._current_score = 0
        
    
    def set_high_score(self):
     
        if self._current_score > self._high_score:
            self._high_score = self._current_score