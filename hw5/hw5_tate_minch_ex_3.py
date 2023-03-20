"""
Homework 5 Exercise 1
Tate Minch
March 20, 2023
This program defines an alternative to the "range" function, called genRange, which accomplishes the same goal using a generator.
"""

def genRange(stop,start = 0,step = 1):
    i = start
    while i < stop:
        yield i
        i+=step

def main():
    for i in genRange(10,0,2):
        print(i)

if __name__ == '__main__':
    main()
