# Reincorment Learning 2020 - Assignment 1: Heuristic Planning
# Auke Bruinsma (s1594443), Meng Yao, Analía Bannura
# This file contains part 3 of the assignment: Search.

# Imports.
import numpy as np
from hex_skeleton import HexBoard
import random as rd

# Global variables
BOARD_SIZE = 4
AI = HexBoard.BLUE
PLAYER = HexBoard.RED

# Initialise the board.
board = HexBoard(BOARD_SIZE)

def minimax(virtual_board,d,mx=True):
	if d <= 0:
		return 2
	elif mx == True:
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if virtual_board.is_empty((i,j)):
					virtual_board.place((i,j),AI)
					minimax(virtual_board,d-1,False)
	elif mx == False:
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if virtual_board.is_empty((i,j)):
					virtual_board.place((i,j),PLAYER)
					minimax(virtual_board,d-1,True)
					
	#virtual_board.print()

def heuristic_eval(board):
	return rd.randint(1,10) # For now, the evaluation function is just a random number.

virtual_board = board
hoi = minimax(virtual_board,1)

print(hoi)

#print(heuristic_val)





