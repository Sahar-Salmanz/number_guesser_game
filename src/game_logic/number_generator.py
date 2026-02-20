import random

def generate_random_number(start: int, end: int) -> int:
    """Generates a random integer between start and end (inclusive).
    """
    return random.randint(start, end)