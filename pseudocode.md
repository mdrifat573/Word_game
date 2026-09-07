Pseudocode

BEGIN
    Display MY name
    My Student ID

Ask user difficulty level
Repeat

Display choices of easy (e), medium (m) or hard (h)
Remove spaces from user input and change to uppercase
Check if input is invalid
Display error message
Until valid input is entered

If input is e then

Set source_list = easy_words
Set word_count = 7
Set guesses_remaining = 5
Set difficulty_name = easy

Else if input is m then

Set source_list = medium_words
Set word_count = 8
Set guesses_remaining = 4
Set difficulty_name = medium

Else

Set source_list = hard_words
Set word_count = 9
Set guesses_remaining = 4
Set difficulty_name = hard

Endif

Randomly select word_count number of words from source_list as word_list
Randomly select one word from word_list as Password
Set starting_guesses = guesses_remaining
Display difficulty name, number of guess, total number of words, and word length
Wait for user press enter key
Set won = false

While guesses_remaining > 0 and won = false
Display all word in word_list with numbering from 1
Display guesses_remaining

Repeat
Ask user to enter the number of a word
Check that user input is a whole number between 1 and the size of the list
If user input is invalid then
Display an error message
END if
Until valid input has been entered

Store choose_word as selected_word and delete it from word_list
Decrease guesses_remaining by 1
Display selected_word

If selected_word equals Password then
Display "Password correct"
Set won to true

Else

Display "Password incorrect"
Set matching_letters to compare_words
Display matching_letters out of Password length as correct

END if
END while

If won = true then

If guesses_remaining = starting_guesses - 1 then
Display "lucky guess!" 
END if
Display "you win!"

Else

Display "you lose!" 
Display the Password

END if
END pseudocode
compare_words function

FUNCTION compare_words(word1, word2)
Set matching_letters to 0

FOR each position from 0 to the length of word1 minus 1
IF the letter in word1 equals the letter in word2 at that position THEN
Increase matching_letters by 1
END IF
END FOR
RETURN matching_letters
END FUNCTION

