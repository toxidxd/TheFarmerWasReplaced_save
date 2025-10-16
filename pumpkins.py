clear()
change_hat(Hats.Wizard_Hat)
#pet_the_piggy()
#do_a_flip()
print(num_items(Items.Hay))
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)		
		move(North)	
	move(East)
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			use_item(Items.Water)
			move(North)
		move(East)
	