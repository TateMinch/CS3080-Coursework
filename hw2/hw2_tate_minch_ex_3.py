'''
Homework 2 Exercise 3
Tate Minch
1/30/23
Description: Program to highlight basic list understanding. Performs
a number of list operations, then calls a custom function to add elements
of the list to a nicely formatted string.
'''

def strList(strItems : list):
    #Define empty string
    allItems=''
    #for each item in list
    for i in strItems:
        #if its the last item, append 'and ' and break the loop
        if i == strItems[-1]:
            allItems += f'and {i}'
            break
        #append item, comma, and space to string
        allItems += f'{i}, '
    #return string
    return allItems



def main():
    pocketContents = ['Wallet', 'Phone', 'Keys']
    print(pocketContents)
    pocketContents.sort()
    print(pocketContents)
    print(pocketContents[0])
    print(pocketContents[1:])
    print(pocketContents[-1])
    print(pocketContents.index('Keys'))
    pocketContents.append('Tablet')
    print(pocketContents)
    pocketContents.insert(1,'Mask')
    print(pocketContents)
    pocketContents.remove('Phone')
    print(pocketContents)
    pocketContents.reverse()
    print(pocketContents)
    print(strList(pocketContents))



if __name__ == '__main__':
    main()