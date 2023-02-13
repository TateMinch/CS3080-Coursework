'''
Homework 3 Exercise 4
Tate Minch
2/13/23
Description: Small incomplete tic tac toe game. Game board represented by dictionary. Will take in user input to make moves
and will print board. No error checking or game functionality added, as assignment did not ask for it.
'''
#print each element of the board in easy to see format.
def printBoard(board:dict):
    print(board['TopLeft'] +'|'+ board['TopMiddle']  +'|'+ board['TopRight'])
    print('- - -')
    print(board['MiddleLeft']  +'|' + board['MiddleMiddle'] +'|' + board['MiddleRight'])
    print('- - -')
    print(board['BottomLeft']  +'|' + board['BottomMiddle']  +'|' + board['BottomRight'])

def main():
    #data structure initialized to all empty moves for board
    board = {'TopLeft':' ', 'TopMiddle':' ','TopRight':' ',
    'MiddleLeft':' ', 'MiddleMiddle':' ','MiddleRight':' ',
    'BottomLeft':' ', 'BottomMiddle':' ', 'BottomRight':' '}

    #Takes in moves for every slot on the board.
    for i in range(9):
        printBoard(board)
        if(i%2 == 0):
            board[input('Player 1 turn. Which Space? ')] = 'O'
        else:
            board[input('Player 2 turn. Which Space? ')] = 'X'


if __name__ == '__main__':
    main()
