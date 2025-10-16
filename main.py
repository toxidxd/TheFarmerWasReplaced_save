import grass
import trees_v2
import go_till
import carrots
import pumpv2
from __builtins__ import clear

need_grass_count = 32000
need_trees_count = 32000
need_carrots_count = 15000
nees_pumps_count = 64000

if num_items(Items.Hay) < need_grass_count:
	print('Grass')
	clear()
	while num_items(Items.Hay) < need_grass_count:
		grass.planting_grass()


if num_items(Items.Wood) < need_trees_count:
	print('Trees')
	clear()
	go_till.go_till()

	while num_items(Items.Wood) < need_trees_count:
		trees_v2.planting_trees()


if num_items(Items.Carrot) < need_carrots_count:
	print('Carrots')
	clear()
	go_till.go_till()

	while num_items(Items.Carrot) < need_carrots_count:
		carrots.planting_carrots()


if num_items(Items.Pumpkin) < nees_pumps_count:
	print('Pumps')
	clear()
	go_till.go_till()
	
	pumpv2.grow_pump()

	while num_items(Items.Pumpkin) < nees_pumps_count:
		# pumpv2.second_grow()
		pumpv2.regrow_dead_pump()
		pumpv2.harvest_pumps()
