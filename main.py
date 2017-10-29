from Board import Board
from minimaxTree import *
from miniMax import *
from miniMaxPruning import *
import time
import random

def testComputer():
	depthOne = -1
	depthTwo = -1
	while (True):
		depthOneStr = raw_input("Computer 1 is X. Please enter choice of depth for Computer 1: ")
		depthTwoStr = raw_input("Computer 2 is O. Please enter choice of depth for Computer 2: ")

		try:
			depthOne = int(depthOneStr)
			depthTwo = int(depthTwoStr)
			break
		except:
			print "Wrong depth input!"
			continue

	computerOne = 'X'
	computerTwo = 'O'
	board = Board()
	board.remove(1, 6)
	board.remove(1, 7)
	while (True):
		start = time.time()
		moveOne = miniMaxPruning(board, evalFunc, computerOne, depthOne)
		period = time.time() - start
		if (moveOne == -1):
			print("Computer 2 wins!")
			break
		board.updateBoard(computerOne, moveOne)
		print "Computer 1 moved: ", moveOne
		print "Calculation took ", period, " seconds to run."
		board.displayBoard()
		print ""
		
		start = time.time()
		moveTwo = miniMaxPruning(board, evalFunc, computerTwo, depthTwo)
		period = time.time() - start
		if (moveTwo == -1):
			print("Computer 1 wins!")
			break
		board.updateBoard(computerTwo, moveTwo)
		print "Computer 2 moved: ", moveTwo
		print "Calculation took ", period, " seconds to run."
		board.displayBoard()
		print ""
		
def testUser():
	board = Board()
	print "Current board is: "
	board.displayBoard()
	userScore = 0
	computerScore = 0
	inUserInput = True
	while (inUserInput):
		user = raw_input("User's choice: please enter 'X' or 'O': ")
		if (user == 'X'):
			computer = 'O'
			inUserInput = False
		elif (user == 'O'):
			computer = 'X'
			inUserInput = False
		else:
			print("Invalid user's choice!")

	while (True):
		userMoveFirst = False
		computerMoveFirst = False
		firstMove = raw_input("Enter 0 to move first, 1 to let computer move first: ")
		if (firstMove == "0"):
			userMoveFirst = True
			break
		elif (firstMove == "1"):
			computerMoveFirst = True
			break
		else:
			print "Invalid input!"

	while (userMoveFirst):
		removeChoice = raw_input("Please remove one piece in the center or on the side by entering your move coordinates without spaces, for instance, enter 55 to remove piece (5, 5): ")
		removeInt = 0
		try:
			removeInt = int(removeChoice)
			if ((removeInt/10, removeInt%10) in board.getRemovableSet()):
				board.removeFromInput(removeInt)
				break
			else:
				print "Not in the center or on the side!"
		except:
			print "Invalid input!"

	if (computerMoveFirst):
		computerRemove = random.sample(board.getRemovableSet(), 1)[0]
		board.remove(computerRemove[0], computerRemove[1])
		print "Computer removed: ", computerRemove
		board.displayBoard()
		while (True):
			userRemove = raw_input("Please remove one piece adjacent to computer's remove piece, by entering your move coordinates without spaces, for instance, enter 55 to remove piece (5, 5): ")
			try:
				removeInt = int(userRemove)
				if (board.validRemoveAfterComputer(computerRemove, removeInt)):
					board.remove(removeInt/10, removeInt%10)
					board.displayBoard()
					break
				else:
					print "Invalid coordinates!"
			except:
				print "Invalid input!"

	while (True):
		inMoveInput = True
		while (inMoveInput):
			print "Please make your move by entering your move coordinates without spaces, for instance, from (4, 2) to (4, 4), enter 4244."
			inputs = raw_input("User's turn: ")
			try:
				moves = []
				for i in range (0, len(inputs)):
					if (i > 0 and i % 2 == 1):
						moves.append((int(inputs[i-1]), int(inputs[i])))
				if (board.updateBoard(user, moves) == True):
					inMoveInput = False
			except:
				print "Invalid user input!"
				continue

		userScore += len(moves) - 1
		print "User moved: ", moves
		print " "
		board.displayBoard()
		start = time.time()
		result = miniMaxPruning(board, evalFunc, computer, 6)
		period = time.time() - start
		if (result == -1):
			print "Computer Lost!"
		else:
			board.updateBoard(computer, result)
		computerScore += len(result) - 1
		print " "
		print "Computer moved: ", result
		print "Calculation took ", period, " seconds to run."
		print " "
		board.displayBoard()
		print " "
		feedBack()
		# print score
		print "Score Board: "
		print "User Score is: ", userScore
		print "Computer Score is: ", computerScore
		print " "

def main():
	while (True):
		userChoice = raw_input("Type 0 if you want to watch computers play, 1 if you want to play against a computer: ")
		if (userChoice == "0"):
			testComputer()
			break
		elif (userChoice == "1"):
			testUser()
			break
		else:
			print "Please enter 0 or 1!"

main()