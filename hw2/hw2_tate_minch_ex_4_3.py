'''
Homework 2 Exercise 4 Part 3
Tate Minch
1/30/23
Description: Same program as part 2, however with this part, the function 'Player' is playing the game.
Makes guesses by cutting value range in half and moving towards answer like binary search. Included in Git repo
is a bash script called 'programCounter.sh', which runs the program 10000 times searching for the message displayed when
the player uses too many guesses. In a few runs of this script, the player had an average win rate of 99.98%.
'''

import random

def player(lowerBound, upperBound, lastGuessWasHigh):
    if ((upperBound - lowerBound)//2) != 0:
        return ((upperBound - lowerBound)//2) + lowerBound
    elif lastGuessWasHigh:
        return lowerBound
    return lowerBound + 1

def main():
    limit = 1000
    lowerBound = random.randint(1,limit - 1)
    upperBound = random.randint(lowerBound + 1,limit)
    num = random.randint(lowerBound,upperBound)
    lastGuessWasHigh = False
    numGuesses = 0
    print(f'I am thinking of a number between {lowerBound} and {upperBound} (both inclusive). You have 10 tries to guess it.')
    while True:
        guess = player(lowerBound, upperBound,lastGuessWasHigh)
        print(f'Guess: {guess}')
        numGuesses+=1
        if guess == num:
            print(f'Good Job! You guessed my number in {numGuesses} guesses!')
            break
        if numGuesses == 10:
            print(f'Sorry, the number I was thinking of was {num}.')
            break
        if guess < num:
            print('Your guess was too low!')
            lastGuessWasHigh=False
            lowerBound = guess
        else:
            print('Your guess was too high!')
            lastGuessWasHigh=True
            upperBound = guess
        
if __name__ == '__main__':
    main()