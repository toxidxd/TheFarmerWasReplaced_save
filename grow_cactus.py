from __builtins__ import *


# clear()
# change_hat(Hats.Carrot_Hat)
# pet_the_piggy()
# do_a_flip()
# print(num_items(Items.Carrot))

def planting_cactus():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            plant(Entities.Cactus)
            use_item(Items.Water)
            # use_item(Items.Fertilizer)
            move(North)
        move(East)
