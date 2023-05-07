import random


def get_range():
    while True:
        range_input = input(
            "Enter the maximum range of numbers to guess from (between 1 and 10,000): "
        )
        if (
            range_input.isdigit()
            and int(range_input) >= 1
            and int(range_input) <= 10000
        ):
            return int(range_input)
        elif range_input == "quit":
            exit()
        else:
            print("Invalid input. Please enter a number between 1 and 10,000.")


def get_difficulty():
    while True:
        difficulty_input = input("Choose a difficulty level (easy, medium, hard): ")
        if difficulty_input.lower() == "easy":
            return 10
        elif difficulty_input.lower() == "medium":
            return 7
        elif difficulty_input.lower() == "hard":
            return 5
        elif difficulty_input == "quit":
            exit()
        else:
            print(
                "Invalid input. Please choose a difficulty level of easy, medium, or hard."
            )


def play_game():
    max_num = get_range()
    max_attempts = get_difficulty()
    attempts = max_attempts
    secret_num = random.randint(1, max_num)
    score = max_num * 100
    high_score = 0
    print(f"\nGuess a number between 1 and {max_num}. You have {attempts} attempts.\n")

    while attempts > 0:
        try:
            guess = input("Enter your guess: ")
            if guess == "quit":
                exit()
            guess = int(guess)
            if guess < 1 or guess > max_num:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {max_num}.")
        else:
            if guess == secret_num:
                print(
                    f"\nCongratulations! You guessed the secret number {secret_num} and scored {score} points!"
                )
                if score > high_score:
                    high_score = score
                    print("New high score!")
                break
            elif guess < secret_num:
                print("Too low!")
            else:
                print("Too high!")
            attempts -= 1
            score = int(
                max_num / (max_attempts - attempts)
            )  # Should I count the last attempt or not?
            print(f"You have {attempts} attempts left.\n")

    while True:
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == "y":
            break
        elif play_again == "n" or play_again == "quit":
            print(f"\nYour final score is: {score}")
            print(f"High score is: {high_score}\n")
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


play_game()
