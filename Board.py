import sys
import copy
import random
from sets import Set

class Board:
	def __init__(self):
		self.matrix = [['' for x in range(9)] for y in range(9)]
		current = 'X'
		for i in range (1, 9):
			if (i%2 == 1):
				current = 'X'
			else:
				current = 'O'
			for j in range (1, 9):
				self.matrix[i][j] = current
				if (current == 'X'):
					current = 'O'
				else:
					current = 'X'

	def noMoveTesting(self):
		for i in range (1, 9):
			for j in range (1, 9):
				self.matrix[i][j] = '.'

	def displayBoard(self):
		sys.stdout.write("   ")
		for i in range(1, 9):
			sys.stdout.write (str(i))
			sys.stdout.write(" ")
		print("\n")
		for i in range (1, 9):
			sys.stdout.write(str(i) + " ")
			for j in range (1, 9):
				sys.stdout.write(" ")
				sys.stdout.write (self.matrix[i][j])
			print " "
		print ""

	def getLegalMoves(self, turn, pos_x, pos_y):
		legalMoves = []  
		tempMove = [(pos_x, pos_y)]
		tempX = pos_x
		tB = self
		while(tempX + 2 < 9):
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
		while(tempX - 2 > 0):
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
		while(tempY + 2 < 9):
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
		while(tempY - 2 > 0):
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
		for i in range(1, 9):
			for j in range(1, 9):
				if (self.matrix[i][j] == turn):
					if(self.getLegalMoves(turn, i, j) != []):
						result += self.getLegalMoves(turn, i, j)
		return result

	def getRemovableSet(self):
		removables = Set([(4, 4), (5, 4), (5, 5), (4, 5)])
		for i in range (1, 9):
			removables.add((1, i))
			removables.add((8, i))
			removables.add((i, 1))
			removables.add((i, 8))
		return removables

	def getPossibleRemoves(self, row, column):
		possibleRemoves = []
		for i in range (row-1, row+2):
			if (i > 0 and i < 9 and i != row):
				possibleRemoves.append((i, column))
		for i in range (column-1, column+2):
			if (i > 0 and i < 9 and i != column):
				possibleRemoves.append((row, i))
		return possibleRemoves

	def remove(self, pos_x, pos_y):
		self.matrix[pos_x][pos_y] = '.'

	def validRemoveAfterComputer(self, computerRemove, userRemove):
		if (userRemove not in range (11, 89)):
			return False
		possibleRemoves = self.getPossibleRemoves(computerRemove[0], computerRemove[1])
		return ((userRemove / 10, userRemove % 10) in possibleRemoves)

	def removeFromInput(self, removeInput):
		row = removeInput / 10
		column = removeInput % 10
		self.remove(row, column)
		possibleRemoves = self.getPossibleRemoves(row, column)
		index = random.randint(0, len(possibleRemoves))
		self.remove(possibleRemoves[index][0], possibleRemoves[index][1])
		print "Computer removed ", possibleRemoves[index]
		self.displayBoard()

		# check if user input moves are legal
	def isLegalMove(self, turn, moves):
		cur = moves[0]
		if(self.matrix[cur[0]][cur[1]] != turn):
			return False

		for move in moves:
			if (move[0] < 1 or move[1] > 8):
				return False

		else:
			#moving
			index = 0
			while (index + 1 < len(moves)):
				cur = moves[index]
				nex = moves[index + 1]
				curRow = cur[0]
				curCol = cur[1]
				nextRow = nex[0]
				nextCol = nex[1]
				if (curRow == nextRow):
					if (abs(curCol-nextCol) == 2):
						if ((self.matrix[curRow][curCol] == turn) and (self.matrix[nextRow][nextCol] == '.') and (self.matrix[curRow][(curCol+nextCol)/2] != turn) and (self.matrix[curRow][(curCol+nextCol)/2] != '.')):
							self.matrix[curRow][curCol] = '.'
							self.matrix[curRow][abs(curCol+nextCol)/2] = '.'
							self.matrix[nextRow][nextCol] = turn
						else:
							return False
					else:
						return False
				elif (curCol == nextCol):
					if (abs(curRow-nextRow) == 2):
						if ((self.matrix[curRow][curCol] == turn) and (self.matrix[nextRow][nextCol] == '.') and (self.matrix[(curRow+nextRow)/2][curCol] != turn) and (self.matrix[(curRow+nextRow)/2][curCol] != '.')):
							self.matrix[curRow][curCol] = '.'
							self.matrix[abs(curRow+nextRow)/2][curCol] = '.'
							self.matrix[nextRow][nextCol] = turn
						else:
							return False
					else:
						return False
				else:
					return False
				index += 1
			return True

	def updateBoard(self, turn, moves):
		temp = copy.deepcopy(self.matrix)
		result = self.isLegalMove(turn, moves)
		if (result == False):
			self.matrix = temp
			print("invalid move")
			print("\n")
		return result
		