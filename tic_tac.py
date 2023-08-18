import numpy as np
from time import sleep
import random
 
def possibilities(board):
    res=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                res.append((i,j))
    return res
 
def select(board,player):
    choices= possibilities(board)
    selected= random.choice(choices)
    board[selected]=player
    return board
    
def row_win(board,player):
    for i in range(len(board)):
        flag= 1
        for j in range(len(board)):
            if board[i][j]!=player:
                flag= 0
                break
        if flag:
            break
    return flag
 
def col_win(board,player):
    for i in range(len(board)):
        flag= 1
        for j in range(len(board)):
            if board[j][i]!=player:
                flag= 0
                break
        if flag:
            break
    return flag
    
def diag_win(board,player):
    flag=1
    for i in range(len(board)):
        if board[i][i]!= player:
            flag=0
            break
    if flag:
        return flag
    flag=1
    j= len(board)-1
    for i in range(len(board)):
        if board[i][j]!=player:
            flag=0
            break
        j=j-1
    return flag
 
def play_game(board):
    winner=0
    counter=1
    print(board)
    sleep(2)
    
    while winner==0:
        for i in [1,2]:
            if counter==10:
                return 0
            player=i
            board= select(board,player)
            print("The Board after ",counter," moves is\n",board)
            if row_win(board,player) or col_win(board,player) or diag_win(board,player):
                winner=player
                break
            counter=counter+1
            sleep(3)
            
    return winner
 
if __name__=='__main__':
    board= np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    ans= play_game(board)
    if ans:
        print("The winner is Player ",ans)
    else:
        print("No Winner!!")