'''
Homework 2 Exercise 2
Tate Minch
1/30/23
Description: Same thing as exercise one, however this time, try except statements are included 
to verify that integers are the input type. If not, an error message is displayed and the program
exits.
'''

def collatz(number:int):
    #Check for odd or even
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return(3 * number + 1)

def main():
    try:
        #Collect number and pass it into collatz
        number = collatz(int(input('Enter Number: ')))
    except ValueError:
        #if value entered is not an int, print error and close program
        print("You must enter an integer!")
        exit(0)

    #while collatz function does not return 1, call it again with new value
    while number != 1:
        number = collatz(number)

if __name__ == '__main__':
    main()