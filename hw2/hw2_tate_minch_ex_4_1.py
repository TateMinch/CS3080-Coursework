'''
Homework 2 Exercise 4 Part 1
Tate Minch
1/30/23
Description: Simple number guessing game. Randomly generates number between 1 and 20 inclusive,
and then takes in an input. The user is told whether the guess is correct, out of bounds, too high, or too low.
User is permitted 10 guesses, at which point the program will display the correct answer and close out.
'''
import random

def main():
    #get random answer and initialize numGuesses to 0
    num = random.randint(1,20)
    numGuesses = 0
    #welcome message
    print('I am thinking of a number between 1 and 20 (both inclusive). You have 10 tries to guess it.')
    #game loop
    while True:
        try:
            guess = int(input(f'Take a guess ({10 - numGuesses} left): '))
        except ValueError:
            #if value entered is not an int, display error and increment numGuesses. 
            #Incorrect value types DO count as answers, so check to make sure user has
            #not used all guesses.
            print('you must enter an integer!')
            numGuesses+=1
            if numGuesses == 10:
                print(f'Sorry, the number I was thinking of was {num}.')
                break
            continue
        numGuesses+=1
        if guess == num:
            print(f'Good Job! You guessed my number in {numGuesses} guesses!')
            break
        if numGuesses == 10:
            print(f'Sorry, the number I was thinking of was {num}.')
            break
        if guess < 1 or guess > 20:
            print('Guess was out of bounds!')
            continue
        print('Your guess was too low') if guess < num else print('Your guess is too high')
        


if __name__ == '__main__':
    main()