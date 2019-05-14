# Simple Python Hangman Game without Classes
# Author: Emeka Peters

# //*[@id="post-236610"]/div[1]/div[2]/ol[1]/li[1]

import random, sys
from typing import List

f = open("words.txt", "r")
LISTOF_WORDS = f.readlines()
WORD2_GUESS = random.choice(LISTOF_WORDS)
while (len(WORD2_GUESS)) < 3:
    WORD2_GUESS = random.choice(LISTOF_WORDS)
WORDLENGTH = len(WORD2_GUESS)
AZ_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
CURR_GUESS = []
letterStore = []

# SETUP

# Prints the word that is being guessed
def print_guessing_word(wordletts: List) -> None:
    print("The word that you are guessing is: {0}".format(" ".join(wordletts)))

# Prints out how many guesses are left
def print_guesses_left(taken: int, allowed: int) -> None:
    guessLeft = allowed - taken + 1
    print("You have " + str(guessLeft) + " guesses left.")

# Helps to start the game
def beginGame() -> None:
    print("Welcome! You are about to start\n")
    while True:
        name = input("Please enter your name\n").strip()
        if name == '':
            print("Please enter alphabets and/or numbers")
        else:
            break


# Hides the guessing word
def make_guessing_word() -> None:
    for character in WORD2_GUESS: 
        CURR_GUESS.append("*")
    print("Hint: You are guessing a " + str(WORDLENGTH) + "-letter word.\n")
    print("You are allowed to guess a letter between A-Z one at a time.\n")
    print("Maximum of 10 guesses allowed. \n")
    print_guessing_word(CURR_GUESS)


def start_guessing() -> None: #Main part of game
    
    guessesTaken = 1
    MAXNO_OFGUESSES = 10
    print_guesses_left(guessesTaken, MAXNO_OFGUESSES)

    while guessesTaken < MAXNO_OFGUESSES:
        guess = input("Guess a letter from the word\n").lower()
        if not guess in AZ_ALPHABETS: 
            print("Invalid Guess: Your guess must be an alphabet between A-Z!")
        elif guess in letterStore: 
            print("Invalid Guess: That letter has already been guessed!")
        else: 
            letterStore.append(guess)
            if guess in WORD2_GUESS:
                print("Correct!")
                for i in range(0, WORDLENGTH):
                    if WORD2_GUESS[i] == guess:
                        CURR_GUESS[i] = guess
                print_guessing_word(CURR_GUESS)
                print_guesses_left(guessesTaken, MAXNO_OFGUESSES)
                if not '*' in CURR_GUESS:
                    print("Victory! You Survived!")
                    print("The END!")
                    break
            else:
                print("Your guess is incorrect (letter not found in word)")
                guessesTaken += 1
                print_guesses_left(guessesTaken, MAXNO_OFGUESSES)
                if guessesTaken == 10:
                    print("Sorry you lost. You can try again! The word was: {0}".format(SECRET_WORD))


if __name__ == "__main__":
    beginGame()
    make_guessing_word()
    start_guessing()