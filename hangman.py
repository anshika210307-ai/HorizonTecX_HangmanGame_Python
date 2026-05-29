import random

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Word list
words = ["python", "coding", "developer", "computer", "hangman"]

# Random word selection
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong attempts
wrong_guesses = 0

print("🎮 Welcome to Hangman Game!")

# Main game loop
while wrong_guesses < 6:

    # Display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You Won!")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct Guess!")

    # Wrong guess
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print(hangman_stages[wrong_guesses])

# Lose condition
if wrong_guesses == 6:
    print("\n💀 Game Over!")
    print("The word was:", word)