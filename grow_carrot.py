from __builtins__ import *
import grow_till_field


def drone_task():
    for _ in range(get_world_size()):
        if can_harvest():
            harvest()
        plant(Entities.Carrot)
        use_item(Items.Water)
        move(North)


def planting_carrot(need_count=0):
    clear()
    change_hat(Hats.Cactus_Hat)
    grow_till_field.go_till()
    while num_items(Items.Carrot) < need_count:
        if spawn_drone(drone_task):
            move(East)


def main():
    print('Carrot')
    planting_carrot(1000000000)


if __name__ == '__main__':
    main()
