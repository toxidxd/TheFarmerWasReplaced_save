def grow_pump():
	use_item(Items.Water)
	plant(Entities.Pumpkin)		


def second_grow():
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
		use_item(Items.Water)
	elif get_entity_type() == None:
		plant(Entities.Pumpkin)
		use_item(Items.Water)


def regrow_dead_pump():
	no_dead_pumps = 128
	while no_dead_pumps > 2:
		no_dead_pumps = 0

		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			use_item(Items.Water)
			no_dead_pumps += 1
		elif get_entity_type() == None:
			plant(Entities.Pumpkin)
			use_item(Items.Water)


def harvest_pumps():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		plant(Entities.Pumpkin)
		move(North)
		#use_item(Items.Water)


