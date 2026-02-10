
WIDTH = get_world_size()
while True:
	for _ in range(WIDTH):
		move(North)
		if not can_harvest():
			plant(Entities.Carrot)
				
		else:
			harvest()
			till()
			plant(Entities.Carrot)
			#plant(Entities.Bush)
	
	move(East)	
	
	