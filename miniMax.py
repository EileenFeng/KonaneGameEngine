from minimaxTree import *
from Board import Board

_DEPTH = 6

def evalFunc(node):


def miniMax(board, evalFunc, tree, turn):
	root = maxNode((-1, -1), None, None, -1)
	miniMaxHelper(_DEPTH, board, evalFunc, root, turn)

def miniMaxHelper(depth, board, evalFunc, node, turn):
	isMax = False
	value = -999
	if (_DEPTH % 2 == depth % 2):
		isMax = True
		value = 999

	if (depth == 0):
		node.value = evalFunc(node)
		return

	else:
		children = legalMoveList(turn)
		for (move in children):
			newChildNode = Node(move, node, None, value)
			node.insertChild(newChildNode)
			miniMaxHelper(depth-1, board, evalFunc, newChildNode, turn)

		bestChild = -1
		compareValue = value
		currentIndex = 0
		for (child in node.childList):
			if (isMax):
				if (child.value > compareValue):
					compareValue = child.value
					bestChild = currentIndex
			else:
				if (child.value < compareValue):
					compareValue = child.value
					bestChild = currentIndex
			currentIndex++
		node.value = compareValue
		node.bestChild = bestChild

