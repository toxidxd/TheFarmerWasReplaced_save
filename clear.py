from __builtins__ import *
from random_hat import get_random_hat


def drone_task(count=None):
    change_hat(get_random_hat())
    while True:
        if can_harvest():
            harvest()
        plant_type, (x, y) = get_companion()
        move(North)
        if get_pos_y() == y and get_pos_x() == x:
            if can_harvest():
                harvest()
            till()
            if plant_type != Items.Hay:
                plant(plant_type)
        if count and num_items(Items.Hay) > count:
            break


def planting_grass(need_count=0):
    clear()
    # while num_items(Items.Hay) < need_count:
    #     if spawn_drone(drone_task):
    #         move(East)
    #     else:
    #         drone_task(need_count)
    drone_task(need_count)


def main():
    print('Hay')
    planting_grass(10000000000)


if __name__ == '__main__':
    main()
