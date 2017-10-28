from minimaxTree import *
from Board import Board
import copy

_DEPTH = 6

def evalFunc(turn, board):
	opponent = 'X'
	if (turn == 'X'):
		opponent = 'O'
	return (len(board.legalMoveList(turn)) - len(board.legalMoveList(opponent)))

def miniMaxPruning(board, evalFunc, turn):
	root = Node((-1, -1), None, list(), -1)
	#print("O's children: ", board.legalMoveList(turn))
	currentBoard = copy.deepcopy(board)
	(bestValue, bestMove) = miniMaxPruningHelper(_DEPTH, currentBoard, evalFunc, root, turn, -999, 999)
	return bestMove

def miniMaxPruningHelper(depth, board, evalFunc, node, turn, alpha, beta):
	isMax = False
	if (_DEPTH % 2 == depth % 2):
		isMax = True

	if (depth == 0):
		return (node.value, node.name)

	else:
		children = board.legalMoveList(turn)
		if(len(children) > 0):
			#print("Expanding node ", node.name, " at level ", depth)
			for move in children:
				newChildNode = Node(move, node, list(), 0)
				node.insertChild(newChildNode)
				#print("Adding child ", move, "to ", node.name)

			bestMove = (-1, -1)
			if (isMax):
				for child in node.childList:
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, child.name)
					bestValue, move = miniMaxPruningHelper(depth-1, currentBoard, evalFunc, child, turn, alpha, beta)
					if (bestValue > alpha):
						alpha = bestValue
						#print("setting bestMove to", move, " depth: ", depth)
						bestMove = child.name
					if (alpha >= beta):
						return (beta, bestMove)
				return (alpha, bestMove)
			else:
				for child in node.childList:
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, child.name)
					bestValue, move = miniMaxPruningHelper(depth-1, currentBoard, evalFunc, child, turn, alpha, beta)
					if (bestValue < beta):
						beta = bestValue
						#print("setting bestMove to", move, " depth: ", depth)
						bestMove = child.name
					if (beta <= alpha):
						return (alpha, bestMove)
				return (beta, bestMove)
			#print("Changing ", node.name, " bestChild to", bestChild, ", value: ", compareValue)
		else:
			if(isMax):
				node.value = -999
			else:
				node.value = 999
			node.bestChildIndex = -1

