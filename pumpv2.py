def grow_pump():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			use_item(Items.Water)
			plant(Entities.Pumpkin)		
			move(North)	
		move(East)

def second_grow():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
				use_item(Items.Water)
			elif get_entity_type() == None:
				plant(Entities.Pumpkin)
				use_item(Items.Water)
			move(North)
		move(East)

def regrow_dead_pump():
	no_dead_pumps = 128
	while no_dead_pumps > 2:
		no_dead_pumps = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					use_item(Items.Water)
					no_dead_pumps += 1
				elif get_entity_type() == None:
					plant(Entities.Pumpkin)
					use_item(Items.Water)
				move(North)
			move(East)

def harvest_pumps():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			#use_item(Items.Water)
			move(North)
		move(East)

