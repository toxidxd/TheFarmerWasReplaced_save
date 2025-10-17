from __builtins__ import *

def planting_sunflowers():
	if can_harvest():
		harvest()
	plant(Entities.Sunflower)
	use_item(Items.Water)
	#use_item(Items.Fertilizer)

def harvest_column():
	for _ in range(get_world_size()):
		planting_sunflowers()
		move(North)

	