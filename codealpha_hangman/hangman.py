import random

words = ["sanatana", "vedha", "upanishads", "india", "gurukul","bhuvarloka ", "patalaloka "]

word = random.choice(words)

guessed_letters = []
display_word = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman")
print("Guess the word, one letter at a time.")

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter.")
    
    elif guess in word:
        print(" Correct guess!")
        guessed_letters.append(guess)

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print(" Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1

if "_" not in display_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over! The word was:", word)
