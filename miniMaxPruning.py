from minimaxTree import *
from Board import Board
import copy

_DEPTH = 6
evals = 0
cutoffs = 0
bn = 0
bd = 0


def evalFunc(turn, board):
	opponent = 'X'
	if (turn == 'X'):
		opponent = 'O'
	return (len(board.legalMoveList(turn)) - len(board.legalMoveList(opponent)))

def miniMaxPruning(board, evalFunc, turn):
	root = Node((-1, -1), None, list(), -1)
	currentBoard = copy.deepcopy(board)
	(bestValue, bestMove) = miniMaxPruningHelper(_DEPTH, currentBoard, evalFunc, root, turn, -999, 999)
	return bestMove

def miniMaxPruningHelper(depth, board, evalFunc, node, turn, alpha, beta):
	global evals, cutoffs, bn, bd
	isMax = False
	if (_DEPTH % 2 == depth % 2):
		isMax = True

	if (depth == 0):
		node.value = evalFunc(turn, board)
		evals += 1
		return (node.value, node.name)

	else:
		children = board.legalMoveList(turn)
		if(len(children) > 0):
			bn += len(children)
			bd += 1
			for move in children:
				newChildNode = Node(move, node, list(), 0)
				node.insertChild(newChildNode)

			bestMove = (-1, -1)
			if (isMax):
				for child in node.childList:
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, child.name)
					(bestValue, move) = miniMaxPruningHelper(depth-1, currentBoard, evalFunc, child, turn, alpha, beta)
					if (bestValue > alpha):
						alpha = bestValue
						bestMove = child.name
					if (alpha >= beta):
						cutoffs += 1
						return (beta, bestMove)
				return (alpha, bestMove)
			else:
				for child in node.childList:
					currentBoard = copy.deepcopy(board)
					currentBoard.updateBoard(turn, child.name)
					(bestValue, move) = miniMaxPruningHelper(depth-1, currentBoard, evalFunc, child, turn, alpha, beta)
					if (bestValue < beta):
						beta = bestValue
						bestMove = child.name
					if (beta <= alpha):
						cutoffs += 1
						return (alpha, bestMove)
				return (beta, bestMove)
		else:
			if(isMax):
				return (-999, (-1, -1))
			else:
				return (-999, (-1, -1))


def feedBack():
	print "Evaluation function was applied: ", evals, " times"
	print "There are ", cutoffs, " cutoffs"
	print "The average branching factor is: ", float(bn)/bd