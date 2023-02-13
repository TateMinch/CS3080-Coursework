'''
Homework 3 Exercise 1
Tate Minch
2/12/23
Description: Small inventory program containing functions to print dictionary, add to item count in inventory, or decrement
item counts in dictionary
'''
import pprint

def deleteItem(inventory, item):
    #if item exists in inventory
    try:
        #if there are more than 0 of this item, decrement it
        if inventory[item] > 0:
            inventory[item]-= 1
        #otherwise, print error message
        else:
            print('You cannot delete this item any further!')
    #otherwise, print error message
    except:
        print('You cannot delete an item you don\'t have!')


def addItem(inventory: dict, item: str):
    #if inventory item already exists, increment count by one
    try:
        inventory[item] += 1
    #otherwise, create and initialize value to one
    except:
        inventory[item] = 1


def printInventory(inventory):
    pprint.pprint(inventory)

def main():
    inventory = {'Hand Sanitizer':10, 'Soap':6,'Kleenex':22,'Lotion':16,'Razors':12}
    printInventory(inventory)


if __name__ == '__main__':
    main()
