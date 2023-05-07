# Guessing_game

This repository contains a Python program that allows the user to play a guessing game. The game generates a random number between a user-specified range, and the user must guess the number within a specified number of attempts based on their chosen difficulty level. The user's score is inversely proportional to the number of attempts they take to guess the number. The game also keeps track of the user's high score.

Installation
Clone the repository to your local machine using git clone https://github.com/HossamShabanAnwar/guessing-game.git
Navigate to the repository directory on your local machine.
Run the program using the command python guessing_game.py

How to Play
Start the game by running the program.
Choose the maximum range of numbers to guess from (between 1 and 10,000).
Choose a difficulty level (easy, medium, hard) which will determine the number of attempts you have before losing the game.
Guess a number within the range and get feedback on whether your guess was too high, too low, or correct.
Keep guessing until you correctly guess the number or run out of attempts.
If you correctly guess the number, your score will be displayed along with your current high score. If you beat your previous high score, congratulations will be displayed.
You can choose to play the game again or quit by typing "y" or "n" when prompted.
If you choose to quit the game, your current score and high score will be displayed.

Features
Generates a random number between a user-specified range.
Allows the user to choose the range of numbers to guess from, with a minimum range of 1 and a maximum range of 10,000.
Allows the user to choose the difficulty level, which will determine the number of guesses they have before they lose the game.
Keeps track of the user's score based on how many guesses it took them to win the game.
Provides feedback to the user on whether their guess was too high, too low, or correct.
Keeps track of the user's high score and displays it at the end of each game.
Congratulates the user on their new high score if they beat their previous high score.
Allows the user to quit the game at any time by typing "quit".
Provides error handling to make sure the user enters valid input (e.g. an integer within the allowed range) and provides appropriate feedback to the user if they enter invalid input.
Includes unit testing for the implemented code.

Requirements
Python 3.6 or higher

Contributing
Contributions to this project are welcome. If you find any issues or have any suggestions for improvement, please open an issue or submit a pull request.
