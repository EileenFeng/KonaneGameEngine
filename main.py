from Board import Board
from minimaxTree import *
from miniMax import *
from miniMaxPruning import *
import time

def testComputer():
	computerOne = 'X'
	computerTwo = 'O'
	board = Board()
	board.remove(4, 5)
	board.remove(4, 4)
	while (True):
		start = time.time()
		moveOne = miniMaxPruning(board, evalFunc, computerOne, 5)
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
		moveTwo = miniMaxPruning(board, evalFunc, computerTwo, 6)
		period = time.time() - start
		if (moveTwo == -1):
			print("Computer 1 wins!")
			break
		board.updateBoard(computerTwo, moveTwo)
		print "Computer 2 moved: ", moveTwo
		print "Calculation took ", period, " seconds to run."
		board.displayBoard()
		print ""
		
def main():
	board = Board()
	board.remove(4, 5)
	board.remove(4, 4)
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
		inMoveInput = True
		while (inMoveInput):
			print "Please make your move by entering your move coordinates without spaces, for instance, from (4, 2) to (4, 4), enter 4244"
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
main()
#testComputer()