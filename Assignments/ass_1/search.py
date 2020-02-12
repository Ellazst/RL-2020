# Reincorment Learning 2020 - Assignment 1: Heuristic Planning
# Auke Bruinsma (s1594443), Meng Yao, Analía Bannura
# This file contains part 3 of the assignment: Search.

# Imports.
import numpy as np
from hex_skeleton import HexBoard
import random as rd
import sys 

# Global variables
BOARD_SIZE = 2
AI = HexBoard.BLUE
PLAYER = HexBoard.RED
EMPTY = HexBoard.EMPTY
INF = 99999

def minimax(board,d,mx=True):
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),AI)
					#board.print()
					g = max(g,minimax(board,d-1,False))
					board.make_empty((i,j))
					print(f'Depth: {d}. Max: {g}')
	elif mx == False:
		g = INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j,),PLAYER)
					#board.print()
					g = min(g,minimax(board,d-1,True))
					board.make_empty((i,j))
					print(f'Depth {d} Min: {g}')
	return g

def alphabeta(board,d,a,b,mx=True):
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),AI)
					board.print()
					g = max(g,alphabeta(board,d-1,a,b,mx=False))
					a = max(a,g) # Update alpha.
					board.make_empty((i,j))
					if g >= b:
						break
	elif mx == False:
		g = INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),PLAYER)
					board.print()
					g = min(g,alphabeta(board,d-1,a,b,mx=True))
					b = min(b,g) # Update beta
					board.make_empty((i,j))
					if a >= g:
						break

	return g


def heuristic_eval(board):
	# For now, the evaluation function is just a random number.
	random_number = rd.randint(1,10)
	#print(random_number)
	return random_number 

# Initialise the board.
board = HexBoard(BOARD_SIZE)

# Make a copy for the search algorithm.
virtual_board = board

# Apply the minimax algorithm.
search_depth = 2
#eval_val = minimax(virtual_board,search_depth)

# Apply the alphabeta algorithm
eval_val = alphabeta(virtual_board,d=search_depth,a=-INF,b=INF)

