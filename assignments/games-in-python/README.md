
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build an interactive Hangman game in Python to practice string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Implement the Hangman game

#### Description
Create a command-line Hangman game that selects a secret word from a predefined list and lets a single player guess letters until they either guess the word or run out of allowed incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Prompt the player to guess single letters and accept input.
- Display current progress using underscores for unknown letters (for example: _ a _ _ a _).
- Reveal correctly guessed letters in their correct positions.
- Track and display remaining incorrect guesses.
- End the game when the word is fully guessed or the player runs out of attempts.
- Print a clear win or lose message that shows the correct word.

#### Example gameplay

```
Progress: _ a _ _ a _
Guess a letter: a
Good guess! Progress: _ a _ _ a _
Guess a letter: n
Sorry, 'n' is not in the word. Attempts left: 5
...
Congratulations — you guessed "python"!
```
