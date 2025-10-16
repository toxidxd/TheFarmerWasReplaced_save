import grass
import trees_v2
import go_till
import carrots
from __builtins__ import clear

need_grass_count = 32000
need_trees_count = 32000
need_carrots_count = 32000

if num_items(Items.Hay) < need_grass_count:
	print('Grass')
	clear()
	while num_items(Items.Hay) < 32000:
		grass.planting_grass()


if num_items(Items.Wood) < need_trees_count:
	print('Trees')
	clear()
	go_till.go_till()

	while num_items(Items.Wood) < 32000:
		trees_v2.planting_trees()


if num_items(Items.Carrot) < need_carrots_count:
	print('Carrots')
	clear()
	go_till.go_till()

	while num_items(Items.Carrot) < 32000:
		print('Carrots')
		carrots.planting_carrots()