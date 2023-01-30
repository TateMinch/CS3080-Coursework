'''
Homework 2, Exercise 1
Tate Minch
1/30/23
Description: Simple implementation of Collatz sequence. Takes in an int,
and if the int is even, it prints and returns the number//2. If it is odd,
it prints and returns 3 times the number plus 1.
'''
def collatz(number:int):
    #check for even or odd
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return(3 * number + 1)


def main():
    #get number and pass it into collatz
    number = collatz(int(input('Enter Number: ')))
    #while collatz doesn't return a 1, call it again with new number
    while number != 1:
        number = collatz(number)

if __name__ == '__main__':
    main()