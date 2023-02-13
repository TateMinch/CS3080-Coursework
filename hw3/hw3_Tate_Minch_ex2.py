'''
Homework 3 Exercise 1
Tate Minch
2/12/23
Description: Takes in a string from the user and uses a dictionary to count the instances of each letter. Case sensitive,
Ignores whitespace and periods.
'''
import pprint


def main():
    #collect user input for string
    string = input('Enter a string, and I will print out the number of times you used each character!: ')
    numOccurences = {}
    for j in string.replace(' ', '').replace('.',''):
        try:
            #if letter already exists in dict, increment
            numOccurences[j] += 1
        except:
            #otherwise, create and initialize count to 1
            numOccurences[j] = 1

    pprint.pprint(numOccurences)





if __name__ == '__main__':
    main()
