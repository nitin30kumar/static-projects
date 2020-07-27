import os
import time
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
Win=1
Draw=-1
Running=0
Stop=1
Game=Running
Mark='X'

print("Tic-Tac-Toe Game by Nitin Kumar ")
print("Anon 1[X] --- Anon 2[0]\n")
print()
print()
print("Please wait ...")
time.sleep(3)


def DrawBoard():
    
    print("%c  | %c  |  %c " %(board[1],board[2],board[3]))
    print("___|____|____")
    print("%c  |  %c |  %c " %(board[4],board[5],board[6]))
    print("___|____|____")
    print("%c  | %c  |  %c " %(board[7],board[8],board[9]))
    print("   |    |   ")

def CheckPosition(x):
    if(board[x]==' '):
        return True
    else:
        return False

def CheckWin():
    global Game
    #win from 1-2-3
    if(board[1]==board[2]and board[2]==board[3] and board[1]!=' '):
        Game=Win
        
    #win from 4-5-6
    elif(board[4]==board[5]and board[5]==board[6] and board[4]!=' '):
        Game=Win
        
    #win from 7-8-9
    elif(board[7]==board[8]and board[8]==board[9] and board[7]!=' '):
        Game=Win
        
    #win from 1-4-7
    elif(board[1]==board[4]and board[4]==board[7] and board[1]!=' '):
        Game=Win
        
    #win from 2-5-8
    elif(board[2]==board[5]and board[5]==board[8] and board[2]!=' '):
        Game=Win
        
    #win from 3-6-9
    elif(board[3]==board[6]and board[6]==board[9] and board[3]!=' '):
        Game=Win
        
    #win from 1-5-9
    elif(board[1]==board[5]and board[5]==board[9] and board[5]!=' '):
        Game=Win
        
    #win from 3-5-7
    elif(board[3]==board[5]and board[5]==board[7] and board[5]!=' '):
        Game=Win
        
    #in case of draw
    elif (board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game=Running

    
        

while(Game==Running):
    os.system('cls')
    DrawBoard()
    if(player%2!=0):
        print("Anon 1's chance :")
        Mark='X'
    else:
        print("Anon 2's chance :")
        Mark='0'
    choice=int(input("Enter the position between[1-9] where you want to mark :"))
    if(CheckPosition(choice)):
        board[choice]=Mark
        player+=1
        CheckWin()
os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw ")
elif(Game==Win):
    player-=1
    if(player%2!=0):
        print("Anon 1 Won , comgratulations .\n Winner Winner , Burger Dinner ")
    else:
        print("Anon 2 Won , congratulations .\n Winner Winner , Pizza Dinner ")
           


    








