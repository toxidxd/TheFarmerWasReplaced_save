from __builtins__ import *

# clear()
change_hat(Hats.Traffic_Cone)


def is_even(n):
    return n % 2 == 0


# def go_till():
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			till()
# 			move(North)
# 		move(East)

# go_till()


def planting_trees():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() == Entities.Tree:
                if can_harvest():
                    harvest()
                use_item(Items.Fertilizer)
                use_item(Items.Water)
            if is_even(get_pos_x()) and not is_even(get_pos_y()):
                plant(Entities.Tree)

            if not is_even(get_pos_x()) and is_even(get_pos_y()):
                plant(Entities.Tree)

            if can_harvest():
                harvest()
            plant(Entities.Sunflower)
            # use_item(Items.Fertilizer)
            move(North)
        move(East)
