# This file contains part 6 of the assignment: Iterative Deepening and Transposition Tables

# Imports.
import search 
from hex_skeleton import HexBoard 

# Global variables
BOARD_SIZE = 4
AI = HexBoard.BLUE
PLAYER = HexBoard.RED
EMPTY = HexBoard.EMPTY
INF = 11

# use tt results to transform a tree search algorithms into graph search algorithms
def ttalphabeta(board,d,a,b,mx):
    # d: depth, ttbm: tt-bestmove, g: search value
    (hit, g, ttbm) = lookup(board, d)
    if hit:
        return g
    
    if d <= 0:
        g = heuristic_eval(board)
        bm = (-1,-1) 
    
    elif mx == True:
        g = -INF
        board.virtual_place(ttbm, AI)
        # search for tt-bestmove's children
        # now it's player's turn
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board.is_empty((i,j)):
                    board.virtual_place((i,j),PLAYER)
                    #board.print()
                    g = min(g,alphabeta(board,d-1,a,b,mx=True))
                    b = min(b,g) # Update beta

                    f = open('alphabeta.txt','a')
                    f.write(f'd = {d} g = {g} a = {a} b = {b}\n')
                    f.close()

                    board.make_empty((i,j))
                    #virtual_board.print()
                    if a >= g:
                        break # alpha cutoff

    elif mx == False:
        g = INF
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board.is_empty((i,j)):
                    board.virtual_place((i,j),AI)
                    #board.print()
                    g_optimal = g
                    g = max(g, alphabeta(board,d-1,a,b,mx=False))
                    a = max(a, g) # Update alpha.

                    f = open('alphabeta.txt','a')
                    f.write(f'd = {d} g = {g} a = {a} b = {b}\n')
                    f.close()
                    # only store bestmove when it's AI's turn
                    if g > g_optimal:
                        bm = (i,j)
                    board.make_empty((i,j))
                    if g >= b:
                        break # beta cutoff
    store(board, g, d, bm)
    return g

def iterativedeepening(board,d,a,b,mx=True):
    d = 1
    while not keypressed() and not time_is_up():
        f = ttalphabeta(board,d,a,b,mx=True)
        d = d + 1
    f = open('movelist.txt','a')
    f.write(f'\n{d2l_conversion(bm[0])},{bm[1]}')
    f.close()
    return f
   
    
def lookup(board, d):
    with open('TranspositionTable.txt','r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.split(', ')[0] == board:
                shallow = 0
                if line.split(', ')[2] == d:
                    return True, line.split(', ')[1], line.split(', ')[3]
                # Should we find the bm for the second deepest search??
                # if not hit at this depth , still use tt−bestmove
                else:
                    if line.split(', ')[2] > shallow:
                        shallow = line.split(', ')[2]
                        second_deepest = [False, line.split(', ')[1], line.split(', ')[3]]
    return second_deepest[0], second_deepest[1], second_deepest[2]
                        
def store(board, g, d, bm):
    f = open('TranspositionTable.txt', 'a')
    f.write(f'\n{board}, {g}, {d}, {bm}')
    f.close()









# Digit to letter conversion.
def d2l_conversion(x_coor):
	letter_arr = np.array(['a','b','c','d','e','f','g','h','i','j']) # Max a playfield of 10 by 10.
	return letter_arr[x_coor]

# Letter to digit conversion.
def l2d_conversion(letter):
	letter_arr = np.array(['a','b','c','d','e','f','g','h','i','j'])
	for i in range(len(letter_arr)):
		if letter == letter_arr[i]:
			return i

# Alphabeta search function.
def alphabeta(board,d,a,b,mx=True):
	best_move = (-1,-1) # # Will always be updated.
	if d <= 0:
		return heuristic_eval(board)
	elif mx == True:
		g = -INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.virtual_place((i,j),AI)
					#board.print()
					g_optimal = g
					g = max(g,alphabeta(board,d-1,a,b,mx=False))
					a = max(a,g) # Update alpha.

					f = open('alphabeta.txt','a')
					f.write(f'd = {d} g = {g} a = {a} b = {b}\n')
					f.close()

					if g > g_optimal:
						best_move = (i,j)
					board.make_empty((i,j))
					if g >= b:
						break
	elif mx == False:
		g = INF
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board.is_empty((i,j)):
					board.virtual_place((i,j),PLAYER)
					#board.print()
					g = min(g,alphabeta(board,d-1,a,b,mx=True))
					b = min(b,g) # Update beta

					f = open('alphabeta.txt','a')
					f.write(f'd = {d} g = {g} a = {a} b = {b}\n')
					f.close()

					board.make_empty((i,j))
					#virtual_board.print()
					if a >= g:
						break
	if d == SEARCH_DEPTH:
		f = open('movelist.txt','a')
		f.write(f'\n{d2l_conversion(best_move[0])},{best_move[1]}')
		f.close()
	return g

# Heuristic evaluation function.
def heuristic_eval(board):
	# For now, the evaluation function is just a random number.
	random_number = rd.randint(1,9)
	
	f = open('alphabeta.txt','a')
	f.write(f'rn = {random_number} ')
	f.close()

	return random_number

# The AI makes a move.
def ai_make_move(board):
	with open('movelist.txt','r') as f:
		x = ''; y = ''
		find_x = True
		lines = f.read().splitlines()
		for char in lines[-1]: # Should work for numbers with digits > 1.
			if char == ',':
				find_x = False
			elif find_x == True:
				x += char
			elif find_x == False:				
				y += char
			
		
		move_to_make = (l2d_conversion(x),int(y))
		board.place(move_to_make,AI)
		board.print()

# Player makes a move.
def player_make_move(board):
	print('Next move.')
	x = l2d_conversion(input(' x: '))
	y = int(input(' y: '))
	
	f = open('movelist.txt','a')
	f.write(f'\n{d2l_conversion(x)},{y}')
	f.close()

	board.place((x,y),PLAYER)
	board.print()

# Play the game.
def play_game(board):
	# Make a copy for the search algorithm.
	virtual_board = board

    # Make a text file for the moves.
    f = open('TranspositionTable.txt','w')
    f.write('TT')
    f.close()
   
   	# Make a text file for the transposition table
	f = open('movelist.txt','w')
	f.write('Movelist')
	f.close()

	# Make a text file for the alphabeta algorithm.
	f = open('alphabeta.txt','w')
	f.write('Alphabeta search.')
	f.write(f'\n Board size:   {BOARD_SIZE}')
	f.write(f'\n Search depth: {SEARCH_DEPTH}\n\n')
	f.close()

	while not board.game_over:
		eval_val = alphabeta(virtual_board,d=SEARCH_DEPTH,a=-INF,b=INF)
		ai_make_move(board)
		player_make_move(board)

# Initialise the board.
board = HexBoard(BOARD_SIZE)

# Play the game.
play_game(board)





