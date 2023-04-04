"""
Homework 6 exercise 1
Name: Tate Minch
Date: 4/3/2023
Description: This program uses a decorator function to slow down the execution of another function.
The slowDown decorator factory takes a rate parameter and returns a decorator that sleeps for the specified rate seconds
before calling the decorated function.
"""
import time

# Define a decorator factory `slowDown` that takes a `rate` parameter
def slowDown(rate=1):
    # Define a decorator function that takes a `func` parameter
    def decorator(func):
        # Define a wrapper function that takes any number of arguments
        def wrapper(*args, **kwargs):
            # Sleep for the specified `rate` seconds
            time.sleep(rate)
            # Call the original function `func` with the provided arguments
            return func(*args, **kwargs)
        # Return the wrapper function
        return wrapper
    # Return the decorator function
    return decorator

# Decorate the `myFunc` function with `slowDown(rate=2)` decorator
# myFunc = slowDown(rate=2)(myFunc)
@slowDown(rate=2)
def myFunc():
    print("This function will execute with a 2-second delay.")

def main():
    myFunc()

if __name__ == "__main__":
    main()


