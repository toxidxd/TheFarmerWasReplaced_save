from __builtins__ import *
import grow_till_field


def drone_task():
    change_hat(Hats.Pumpkin_Hat)
    dead = 0

    while True:
        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
        elif get_entity_type() == Entities.Dead_Pumpkin:
            plant(Entities.Pumpkin)
            dead += 1

        if get_water() < 0.70 and num_items(Items.Water) > 1000:
            use_item(Items.Water)


        move(North)


def planting_pumpkin(need_count=0):
    clear()
    grow_till_field.go_till()
    while num_items(Items.Pumpkin) < need_count:
        if spawn_drone(drone_task):
            move(East)
        else:
            drone_task()


def main():
    print('Pumpkin')
    planting_pumpkin(1000000000)


if __name__ == '__main__':
    main()
