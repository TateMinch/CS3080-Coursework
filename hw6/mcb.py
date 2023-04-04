"""
Homework 6 exercise 3
Name: Tate Minch
Date: 4/3/2023
Description: This is a command-line tool for saving, loading, and deleting text snippets from the clipboard using
keywords, which are stored in a shelf file.
"""
import shelve
import pyperclip
import sys

def save(keyword):
    # Save clipboard content under keyword.
    mcb_shelf[keyword] = pyperclip.paste()

def load(keyword):
    # Load keyword's content to clipboard.
    if keyword in mcb_shelf:
        pyperclip.copy(mcb_shelf[keyword])
    else:
        print(f"No keyword '{keyword}' found.")

def list_keywords():
    # Prints a list of all keywords.
    print(list(mcb_shelf.keys()))

def main():
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        save(sys.argv[2])
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            list_keywords()
        else:
            load(sys.argv[1])
    else:
        print('Usage: python3 mcb.py [save <keyword>], [delete <keyword>], [list], or [<keyword>].')

    mcb_shelf.close()

mcb_shelf = shelve.open('mcb')
if __name__ == '__main__':
    main()
