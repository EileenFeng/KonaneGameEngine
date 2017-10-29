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
	(cbv, bm) = miniMaxHelper(_DEPTH, currentBoard, evalFunc, root, turn)
	return bm

def miniMaxHelper(depth, board, evalFunc, node, turn):
	isMax = False
	value = 999
	if (_DEPTH % 2 == depth % 2):
		isMax = True
		value = -999

	if (depth == 0):
		node.value = evalFunc(turn, board)
		return (node.value, node.name)

	else:
		children = board.legalMoveList(turn)
		if(len(children) > 0):
			if(isMax): 
				cbv = -999
				bestMove = (-1, -1)
				for move in children:
					newChildNode = Node(move, node, list(), value)
					node.insertChild(newChildNode)
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, move)
					(bv, bm) = miniMaxHelper(depth-1, currentBoard, evalFunc, newChildNode, turn)
					if(bv > cbv):
						cbv = bv
						bestMove = newChildNode.name
				return (cbv, bestMove)
			else: 
				cbv = 999
				bestMove = (-1, -1)
				for move in children:
					newChildNode = Node(move, node, list(), value)
					node.insertChild(newChildNode)
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, move)
					(bv, bm) = miniMaxHelper(depth-1, currentBoard, evalFunc, newChildNode, turn)
					if(bv < cbv):
						cbv = bv
						bestMove = newChildNode.name
				return (cbv, bestMove)

		else:
			if(isMax):
				return (-999, (-1, -1))
			else:
				return (-999, (-1, -1))
