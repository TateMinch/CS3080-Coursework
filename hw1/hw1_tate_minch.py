'''
Homework 1
Name: Tate Minch
Date: 1/24/23
Description of Program: A "security" program, where a user is asked to answer 3 randomly generated
simple math questions. The user gets 5 attempts to correctly answer each question, and if the questions
are each answered correctly, access is gained to secret info. If not, the user is asked if they would like
to retry. If yes, the program asks the user 3 new randomly generated questions.
'''

import random
import time
import sys
import signal

def signal_handler(sig, frame):
    print('\nGiving up??')
    sys.stdout.flush()
    time.sleep(2)
    print('fine...')
    sys.stdout.flush()
    time.sleep(2)
    print('BYE')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def generateQuestions():
    #create and populate list of random numbers for question and answer generation
    numbersForQuestions = []
    #need 5 integers between 0 and 100
    for i in range(5):
        numbersForQuestions.append(random.randint(0,100))
    #need a random int between 2 and 20 and a random float between 0 and 5
    numbersForQuestions.append(random.randint(2,20))
    numbersForQuestions.append('{:.2f}'.format(random.uniform(0.0,5.0)))

    #create and populate list of questions and answers (tuples) using random numbers from previous list
    questionsAndAnswers = []
    questionsAndAnswers.append((f'What is {str(numbersForQuestions[0])} + {str(numbersForQuestions[1])}?',
    str(numbersForQuestions[0]+numbersForQuestions[1])))

    questionsAndAnswers.append((f'What is ({str(numbersForQuestions[5])} + {str(numbersForQuestions[6])})/2 with INTEGER DIVISION?',
    str(int((numbersForQuestions[5] + float(numbersForQuestions[6]))//2))))

    questionsAndAnswers.append((f'What is ({str(numbersForQuestions[2])} - {str(numbersForQuestions[3])}) * {str(numbersForQuestions[4])}?',
    str((numbersForQuestions[2] - numbersForQuestions[3]) * numbersForQuestions[4])))

    #return list
    return questionsAndAnswers

def askQuestions(questionsAndAnswers) -> bool:
    totalAttemptsAllowed = 5
    incorrectAnswerAttempts = 0
    #for the number of questions (3)
    for i in range(len(questionsAndAnswers)):
        #print out question and prompt user for answer
        print(f'Question {i+1}: {questionsAndAnswers[i][0]}')
        answer = input('Answer: ')
        #if answer is correct, continue to next question
        if answer == questionsAndAnswers[i][1]:
            print('Correct!')
            continue
        #while answer is not the correct one and the user has attempts left
        while answer != questionsAndAnswers[i][1] and incorrectAnswerAttempts < totalAttemptsAllowed - 1:
            #increment number of incorrect attempts and ask again
            incorrectAnswerAttempts+=1
            answer = input(f'WRONG - try again! ({totalAttemptsAllowed - incorrectAnswerAttempts} attempts remaining): ')
        #if the user has used all of their attempts, break out of for loop and return falsy boolean value
        if answer != questionsAndAnswers[i][1]:
            break
        #if the user used more than one attempt, but got the answer right, reset incorrectAnswerAttempts to 0 for next question
        elif incorrectAnswerAttempts > 0:
            print('Correct!')
            incorrectAnswerAttempts = 0
    
    # return truthy or falsey boolean value - if the answers were all successfully answered, incorrectAnswerAttempts will be 0 and false will be returned to
    # the wrongAnswers variable in main, however, if the user reached the max number of attempts without getting the answer correct, the variable
    # incorrectAnswerAttempts will have the value of 4, which will evaluate to true being returned to the wrongAnswers variable in main
    return incorrectAnswerAttempts
            
def main():
    #welcome message
    print('''Welcome to the bridge of self reflection! I am the Troll that owns it! In order to cross the bridge and get access to the secret (and juicy) information, you must answer my three questions! I hope you know what integer division is!''')
    while True:
        #call generateQuestions and pass list of questions and answers into askQuestions, storing truthy or falsy boolean value in wrongAnswers variable
        wrongAnswers = askQuestions(generateQuestions())
        #if the questions were correctly answered, print the secret info and break out of while loop
        if not wrongAnswers:
            print('Congratulations! You gained access to the SECRET INFORMATION...',end='')
            sys.stdout.flush()
            for i in range(3):
                time.sleep(0.5)
                print('.', end='')
                sys.stdout.flush()
            print('\nWait for it',end='')
            sys.stdout.flush()
            for i in range(3):
                time.sleep(0.5)
                print('.', end='')
                sys.stdout.flush()
            time.sleep(2)
            print('\nYou can do basic math! Who woulda thought?')
            break
        #if the questions were not correctly answered, ask if the user would like to try again
        else:
            print('You failed, you can\'t cross my bridge! Unless...', end='')
            sys.stdout.flush()
            for i in range(3):
                time.sleep(0.5)
                print('.', end='')
                sys.stdout.flush()
            time.sleep(1.5)
            #if not, break out of while loop
            if not input('\nWould you like to try again? (Yes or no): ').lower().startswith('y'):
                break
            
if __name__ == '__main__':
    main()
