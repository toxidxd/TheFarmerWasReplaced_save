from __builtins__ import *

clear()


# def planting_grass():
# 	for i in range(get_world_size()):	
# 		for j in range(get_world_size()):
# 				#if can_harvest():
# 			harvest()
# 			move(North)	
# 		move(East)

# for _ in range(2):
# 	spawn_drone(planting_grass)

# move(East)
def go_till():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            till()
            move(North)
        move(East)


def is_even(n):
    return n % 2 == 0


def planting_trees():
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


# set_world_size(8)
go_till()


def harvest_column():
    for _ in range(get_world_size()):
        planting_trees()
        move(North)


while True:
    if spawn_drone(harvest_column):
        move(East)
