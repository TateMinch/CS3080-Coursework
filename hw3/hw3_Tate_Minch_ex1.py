'''
Homework 3 Exercise 1
Tate Minch
2/12/23
Description: Given a 2d array of periods and Os in the shape of a heart oriented incorrectly, this prints it column first rather
than row first.
'''
def main():
    grid = [['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

    numRows = len(grid)
    numCols = len(grid[0])

    for i in range(numCols):
        for j in range(numRows):
            print(grid[j][i],end='')
        print('\n')


if __name__ == '__main__':
    main()
