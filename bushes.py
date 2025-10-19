from __builtins__ import *

clear()
# pet_the_piggy()
# do_a_flip()
while True:
	for i in range(get_world_size()):

		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Bush)
			move(North)
		move(East)
