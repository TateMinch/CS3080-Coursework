"""
Homework 6 exercise 2
Name: Tate Minch
Date: 4/3/2023
Description: This program demonstrates the use of decorators to count the number of function calls and cache function
results for faster execution. The cache decorator caches the results of a fib call using a dictionary, and the
countCalls decorator counts the number of times the fib function is called.
"""
# Define the `cache` decorator to cache the results of a function call
def cache(func):
    cache_dict = {}

    # Define a wrapper function to cache function results
    def wrapper(*args, **kwargs):
        # Create a key based on the function arguments
        key = (args, tuple(kwargs.items()))

        # If the function result is not already cached, cache it
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)

        # Return the cached function result
        return cache_dict[key]

    # Return the wrapper function
    return wrapper

# Define the `countCalls` decorator to count the number of times a function is called
def countCalls(func):
    count = 0

    # Define a wrapper function to count the number of function calls
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        print(f"Call {count} of {func.__name__}")

        return func(*args, **kwargs)

    return wrapper

# Decorate the `fib` function with the `countCalls` and `cache` decorators
# fib = countCalls(cache(fib))
@countCalls
@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def main():
    fib(10)

if __name__ == '__main__':
    main()
