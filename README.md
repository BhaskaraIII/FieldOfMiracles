# Field of miracles
____
## Short description of the project
This project is an opportunity to implement the game "Field of Miracles". In this version of the game there is no graphics or other visualization of the game process.
____
## Rules of the game
The program guesses a random word. According to the tradition of Russian linguistic games, the word must be a noun, a common noun in the nominative case singular.The player suggests a letter (or the entire word) that may be part of the word. If the player guesses a letter that is in the word, the guessed word is shown and all the guessed letters are indicated. If the player does not guess the letter, he is told that there is no such letter. The game continues until the word is guessed.
____
## Description of the game mechanism from the player's position
The player knows the number of letters in the word, and is shown the word encrypted with the "*" symbol. He can ask to see the rules of the game, as well as the existing commands. If the player enters more than one letter or not a letter, a corresponding error message is displayed. The input is not case sensitive. If the entered letter was, then the corresponding message is also displayed. If the entered letter occurs more than once in a word, then all are opened.
____
## Commands used
- /help - show the rules of the game
- /usedletters - show list of entered letters
- /leftletters - show number of remaining letters
- /surrender - give up
____
