import sys
import copy
class Board:
	def __init__(self, matrix):
		self.matrix = [['' for x in range(9)] for y in range(9)]
		current = 'X'
		for i in range (1, 9):
			if (i%2 == 0):
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
		for i  in range(1, 9):
			sys.stdout.write (str(i))
			sys.stdout.write(" ")
		print("\n")
		for i in range (1, 9):
			sys.stdout.write(str(i) + " ")
			for j in range (1, 9):
				sys.stdout.write(" ")
				sys.stdout.write (self.matrix[i][j])
			print " "

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

	def remove(self, pos_x, pos_y):
		self.matrix[pos_x][pos_y] = '.'

		# check if user input moves are legal
	def isLegalMove(self, turn, moves):
		cur = moves[0]

		#print "check legal moves", cur, self.matrix[cur[0]][cur[1]]
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
							self.matrix[(curRow+nextRow)/2][curCol] = '.'
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
		'''print result
		if (result):
			#print "user moves", moves, "are made"
			self.displayBoard()
			return self
		else:
			print "user input moves are invalid"
			self.displayBoard()
			return self
		'''
