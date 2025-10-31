from __builtins__ import *
import grow_till_field


def drone_task(count=None):
    change_hat(Hats.Pumpkin_Hat)

    while True:
        if count and num_items(Items.Pumpkin) > count:
            break

        if num_items(Items.Carrot) < 1000:
            break

        for _ in range(get_world_size() * 3):
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
            elif get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)

            if get_water() < 0.70 and num_items(Items.Water) > 1000:
                use_item(Items.Water)

            move(North)

        for _ in range(get_world_size()):
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
            elif can_harvest():
                harvest()
                plant(Entities.Pumpkin)

            if get_water() < 0.70 and num_items(Items.Water) > 1000:
                use_item(Items.Water)

            move(North)


def planting_pumpkin(need_count=0):
    harvest()
    clear()
    grow_till_field.go_till()
    while num_items(Items.Pumpkin) < need_count:
        if spawn_drone(drone_task):
            move(East)
        else:
            drone_task(need_count)
        if num_items(Items.Carrot) < 1000:
            break


def main():
    print('Pumpkin')
    planting_pumpkin(1000000000)


if __name__ == '__main__':
    main()
