import grass
import trees_v2
import go_till
import carrots
import pumpv2
import grow_cactus
import power

from __builtins__ import clear


need_power_count = 20000
need_grass_count = 999999
need_trees_count = 999999
need_carrots_count = 999999
need_pumps_count = 4500000
need_cactus_count = 25000

# set_world_size(16)
# set_execution_speed(10)
while True:
	if num_items(Items.Power) < need_power_count:
		print('Power')
		clear()
		go_till.go_till()

		while num_items(Items.Power) < need_power_count:
			if spawn_drone(power.harvest_column):
				move(East)


	if num_items(Items.Hay) < need_grass_count:
		print('Grass')
		clear()
		while num_items(Items.Hay) < need_grass_count:
			# grass.planting_grass()
			if spawn_drone(grass.planting_grass):
				move(East)


	if num_items(Items.Wood) < need_trees_count:
		print('Trees')
		clear()
		go_till.go_till()

		while num_items(Items.Wood) < need_trees_count:
			if spawn_drone(trees_v2.harvest_column):
				move(East)


	if num_items(Items.Carrot) < need_carrots_count:
		print('Carrots')
		clear()
		go_till.go_till()

		while num_items(Items.Carrot) < need_carrots_count:
			if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
				break
			if spawn_drone(carrots.harvest_column):
				move(East)
			

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