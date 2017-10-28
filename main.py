from Board import Board
from minimaxTree import *
from players import player

def main():
	l = [[]]
	board = Board(l)
	board.remove(4, 5)
	board.remove(4, 4)
	board.displayBoard()
	user = raw_input("User's choice: please enter 'X' or 'O': ")
	if (user == 'X'):
		computer = 'O'
	else:
		computer = 'X'
	while (True):
		print "Please make your move by entering your move coordinates without spaces, for instance, from (4, 2) to (4, 4), enter 4244"
		inputs = raw_input("User's turn: ")
		moves = []
		for i in range (0, len(inputs)):
			if (i > 0 and i % 2 == 1):
				moves.append((int(inputs[i-1]), int(inputs[i])))
		#print moves
		board.updateBoard(user, moves)
		#resultX = board.legalMoveList('X')
		#resultO = board.legalMoveList('O')
		#print "X", resultX
		#print "O", resultO
		result = board.legalMoveList(computer)
		board.updateBoard(computer, result[0])
		print("Computer moved: ", result[0])
main()
