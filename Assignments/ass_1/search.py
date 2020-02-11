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

'''
virtual_board = board
search_depth = 1

def minimax(board,d,mx=True):
	if d <= 0:
		return 'Hey!'
	else:
		d -= 1
		print(d)
		return minimax(board,d)

hoi = minimax(virtual_board,search_depth,)
print(hoi)

'''
def minimax(board,d,mx=True):
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),AI)
					board.print()
					g = max(g,minimax(board,d-1,False))
					board.make_empty((i,j))
					print(f'Depth: {d}. Max: {g}')
	elif mx == False:
		g = INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j,),PLAYER)
					board.print()
					g = min(g,minimax(board,d-1,True))
					board.make_empty((i,j))
					print(f'Depth {d} Min: {g}')
	return g


def heuristic_eval(board):
	# For now, the evaluation function is just a random number.
	random_number = rd.randint(1,10)
	print(random_number)
	return random_number 

# Initialise the board.
board = HexBoard(BOARD_SIZE)

# Make a copy for the search algorithm.
virtual_board = board

# Apply the minimax algorithm.
search_depth = 2
eval_val = minimax(virtual_board,search_depth)

print("")
print(eval_val)
print("")