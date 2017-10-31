from Board import Board

class Node:
	def __init__(self, name, parent, childList, value): 
		self.name = name
		self.parent = parent
		self.childList = childList
		self.value = value 

	def insertChild(self, node):
		self.childList.append(node)

	def setParent(self, minNode):
		self.minParent = minNode

def evalFunc(turn, board):
	opponent = 'X'
	if (turn == 'X'):
		opponent = 'O'
	turnScore = 0
	opponentScore = 0
	turnList = board.legalMoveList(turn)
	opponentList = board.legalMoveList(opponent)
	for move in turnList:
		turnScore += (len(move)-1)
	for move in opponentList:
		opponentScore += (len(move)-1)
	return (turnScore - opponentScore)