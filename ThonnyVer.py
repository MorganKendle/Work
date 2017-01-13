from time import sleep
from random import randint
import tabulate

def makeboard(gridsize, playerXY):  #function to make the gameboard
    board = []  #a list to store the board
    square = "\u2588\u2588\u2588"  #a variable to store the blank square character
    player = "°-°"
    row = []  #a list to store the row

    for c in range(0, gridsize):  #a for loop to make the row characters
        row.append(square)  #adds the blank character to row

    for r in range(0, gridsize):  #a for loop to print the row characters
        row = list(row)  #set row to the new value of row
        board.append(row)  #adds the row character to board
    board[playerXY[1]][playerXY[0]] = player
    return board  #sends board out

def printBoard(board):  #function to print the board
    '''
    for r in board:  #for every character in board
        print(str(" ").join(r))#print the character
    '''
    print(tabulate.tabulate(board, tablefmt="fancy_grid"))

def checkBlank(board, playerXY):
    if board[playerXY[0]][playerXY[1]] == "{*}":
        return "blank"
    elif board[playerXY[0]][playerXY[1]] == "{^}":
        return "treasure"
    elif board[playerXY[0]][playerXY[1]] == "{#}":
        return "bandit"
    else:
        return "error"

def makeblankboard(gridsize, nobandit, notreasure):
    '''this is task 2'''
    boardbase = []  #a list to store the treasure chests and bandits
    rowbase = []  #a list to store the rows
    blank = "{*}"  #blank square
    treasure = "{@}"  #treasure square
    bandit = "{#}"  #bandit square
    for x in range(0,gridsize):
        rowbase.append(blank)
        
    for v in range(0,gridsize):
        roww = list(rowbase)
        boardbase.append(roww)

    for i in range(notreasure):
        treasureplace = randint(0, gridsize - 1), randint(0, gridsize - 1)
        print(treasure)
        print(treasureplace[0], treasureplace[1])
        print("\n")
        boardbase[treasureplace[0]][treasureplace[1]] = treasure

    for i in range(0, nobandit): 
        banditplace = randint(0, gridsize - 1), randint(0, gridsize - 1)
        print(bandit)
        print(banditplace[0], banditplace[1])
        print("\n")
        boardbase[banditplace[0]][banditplace[1]] = bandit


    print(tabulate.tabulate(boardbase, tablefmt="fancy_grid"))
        

    return boardbase

def searchsquare(board, playerXY):  #defines a function
    otherboard = checkBlank(board, playerXY)  #use an outside function to do something
    return(otherboard)

def distr():
    dier = True
    while dier == True:
        try:
            distexicusmaximus = int(input("How far do you want to move in that direction?: ")) #asks the user how far they want to move
            dier = False
        except ValueError:
            print("That distance is invalid °~°")
            dier = True
    return(distexicusmaximus)

def gamefunc(playerXY, board, coins, gridsize):  #do this forever
    while True:
        if coins >= 100:
            print("You win!")
            sleep(1)
            quit()
        board = makeboard(gridsize, playerXY)  #make the board
        '''this is task 3 and task 6'''
        printBoard(board)  #prints the board
        '''this is task 1'''
        print("^<^ - ?")
        dier = True
        while dier == True:
            '''this is task 4'''
            move = input("Which direction do you wish to go? (wasd): ")  #asks the user how they would like to move
            if move == "w":  #if the user inputs w
                '''this is task 5'''
                dist = distr()
                if playerXY[1]-dist < 0:  #if the players Y is too big
                    print("A wall blocks your path... -_-")  #print an error message
                else:  #otherwise
                    playerXY = playerXY[0], playerXY[1]-dist  #move the player
                    dier = False
            elif move == "s":  #if the user inputs s
                '''this is task 5'''
                dist = distr()
                if playerXY[1]+dist > 7:  #if the players Y is too small
                    print("A wall blocks your path... -_-")  #prints an error message
                else:  #otherwise
                    playerXY = playerXY[0], playerXY[1]+dist  #move the player
                    dier = False
            elif move == "a":  #if the user inputs a
                '''this is task 5'''
                dist = distr()
                if playerXY[0]-dist < 0:  #if the players X is too small
                    print("A wall blocks your path... -_-")  #prints an error message
                else:  #otherwise
                    playerXY = playerXY[0]-dist, playerXY[1]  #move the player
                    dier = False
            elif move == "d":  #if the user inputs d
                '''this is task 5'''
                dist = distr()
                if playerXY[0]+dist > 7:  #if the players X is too big
                    print("A wall blocks your path... -_-")  #prints an error message
                else:  #otherwise
                    playerXY = playerXY[0]+dist, playerXY[1]  #move the player
                    dier = False
            else:  #if all else fails
                print("That move is invalid °~°")  #tell the player they were wrong
                dier = True
                print(coins)  #print the number of coins they have

#haven't done task 8 yet
def yetanotherstarter():  #Defines a new functiond
    gridsize = 8  #sets the size of the grid
    playerXY = 0, 7  #sets the player's original X and Y
    board = makeboard(gridsize, playerXY)  #set a variable to a function
    pastPos = 0,0  #used for removing the previous X
    notreasure = 10  #sets the number of treasures
    nobandit = 5  #sets the number of bandits
    coins = 0  #sets the number of coins
    ye = str(input("Do you want to start the game? (Y/N) "))  #Asks the user whether they want to start the game
    if ye == "Y":  #Here the program is checking the input against all viable answers
        pas = ("Y")
    elif ye == "y":
        pas = ("Y")
    elif ye == "Yes":
        pas = ("Y")
    elif ye == "yes":
        pas = ("Y")
    elif ye == "N":
        pas = ("N")
    elif ye == "n":
        pas = ("N")
    elif ye == "No":
        pas = ("N")
    elif ye == "no":
        pas = ("N")
    else:
        pas = ("?")
    
    if pas == "Y":  #Uses the result from the checking array above
        print("°<° - Welcome to Dungeoneer [Treasure Hunt], the dungeon crawler made entirely from text, good luck!")  #Menu text
        makeblankboard(gridsize, nobandit, notreasure)  #Makes the board
        gamefunc(playerXY, board, coins, gridsize)  #Starts the game
    elif pas == "N":  #Uses the result from the checking array above
        print (";^;")  #Emoticon
        sleep(1)  #Allows the user to see they cancelled the game
        quit()  #Exits the game
    else:  #If the result was not in the array
        print("°<° - ?")  #Emoticon
        print("Input makes no cense...")  #Tell the user the input wasn't understood
        yetanotherstarter()  #Runs start function again

yetanotherstarter()  #Runs the starter function
