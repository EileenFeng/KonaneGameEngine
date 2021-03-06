from minimaxTree import *
from Board import Board
import copy

_DEPTH = None
inf = float("inf")

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

def miniMax(board, evalFunc, turn):
	global _DEPTH, inf
	root = Node(-1, None, list(), -1)
	currentBoard = copy.deepcopy(board)
	(cbv, bm) = miniMaxHelper(_DEPTH, currentBoard, evalFunc, root, turn)
	return bm

def miniMaxHelper(depth, board, evalFunc, node, turn):
	global _DEPTH, inf
	isMax = False
	value = inf
	if (_DEPTH % 2 == depth % 2):
		isMax = True
		value = -inf

	if (depth == 0):
		node.value = evalFunc(turn, board)
		return (node.value, node.name)

	else:
		children = board.legalMoveList(turn)
		if(len(children) > 0):
			if(isMax): 
				cbv = -inf
				bestMove = -1
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
				cbv = inf
				bestMove = -1
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
			return(None, -1)
