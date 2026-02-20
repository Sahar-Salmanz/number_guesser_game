def provide_hint(guess: int, actual_number: int):
    """Provides a hint to the user based on their guess and the actual number.
    """
    if guess < actual_number:
        return 'Your guess is too low.'
    else:
        return 'Your guess is too high.'