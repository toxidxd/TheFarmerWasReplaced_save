import grass
import trees_v2
import go_till
import carrots
import pumpv2
import grow_cactus

from __builtins__ import clear


need_grass_count = 200000
need_trees_count = 200000
need_carrots_count = 100000
need_pumps_count = 100000
need_cactus_count = 50000


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
		if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
			break
		carrots.planting_carrots()
		

if num_items(Items.Pumpkin) < need_pumps_count:
	print('Pumps')
	clear()
	go_till.go_till()
	
	pumpv2.grow_pump()

	while num_items(Items.Pumpkin) < need_pumps_count:
		if num_items(Items.Carrot) < 100:
			break
		# pumpv2.second_grow()
		pumpv2.regrow_dead_pump()
		pumpv2.harvest_pumps()


if num_items(Items.Cactus) < need_cactus_count:
	print('Cactus')
	clear()
	go_till.go_till()

	while num_items(Items.Cactus) < need_cactus_count:
		if num_items(Items.Pumpkin) < 100:
			break
		grow_cactus.planting_cactus()