clear()
change_hat(Hats.Wizard_Hat)
#print(num_items(Items.Hay))
#pet_the_piggy()
do_a_flip()

def grow_pump():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
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

def harvest_pumps():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			use_item(Items.Water)
			move(North)
		move(East)

grow_pump()

while True:
	second_grow()
	harvest_pumps()
	
	
#pet_the_piggy()
#do_a_flip()
