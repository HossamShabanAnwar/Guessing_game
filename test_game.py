from operator import call
import unittest
from unittest.mock import patch
import io
import sys

import game  # assuming the given code is in a file named game.py

class TestGame(unittest.TestCase):
    
    # test get_range() function
    
    def test_get_range_valid_input(self):
        with patch('builtins.input', return_value='100') as mock_input:
            result = game.get_range()
            self.assertEqual(result, 100)
    
    def test_get_range_quit_input(self):
        with patch('builtins.input', return_value='quit'), self.assertRaises(SystemExit) as cm:
            game.get_range()
        self.assertEqual(cm.exception.code, None)
    
    def test_get_range_invalid_input(self):
        with patch('builtins.input', side_effect=['0', '10001', 'abc', '']) as mock_input, \
             patch('builtins.print') as mock_print:
            result = game.get_range()
            mock_print.assert_has_calls([call('Invalid input. Please enter a number between 1 and 10,000.')] * 3)
    
    # test get_difficulty() function
    
    def test_get_difficulty_valid_input_easy(self):
        with patch('builtins.input', return_value='easy') as mock_input:
            result = game.get_difficulty()
            self.assertEqual(result, 10)
    
    def test_get_difficulty_valid_input_medium(self):
        with patch('builtins.input', return_value='medium') as mock_input:
            result = game.get_difficulty()
            self.assertEqual(result, 7)
    
    def test_get_difficulty_valid_input_hard(self):
        with patch('builtins.input', return_value='hard') as mock_input:
            result = game.get_difficulty()
            self.assertEqual(result, 5)
    
    def test_get_difficulty_quit_input(self):
        with patch('builtins.input', return_value='quit'), self.assertRaises(SystemExit) as cm:
            game.get_difficulty()
        self.assertEqual(cm.exception.code, None)
    
    def test_get_difficulty_invalid_input(self):
        with patch('builtins.input', side_effect=['abc', 'easy peasy', '']) as mock_input, \
             patch('builtins.print') as mock_print:
            result = game.get_difficulty()
            mock_print.assert_has_calls([call("Invalid input. Please choose a difficulty level of easy, medium, or hard.")] * 3)
    
    # test play_game() function
    
    @patch('builtins.input', side_effect=['10', '1', '2', '3', '4', '5', 'quit', 'n'])
    def test_play_game_easy_difficulty_wins(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        game.play_game()
        sys.stdout = sys.__stdout__
        self.assertIn("Congratulations! You guessed the secret number", captured_output.getvalue())
        self.assertIn("New high score!", captured_output.getvalue())
    
    @patch('builtins.input', side_effect=['10', '1', '2', '3', '4', '5', 'quit', 'n'])
    def test_play_game_easy_difficulty_loses(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        game.play_game()
        sys.stdout = sys.__stdout__
        self.assertIn("Your final score is: 100", captured_output.getvalue())
        self.assertIn("High score is: 0", captured_output.getvalue())
    
    # add more test cases for different scenarios if needed

if __name__ == '__main__':
    unittest.main()
