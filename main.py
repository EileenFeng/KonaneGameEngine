from Board import Board

def main():
	l = [[]]
	board = Board(l)
	#board.displayBoard()
	board.remove(4, 5)
	board.remove(0, 0)
	board.remove(2, 2)
	board.remove(2, 4)
	board.remove(2, 6)
	board.remove(3, 6)
	board.remove(1, 6)
	board.displayBoard()
	resultX = board.legalMoveList('X')
	resultO = board.legalMoveList('O')
	print "X", resultX
	print "O", resultO

main()
