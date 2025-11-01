from __builtins__ import *
import grow_till_field


def sort_cactus():
    if measure() > measure(North):
        swap(North)

    if measure() > measure(East):
        swap(East)

    if measure() < measure(South):
        swap(South)

    if measure() < measure(West):
        swap(West)


def drone_task_grow(count=None):
    for _ in range(get_world_size()):
        plant(Entities.Cactus)
        if get_water() < 0.70 and num_items(Items.Water) > 1000:
            use_item(Items.Water)
        move(North)


def drone_task_sort(count=None):
    for _ in range(get_world_size()/2):
        for _ in range(get_world_size()):
            sort_cactus()
            move(North)
        move(East)


def drone_task_harvest(count=None):
    for _ in range(get_world_size()):
        if can_harvest():
            harvest()
        plant(Entities.Cactus)

        if get_water() < 0.70 and num_items(Items.Water) > 1000:
            use_item(Items.Water)

        move(North)


def planting_cactus(need_count=0):
    clear()
    do_a_flip()
    change_hat(Hats.Pumpkin_Hat)
    grow_till_field.go_till()
    while num_items(Items.Cactus) < need_count:
        for _ in range(get_world_size()):
            if spawn_drone(drone_task_grow):
                move(East)
            else:
                drone_task_grow()

        move(East)

        for _ in range(get_world_size()):
            if spawn_drone(drone_task_sort):
                # pass
                move(East)
            else:
                drone_task_sort()

        while num_drones() > 1:
            do_a_flip()

        harvest()

        if num_items(Items.Hay) < 1000 or num_items(Items.Wood) < 1000:
            break


def main():
    # set_world_size(12)
    # set_execution_speed(3)
    print('Cactus')

    change_hat(Hats.Cactus_Hat)
    planting_cactus(1000000000)


if __name__ == '__main__':
    main()
