# clear()
# change_hat(Hats.Carrot_Hat)
#pet_the_piggy()
#do_a_flip()
# print(num_items(Items.Carrot))

def planting_carrots():
	if can_harvest():
		harvest()
	plant(Entities.Carrot)
	use_item(Items.Water)
	#use_item(Items.Fertilizer)

def harvest_column():
	for _ in range(get_world_size()):
		planting_carrots()
		move(North)

	