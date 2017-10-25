import sys
import copy
class Board:
	def __init__(self, matrix):
		self.matrix = [['' for x in range(8)] for y in range(8)]
		current = 'X'
		for i in range (0, 8):
			if (i%2 == 0):
				current = 'X'
			else:
				current = 'O'
			for j in range (0, 8):
				self.matrix[i][j] = current
				if (current == 'X'):
					current = 'O'
				else:
					current = 'X'

	#returns (-1, -1) if illegal move, otherwise returns move with right coords
	def convertMove(self, row, col):
		if (row < 1 or col < 1 or row > 8 or col > 8):
			return (-1, -1)
		return (row-1, col-1)


	def displayBoard(self):
		for i  in range(0, 8):
			sys.stdout.write(" ")
			sys.stdout.write (str(i))
		print " "
		for i in range (0, 8):
			for j in range (0, 8):
				sys.stdout.write(" ")
				sys.stdout.write (self.matrix[i][j])
			print "", i
		print " "

	def getLegalMoves(self, turn, pos_x, pos_y):
		legalMoves = []  
		tempMove = [(pos_x, pos_y)]
		tempX = pos_x
		tB = self
		while(tempX + 2 < 8):
			if ((tB.matrix[tempX + 1][pos_y] != turn) and (tB.matrix[tempX + 1][pos_y] != '.')):
				if (tB.matrix[tempX+2][pos_y] == '.'):
					tempX += 2
					tB.matrix[tempX][pos_y] == '.'
					tempMove.append((tempX, pos_y))
					legalMoves.append(copy.deepcopy(tempMove))
				else:
					break
			else:
				break

		tempX = pos_x
		tempMove = [(pos_x, pos_y)]
		tB = self
		while(tempX - 2 > -1):
			if ((tB.matrix[tempX - 1][pos_y] != turn) and (tB.matrix[tempX - 1][pos_y] != '.')):
				if (tB.matrix[tempX-2][pos_y] == '.'):
					tempX -= 2
					tB.matrix[tempX][pos_y] == '.'
					tempMove.append((tempX, pos_y))
					legalMoves.append(copy.deepcopy(tempMove))
				else:
					break
			else:
				break

		tempY = pos_y
		tempMove = [(pos_x, pos_y)]
		tB = self
		while(tempY + 2 < 8):
			if ((tB.matrix[pos_x][tempY + 1] != turn) and (tB.matrix[pos_x][tempY + 1] != '.')):
				if (tB.matrix[pos_x][tempY + 2] == '.'):
					tempY += 2
					tB.matrix[pos_x][tempY] == '.'
					tempMove.append((pos_x, tempY))
					legalMoves.append(copy.deepcopy(tempMove))
				else:
					break
			else:
				break

		tempY = pos_y
		tempMove = [(pos_x, pos_y)]
		tB = self
		while(tempY - 2 > -1):
			if ((tB.matrix[pos_x][tempY - 1] != turn) and (tB.matrix[pos_x][tempY - 1] != '.')):
				if (tB.matrix[pos_x][tempY - 2] == '.'):
					tempY -= 2
					tB.matrix[pos_x][tempY] == '.'
					tempMove.append((pos_x, tempY))
					legalMoves.append(copy.deepcopy(tempMove))
				else:
					break
			else:
				break

		return legalMoves

	def legalMoveList(self, turn):
		result = []
		for i in range(0, 8):
			for j in range(0, 8):
				if (self.matrix[i][j] == turn):
					if(self.getLegalMoves(turn, i, j) != []):
						result += self.getLegalMoves(turn, i, j)
		return result

	def remove(self, pos_x, pos_y):
		self.matrix[pos_x][pos_y] = '.'
