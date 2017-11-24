import random

#draw grid
#pick random location for player
#pick random location for exit door
#pick random location for monster
#draw player in grid
#take movement input
#move player unless invalid move past edges of grid
#check for win/loss
#clear screen and redraw grid

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
		 (0,1), (1,1), (2,1), (3,1), (4,1),
		 (0,2), (1,2), (2,2), (3,2), (4,2),
		 (0,3), (1,3), (2,3), (3,3), (4,3),
		 (0,4), (1,4), (2,4), (3,4), (4,4)]

def get_locations():
	monster = None
	door = None
	player = None

	return monster, door, player

while True:
	print("Welcome to the dungeon!")
	print("You are currently in room {}") #fill with player position
	print("You can move {}") #fill with available moves
	print("Enter QUIT to quit")

	move = input("> ")
	if move == 'QUIT':
		break

	#good move, change player position
	#bad move dont change
	#on the monster, they lose
	#on door, they win
	#otherwise loop
	