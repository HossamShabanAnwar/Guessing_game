import random


def play_game():
    print("Welcome to the number guessing game!")
    high_score = 0
    while True:
        min_range = int(input(f"Please enter Min range ( 1 <= Min_range < 10,000): "))
        max_range = int(input(f"Please enter Max range ( 1 < Max_range <= 10,000): "))
        max_tries = int(
            input(
                f"Enter the maximum number of tries (10 tries (easy), 7 tries (medium), 5 tries (hard)): "
            )
        )
        # Generate a random number and start the game
        secret_number = random.randint(min_range, max_range)
        print(
            f"The secret number is between {min_range} and {max_range}. You have {max_tries} guesses."
        )
        score = max_range  # Initialize score to max possible value
        for attempt in range(1, max_tries + 1):
            # Prompt the user for a guess
            while True:
                try:
                    guess = int(input(f"Guess #{attempt}: "))
                    if guess < min_range or guess > max_range:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        f"Invalid input. Please enter an integer between {min_range} and {max_range}."
                    )
            # Compare the guess to the secret number and give feedback
            if guess == secret_number:
                print(
                    f"Congratulations! You guessed the secret number ({secret_number}) in {attempt} tries."
                )
                score = max_range // attempt
                if score > high_score:
                    high_score = score
                    print(f"New high score: {high_score}!")
                break
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        else:
            print(
                f"Sorry, you ran out of guesses. The secret number was {secret_number}."
            )
        # Prompt the user to play again or quit
        while True:
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again == "y":
                break
            elif play_again == "n" or play_again == "quit":
                print(f"Your final score is: {score}")
                print(f"Your high score is: {high_score}")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    play_game()
