# Password Guesser Deluxe

A Python word guessing game for the Programming Principles assignment at ECU, Semester 2, 2026.

The game randomly chooses a password from a list of words. Your task is to find it before you run out of guesses.

## How to run

You need Python 3. No extra packages are needed.

Open the terminal in the folder containing `word_game.py` and run:

```bash
python3 word_game.py
```

On Windows, you can also use `python word_game.py` if that is how Python is installed.

## How to play

1. Choose `E` for Easy, `M` for Medium or `H` for Hard. Lowercase letters work too.
2. Press Enter to start.
3. Enter the number beside the word you want to guess.
4. Use the feedback to help choose your next word.

| Difficulty | Word length | Words to choose from | Guesses |
| --- | --- | --- | --- |
| Easy | 6 letters | 7 | 5 |
| Medium | 7 letters | 8 | 4 |
| Hard | 8 letters | 9 | 4 |

For an incorrect guess, the game shows how many letters match the password in the same position. For example, `2/6 correct` means two of the six letters are in the correct positions.

The guessed word is removed, so check the numbers again before your next guess. Invalid input does not use a guess.

Finding the password ends the game with a win. Getting it on the first guess also displays `Lucky guess!`. If you run out of guesses, the game reveals the password.

## Code

The program is in `word_game.py`. It uses Python's built-in `random` module to select the words and password. The `compare_words(word1, word2)` function returns the number of letters that match in the same position.

The word lists came from the assignment starter file.

## Student details

- Name: Md Rifat Hasan
- Student number: ADD YOUR STUDENT NUMBER

Replace the student-number placeholder here and in `word_game.py` before submitting.
