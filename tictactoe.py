#!/usr/bin/env python3

def validPosition(pos):
        if(pos in range(0, 9)):
                return True
        return False

def play(board, pos):
	if (not validPosition(pos)):
		return False
	if(board[pos] == "_"):
		return True
	return False

def check(board, listOfPOS):
	for i in listOfPOS:
		if(not validPosition(i)):
			return False
	boardValues = []
	for i in listOfPOS:
		boardValues.append(board[i])
	if("_" in boardValues):
		return False
	if(boardValues[0] == boardValues[1] and boardValues[1] == boardValues[2]):
		return True
	return False

def hasPlayerWon(board, pos):
	#check plays with 4
	middle = 4
	for i in range(1, 5):
		pos1 = middle - i
		pos2 = middle
		pos3 = middle + i
		listOfPos = [pos1, pos2, pos3]	
		if pos in listOfPos:
			if(check(board, listOfPos)):
				return True
	upperCorner = 0
	for i in range(1, 4, 2):
		pos1 = upperCorner
		pos2 = upperCorner + i
		pos3 = upperCorner + (i*2)
		listOfPos = [pos1, pos2, pos3]
		if(pos in listOfPos):
                        if(check(board, listOfPos)):
                                return True
	lowerCorner = 8
	for i in range(1, 4, 2):
		pos1 = lowerCorner - (i*2)
		pos2 = lowerCorner - i
		pos3 = lowerCorner 
		listOfPos = [pos1, pos2, pos3]
		if(pos in listOfPos):
                        if(check(board, listOfPos)):
                                return True
	return False  	

def printBoard(board):
	x = 0
	while x < 9:
                print(board[x], board[x+1], board[x+2])
                x += 3

def board():
	board = []
	for x in range(9):
		board.append("_")
	return board

def nextPlayer(player):
	if(player == 1):
		return 2
	return 1

def playerIcon(player):
	if(player == 1):
		return "x"
	return "o"

def start():
	myBoard = board()
	printBoard(myBoard)
	inPlay = True
	player = 1
	while inPlay:	
		pos = input("Player {}: enter a position to play \n".format(player))
		pos = int(pos) - 1
		if(play(myBoard, pos)):
			myBoard[pos] = playerIcon(player)
			if(hasPlayerWon(myBoard, pos)):
				inPlay = False
				printBoard(myBoard)
				print("Player {} wins!".format(player))
				break
			player = nextPlayer(player)
		else:
			print("This play is not acceptable")
		printBoard(myBoard)

start()
