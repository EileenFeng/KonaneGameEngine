from minimaxTree import *
from Board import Board
import copy

_DEPTH = 6

def evalFunc(turn, board):
	opponent = 'X'
	if (turn == 'X'):
		opponent = 'O'
	return (len(board.legalMoveList(turn)) - len(board.legalMoveList(opponent)))

def miniMax(board, evalFunc, turn):
	root = Node((-1, -1), None, list(), -1)
	currentBoard = copy.deepcopy(board)
	miniMaxHelper(_DEPTH, board, evalFunc, root, turn)
	print("Best child index: ", root.bestChildIndex)
	print root.childList[-1].name
	#if (root.bestChildIndex == -1):
	#	return (-1, -1)
	return root.childList[root.bestChildIndex].name

def miniMaxHelper(depth, board, evalFunc, node, turn):
	isMax = False
	value = 999
	if (_DEPTH % 2 == depth % 2):
		isMax = True
		value = -999

	if (depth == 0):
		node.value = evalFunc(turn, board)
		return

	else:
		children = board.legalMoveList(turn)
		if(len(children) > 0):
			for move in children:
				newChildNode = Node(move, node, list(), value)
				node.insertChild(newChildNode)
				currentBoard = copy.deepcopy(board)
				currentBoard.updateBoard(turn, move)
				miniMaxHelper(depth-1, currentBoard, evalFunc, newChildNode, turn)

			bestChild = -1
			compareValue = value
			currentIndex = 0
			for child in node.childList:
				print(child.name)
				if (isMax):
					if (child.value > compareValue):
						compareValue = child.value
						bestChild = currentIndex
				else:
					if (child.value < compareValue):
						compareValue = child.value
						bestChild = currentIndex
				currentIndex+=1
			node.value = compareValue
			node.bestChildIndex = bestChild
			print("Changing ", node.name, " bestChild to", bestChild, ", value: ", compareValue)
		else:
			if(isMax):
				node.value = -999
			else:
				node.value = 999
			node.bestChildIndex = -1

