#clear()
#pet_the_piggy()
#do_a_flip()
#while True:

# def planting_grass():
# 	for i in range(get_world_size()):	
# 		for j in range(get_world_size()):
# 				#if can_harvest():
# 			harvest()
# 			move(North)	
# 		move(East)


def planting_grass():
	for _ in range(get_world_size()):
		harvest()
		move(North)

