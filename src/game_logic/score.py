class Score:
    def __init__(self, initial_score=100):
        self.score = initial_score

    def decrement_score(self, penalty=10):
        """Decrements the score by a specified penalty amount."""
        self.score -= penalty
        self.score = max(self.score, 0)  # Ensure score does not go below 0

    def get_score(self):
        """Return the current score."""
        return self.score