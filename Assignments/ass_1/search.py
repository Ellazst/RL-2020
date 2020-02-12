# Reincorment Learning 2020 - Assignment 1: Heuristic Planning
# Auke Bruinsma (s1594443), Meng Yao, Analía Bannura
# This file contains part 3 of the assignment: Search.

# Imports.
import numpy as np
from hex_skeleton import HexBoard
import random as rd
import sys 

# Global variables
BOARD_SIZE = 8
AI = HexBoard.BLUE
PLAYER = HexBoard.RED
EMPTY = HexBoard.EMPTY
INF = 99999

# Since alphabeta is sort of an upgraded minimax function, we decided to
# first implement this algorithm, and if that succeeds, go to alphabeta.
def minimax(board,d,mx=True):
	best_move = (-1,-1) # Will always be updated.
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),AI)
					board.print()
					g_optimal = g
					g = max(g,minimax(board,d-1,False)[0])
					if g > g_optimal:
						best_move = (i,j)
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
	return g,best_move

def alphabeta(board,d,a,b,mx=True):
	best_move = (-1,-1) # # Will always be updated.
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),AI)
					#board.print()
					g_optimal = g
					g = max(g,alphabeta(board,d-1,a,b,mx=False))
					a = max(a,g) # Update alpha.
					if g > g_optimal:
						best_move = (i,j)
					board.make_empty((i,j))
					#virtual_board.print()
					if g >= b:
						break
	elif mx == False:
		g = INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.place((i,j),PLAYER)
					#board.print()
					g = min(g,alphabeta(board,d-1,a,b,mx=True))
					b = min(b,g) # Update beta
					board.make_empty((i,j))
					#virtual_board.print()
					if a >= g:
						break
	if d == search_depth:
		f = open('movelist.txt','w')
		f.write(f'{best_move[0]},{best_move[1]}')
		f.close()
	return g


def heuristic_eval(board):
	# For now, the evaluation function is just a random number.
	random_number = rd.randint(1,10)
	#print(random_number)
	return random_number

def ai_make_move(board):
	with open('movelist.txt','r') as f:
		x = ''; y = ''
		find_x = True
		lines = f.read().splitlines()
		for char in lines[-1]: # Should work for numbers with digits > 1.
			if char == ',':
				find_x = False
			elif find_x == False:
				y += char
			elif find_x == True:
				x += char
		
		move_to_make = (int(x),int(y))
		board.place(move_to_make,AI)
		board.print()

def player_make_move(board):
	print('Next move.')
	x = int(input(' x: '))
	y = int(input(' y: '))

	f = open('movelist.txt','w')
	f.write(f'{x},{y}')
	f.close()

	board.place((x,y),PLAYER)
	board.print()

def play_game(board):
	# Make a copy for the search algorithm.
	virtual_board = board

	while not board.game_over:
		eval_val = alphabeta(virtual_board,d=search_depth,a=-INF,b=INF)
		ai_make_move(board)
		player_make_move(board)




# Initialise the board.
board = HexBoard(BOARD_SIZE)

# Play the game.
search_depth = 2
play_game(board)



# Apply the minimax algorithm.
#eval_val,best_move = minimax(virtual_board,search_depth)

# Apply the alphabeta algorithm
#eval_val = alphabeta(virtual_board,d=search_depth,a=-INF,b=INF)
#print(eval_val)
#ai_make_move(board)

#player_make_move(board)






