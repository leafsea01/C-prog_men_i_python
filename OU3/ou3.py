
import re
import random

class boardgenerator(object):
    __slots__ = ['current', 'next']

on = "X"
off = "."
def main(): 
    col = 20
    row = 20
    
    a = input("Enter (G) for glider or (R) for random or S for Semaphore or (C) for custum: ")
    board = generat_new_board(row,col)

    if(a == "G" or a == "g"):
        creat_glider(board)
    
    if(a == "R" or a == "r"):
        random_board(board,row,col)

    if(a == "S" or a == "s"):
        loadSemaphore(board)

    if(a == "C" or a == "c"):
        coustum(board,row,col)
    a = ""
     
    while(a == ""):
        next_generation(board,row,col)
        update_board(board,row,col)
        pint_rboard(board,row)
        print("for next generation press (enter): " )
        a = input("to exit press any key: ")
       
   
    

    
    
   
    
def random_board(board,row, col):

    for i in range(row):
        for j in range (col):

            if 1 == random.randint(0,1):
                board.current[i][j] = on
            
    

    

def generat_new_board(row,col):
    board = boardgenerator()

    board.current = [[off for i in range(col)] for j in range(row)]
    board.next = [[off for i in range(col)] for j in range(row)]
    return board

def creat_glider(board):
    board.current[0][1] = on
    board.current[1][2] = on
    board.current[2][0] = on
    board.current[2][1] = on
    board.current[2][2] = on

def loadSemaphore(board):
    board.current[0][1] = on
    board.current[0][2] = on
    board.current[0][3] = on

def coustum(board,row,col):
    print("Enter posistion for alive cells borde size is (",row,"x",col,"): ",end= "" )
    x = [int(x) for x in re.split(",| ",input())]

    for i in range(0,len(x),2):
        board.current[x[i]][x[i+1]] = on
        

def neighbors(board, row, col,r,c):
    neighbors = 0
    for i in range(3):
        for j in range(3):
            if ((r-1+i) < row and (r-1+i) >= 0) and ((c-1+j) >= 0 and (c-1+j) < col) and (((r-1+i) != r) or ((c-1+j) != c)):
                
                if board.current[(r-1+i)][(c-1+j)] == on:
                    
                    
                    neighbors = neighbors + 1
        
    return neighbors

def next_generation(board,row,col):
    for i in range(row):
        for j in range(col):
            nrneighboars = neighbors(board,row,col,i,j)
            #print(nrneighboars)
            if nrneighboars == 3:
                board.next[i][j] = on
                continue
            if nrneighboars == 2:
                board.next[i][j] = board.current[i][j]
                continue
            board.next[i][j] = off

def update_board(board,row,col):
    for i in range(row):
        for j in range(col):
            board.current[i][j] = board.next[i][j]

def pint_rboard(board,row):

    for i in range(row):
        print(board.current[i][:])


if __name__ == "__main__":
    main()