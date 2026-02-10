# hats = [Hats.Gray_Hat, Hats.Brown_Hat, Hats.Purple_Hat, Hats.Green_Hat, Hats.Straw_Hat]


clear()

WORLD_WIDTH = get_world_size()
WORLD_SIZE = WORLD_WIDTH * WORLD_WIDTH


def get_index(x, y, width):
  return y * width + x
  
def build_square_matrix(width):
	# 6 7 8
	# 3 4 5
	# 0 1 2
	
	# (0,2) (1,2) (2,2)
	# (0,1) (1,1) (2,1)
	# (0,0) (1,0) (2,0)
	
	n = width
	matrix = []
	for i in range(n):
		row = []
		for j in range(n):
			row.append(n * i + j + 1)
		matrix.append(row)
	return matrix
	

	
square_matrix = build_square_matrix(WORLD_WIDTH)
	



SHIFT = ((0,1), (1,0), (0,-1), (-1,0))
direction = 0
x = 0
y = 0

for _ in range(WORLD_SIZE):
	square_matrix[x][y] = 0
	next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
	if (next_x not in range(len(square_matrix))) or (next_y not in range(len(square_matrix))) or (square_matrix[next_x][next_y] == 0):
		direction = (direction + 1) % 4
		next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
	

	diff_x, diff_y = next_x - x, next_y - y
	x, y = next_x, next_y
	
	if (diff_x, diff_y) == SHIFT[0]:
		move(North)
	elif (diff_x, diff_y) == SHIFT[1]:
		move(East)
	elif (diff_x, diff_y) == SHIFT[2]:
		move(South)
	elif (diff_x, diff_y) == SHIFT[3]:
		move(West)
	else:
		# reached the end
		do_a_flip()
