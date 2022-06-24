#JESUS IS LORD!
#TIC TAC TOE GAME BY ME!!
# PLEASE FOLLOW ON INSTAGRAM @tobor._
def displayboard(): #prints sample board
    gb= [' ','1','2','3','4','5','6','7','8','9']
    print(gb[1],gb[2] ,gb[3], sep=" | ")
    print('---------')
    print(gb[4],gb[5] ,gb[6], sep=" | ")
    print('---------')
    print(gb[7],gb[8] ,gb[9], sep=" | ")
def displayboard_2(gb1): #prints actual game board for playing
    print('\n'*3)
    print(gb1[1] , "|" , gb1[2] , '|' ,  gb1[3])
    print('---------')
    print(gb1[4] , "|" , gb1[5] , "|" , gb1[6])
    print('---------')
    print(gb1[7] , "|" , gb1[8] , "|" , gb1[9])

def player_input():
    position = 0
    while position not in range(1,10):
         position = int(input('please input a position (1-9): '))
    return position


def play(position,board,marker):
    while True:
        if board[position] == ' ': #checks to make sure you don't play in a filled up position
            board[position] = marker
            break
        else:
            print(" ", sep="\n\n")
            print("try another space!!!")
            print()
            position = int(input('please input a position (1-9): '))
counter2 = 0
tries = 0
gb1= [' ']*10
displayboard()
displayboard_2(gb1)
while True:
    position = player_input()

    play(position,gb1,'X')
    tries += 1 #counts for each time you have a valid play
    if tries > 8:
        counter2 += 1
        displayboard_2(gb1)
        break
    print()

    displayboard_2(gb1)
    # conditions under check if you win, it has a total of 8 combinations  
    if ' ' not in gb1[1] and gb1[2] and gb1[3]:
        if gb1[1] == gb1[2] and gb1[2] == gb1[3]:
            break
    if ' ' not in gb1[4] and gb1[5] and gb1[6]:
        if gb1[4] == gb1[5] and gb1[5] == gb1[6]:
            break
    if ' ' not in gb1[7] and gb1[8] and gb1[9]:
        if gb1[7] == gb1[8] and gb1[8] == gb1[9]:
            break
    if ' ' not in gb1[1] and gb1[4] and gb1[7]:
        if gb1[1] == gb1[4] and gb1[4] == gb1[7]:
            break
    if ' ' not in gb1[2] and gb1[5] and gb1[8]:
        if gb1[2] == gb1[5] and gb1[5] == gb1[8]:
            break
    if ' ' not in gb1[3] and gb1[6] and gb1[9]:
        if gb1[3] == gb1[6] and gb1[6] == gb1[9]:
            break
    if ' ' not in gb1[1] and gb1[5] and gb1[9]:
        if gb1[1] == gb1[5] and gb1[5] == gb1[9]:
            break
    if ' ' not in gb1[3] and gb1[5] and gb1[7]:
        if gb1[3] == gb1[5] and gb1[5] == gb1[7]:
            break
    position = player_input()

    play(position,gb1,'O')
    tries += 1
    if tries > 8:
        counter2 += 1
        displayboard_2(gb1)
        break
    print()

    displayboard_2(gb1)

    if ' ' not in gb1[1] and gb1[2] and gb1[3]:
        if gb1[1] == gb1[2] and gb1[2] == gb1[3]:
            break
    if ' ' not in gb1[4] and gb1[5] and gb1[6]:
        if gb1[4] == gb1[5] and gb1[5] == gb1[6]:
            break
    if ' ' not in gb1[7] and gb1[8] and gb1[9]:
        if gb1[7] == gb1[8] and gb1[8] == gb1[9]:
            break
    if ' ' not in gb1[1] and gb1[4] and gb1[7]:
        if gb1[1] == gb1[4] and gb1[4] == gb1[7]:
            break
    if ' ' not in gb1[2] and gb1[5] and gb1[8]:
        if gb1[2] == gb1[5] and gb1[5] == gb1[8]:
            break
    if ' ' not in gb1[3] and gb1[6] and gb1[9]:
        if gb1[3] == gb1[6] and gb1[6] == gb1[9]:
            break
    if ' ' not in gb1[1] and gb1[5] and gb1[9]:
        if gb1[1] == gb1[5] and gb1[5] == gb1[9]:
            break
    if ' ' not in gb1[3] and gb1[5] and gb1[7]:
        if gb1[3] == gb1[5] and gb1[5] == gb1[7]:
            break
if counter2 == 1: # this happens if the board is full and no win condition was satisfied
    print()
    print("It's a draw")
else: # this happens if any of the 8 win conditions were satisfied
    if gb1[1] == gb1[2] and gb1[2] == gb1[3] == 'X' or gb1[4] == gb1[5] and gb1[5] == gb1[6] == 'X' or gb1[7] == gb1[8] and gb1[8] == gb1[9] =='X' or gb1[1] == gb1[4] and gb1[4] == gb1[7] == 'X' or gb1[2] == gb1[5] and gb1[5] == gb1[8] == 'X' or gb1[3] == gb1[6] and gb1[6] == gb1[9] == 'X' or gb1[1] == gb1[5] and gb1[5] == gb1[9] == 'X' or gb1[3] == gb1[5] and gb1[5] == gb1[7] == 'X':
        print()
        print("X wins!!!!!!!!!")
    else:
        print()
        print("O wins!!!!!!!!!")
# This is a  game I applied with my basic knowlegde of lists and functions
