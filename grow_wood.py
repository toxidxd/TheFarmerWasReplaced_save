from __builtins__ import *
import grow_till_field
from random_hat import get_random_hat


def is_even(n):
    return n % 2 == 0


def drone_task(count = None):
    change_hat(get_random_hat())

    while True:

        if is_even(get_pos_x()) and not is_even(get_pos_y()):
            if get_water() < 0.70 and num_items(Items.Water) > 1000:
                use_item(Items.Water)
            if can_harvest():
                harvest()
            plant(Entities.Tree)
            plant_type, (x, y) = get_companion()
            move(North)
            if get_pos_y() == y and get_pos_x() == x:
                if can_harvest():
                    harvest()
                plant(plant_type)
            # use_item(Items.Fertilizer)


        elif not is_even(get_pos_x()) and is_even(get_pos_y()):
            if get_water() < 0.70 and num_items(Items.Water) > 1000:
                use_item(Items.Water)
            if can_harvest():
                harvest()
            plant(Entities.Tree)
            plant_type, (x, y) = get_companion()
            move(North)
            if get_pos_y() == y and get_pos_x() == x:
                if can_harvest():
                    harvest()
                plant(plant_type)
            # use_item(Items.Fertilizer)

        if count and num_items(Items.Wood) > count:
            break
        if get_water() < 0.70 and num_items(Items.Water) > 1000:
            use_item(Items.Water)
        move(North)


def planting_trees(need_count):
    clear()
    change_hat(Hats.Traffic_Cone)
    grow_till_field.go_till()
    while num_items(Items.Wood) < need_count:
        if spawn_drone(drone_task):
            move(East)
        else:
            drone_task(need_count)


def main():
    print('Wood')
    planting_trees(10000000000)


if __name__ == '__main__':
    main()
