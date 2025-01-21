"""Bagels
A deductive logic game where you must guess a number 
based on clues"""
import random

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
        
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

NUM_DIGITS = int(
    input(
        "How many digits should the number have: "
    )
)

MAX_GUESSES = int(
    input(
        "How many guesses do you need: "
    )
)

def main():
    print(f'''Bagels a deductive logic game.
          
          I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
          Try to guess what it is. 
          These are the clues I will give you:
          When I say:       That means:
          Pico              One digit is correct but wrong position.
          Fermi             One digit is correct and in right position.
          Bagels            No digit is correct''')
    
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print(f"You have {MAX_GUESSES} guesses to get it")
        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")

            if guess == secretNum:
                print("you got it!")
                break

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1


            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The answer was {secretNum}")

        print("Do you want to play again?")
        if not input("> ").lower.startswith("y"):
            break
    
    print("Thanks for playing")


if __name__ == "__main__":
    main()