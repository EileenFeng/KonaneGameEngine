from Board import Board
from minimaxTree import *
from miniMax import *
from players import player

def main():
	l = [[]]
	board = Board(l)

	'''board.noMoveTesting()
	result =  miniMax(board, evalFunc, 'X')
	print("Move generated: ", result)
	'''

	board.remove(4, 5)
	board.remove(4, 4)
	board.displayBoard()
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
		board.updateBoard(user, moves)
		result = miniMax(board, evalFunc, computer)
		print(result)
		board.updateBoard(computer, result)
		board.displayBoard()
		print("Computer moved: ", result)
main()
