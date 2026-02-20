from src.utils.input_validator import get_valid_input
from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.game_logic.score import Score


def main():
    actual_number = generate_random_number(1, 100)
    score = Score()

    while True:
        user_input = get_valid_input(1, 100)
        if user_input == actual_number:
            print(f'Congratulations! You guessed the number. Your score is {score.get_score()}.')
            replay = input('Would you like to play again (yes/no)? ')
            if replay.lower() == 'yes':
                actual_number = generate_random_number(1, 100)
                score = Score()
                continue
            else:
                break
        else:
            hint = provide_hint(user_input, actual_number)
            print(hint)
            score.decrement_score()



if __name__ == '__main__':
    main()