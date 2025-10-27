from __builtins__ import *
import grow_till_field

# clear()
# change_hat(Hats.Traffic_Cone)


def is_even(n):
    return n % 2 == 0


# def go_till():
#     for i in range(get_world_size()):
#         for j in range(get_world_size()):
#             till()
#             move(North)
#         move(East)

# go_till()


# def planting_trees():
#     for i in range(get_world_size()):
#         for j in range(get_world_size()):
#             if get_entity_type() == Entities.Tree:
#                 if can_harvest():
#                     harvest()
#                 use_item(Items.Fertilizer)
#                 use_item(Items.Water)
#             if is_even(get_pos_x()) and not is_even(get_pos_y()):
#                 plant(Entities.Tree)

#             if not is_even(get_pos_x()) and is_even(get_pos_y()):
#                 plant(Entities.Tree)

#             if can_harvest():
#                 harvest()
#             plant(Entities.Sunflower)
#             # use_item(Items.Fertilizer)
#             move(North)
#         move(East)


def drone_task():
    # if get_entity_type() == Entities.Tree:
    #     if can_harvest():
    #         harvest()
    #     use_item(Items.Fertilizer)
    #     use_item(Items.Water)
    for _ in range(get_world_size()):

        if is_even(get_pos_x()) and not is_even(get_pos_y()):
            # if is_even(get_pos_y()):
            if can_harvest():
                harvest()
            plant(Entities.Tree)
            use_item(Items.Fertilizer)
            use_item(Items.Water)

        if not is_even(get_pos_x()) and is_even(get_pos_y()):
            # if not is_even(get_pos_y()):
            if can_harvest():
                harvest()
            plant(Entities.Tree)
            use_item(Items.Fertilizer)
            use_item(Items.Water)
        move(North)

# if get_entity_type() != Entities.Tree:
#     if can_harvest():
#         harvest()
#     plant(Entities.Sunflower)

def planting_trees(need_count):
    clear()
    change_hat(Hats.Traffic_Cone)
    grow_till_field.go_till()
    while num_items(Items.Wood) < need_count:
        if spawn_drone(drone_task):
            move(East)
        else:
            drone_task()

def main():
    print('Wood')
    planting_trees(1000000000)


if __name__ == '__main__':
    main()
