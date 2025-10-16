clear()
#pet_the_piggy()
#do_a_flip()
while True:
	for i in range(get_world_size()):
		#move(North)
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Tree)
			use_item(Items.Water)
			move(North)	
			#if can_harvest():
			#	harvest()
			#move(North)
		move(East)
		move(East)