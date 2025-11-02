from __builtins__ import *
import grow_till_field
from random_hat import get_random_hat


def drone_task():
    # for _ in range(get_world_size()):
    change_hat(get_random_hat())
    while True:
        # if can_harvest():
        harvest()
        plant(Entities.Sunflower)
        if get_water() < 0.70 and num_items(Items.Water) > 1000:
            use_item(Items.Water)
        move(North)


def planting_sunflower(need_count=0):
    clear()
    change_hat(Hats.Sunflower_Hat)
    grow_till_field.go_till()
    while num_items(Items.Power) < need_count:
        if spawn_drone(drone_task):
            move(East)
        else:
            drone_task()


def main():
    print('Sunflower')
    planting_sunflower(1000000000)


if __name__ == '__main__':
    main()
