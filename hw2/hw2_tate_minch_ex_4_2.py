'''
Homework 2 Exercise 4 part 2
Tate Minch
1/30/23
Description: Same thing as part 1, but now the limits are randomly generated rather than hard coded.
'''
import random

def main():
    limit = 1000
    lowerBound = random.randint(1,limit-1)
    upperBound = random.randint(lowerBound+1,limit)
    num = random.randint(lowerBound,upperBound)
    numGuesses = 0
    print(f'I am thinking of a number between {lowerBound} and {upperBound} (both inclusive). You have 10 tries to guess it.')
    while True:
        try:
            guess = int(input(f'Take a guess ({10 - numGuesses} left): '))
        except ValueError:
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
        if guess < lowerBound or guess > upperBound:
            print('Guess was out of bounds!')
            continue
        print('Your guess was too low') if guess < num else print('Your guess is too high')
        


if __name__ == '__main__':
    main()