from Board import Board
from minimaxTree import *
from miniMax import *
from miniMaxPruning import *

def main():
	l = [[]]
	board = Board(l)
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
		print "Please make your move by entering your move coordinates without spaces, for instance, from (4, 2) to (4, 4), enter 4244"
		inputs = raw_input("User's turn: ")
		moves = []
		for i in range (0, len(inputs)):
			if (i > 0 and i % 2 == 1):
				moves.append((int(inputs[i-1]), int(inputs[i])))
		#print moves
		temp = board.updateBoard(user, moves)
		while (temp == False):
			print "Please make your move by entering your move coordinates without spaces"
			inputs = raw_input("User's turn: ")
			moves = []
			for i in range (0, len(inputs)):
				if (i > 0 and i % 2 == 1):
					moves.append((int(inputs[i-1]), int(inputs[i])))
					temp = board.updateBoard(user, moves)
		userScore += len(moves) - 1
		print "User moved: ", moves
		print " "
		board.displayBoard()
		result = miniMaxPruning(board, evalFunc, computer)
		if (result == (-1, -1)):
			print "Computer Lost!"
		else:
			board.updateBoard(computer, result)
		computerScore += len(result) - 1
		print " "
		print "Computer moved: ", result
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
