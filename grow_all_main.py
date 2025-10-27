import grow_hay
import grow_wood
import grow_carrot
import grow_pumpkin
import grow_cactus
import grow_sunflower
import grow_till_field

from __builtins__ import *





need_hay_count = 1000000
need_wood_count = 1000000
need_carrot_count = 1000000
need_pumpkin_count = 1000000
need_cactus_count = 1000000
need_power_count = 10000

# set_world_size(10)
# set_execution_speed(5)
while True:
    if num_items(Items.Hay) < need_hay_count:
        print('Hay')
        grow_hay.planting_grass(need_hay_count)

    if num_items(Items.Wood) < need_wood_count:
        print('Wood')
        grow_wood.planting_trees(need_wood_count)

    if num_items(Items.Carrot) < need_carrot_count:
        print('Carrots')
        grow_carrot.planting_carrot(need_carrot_count)

    if num_items(Items.Pumpkin) < need_pumpkin_count:
        print('Pumps')
        clear()
        grow_till_field.go_till()

        grow_pumpkin.grow_pump()

        while num_items(Items.Pumpkin) < need_pumpkin_count:
            get_power()
            if num_items(Items.Carrot) < 1000:
                break
            # pumpv2.second_grow()
            if spawn_drone(grow_pumpkin.harvest_pumps):
                move(East)
    # pumpv2.regrow_dead_pump()
    # pumpv2.harvest_pumps()

    if num_items(Items.Cactus) < need_cactus_count:
        print('Cactus')
        clear()
        grow_till_field.go_till()

        while num_items(Items.Cactus) < need_cactus_count:
            get_power()
            if num_items(Items.Pumpkin) < 1000:
                break

            if spawn_drone(grow_cactus.planting_cactus):
                move(East)

    else:
        need_hay_count *= 10
        need_wood_count *= 10
        need_carrot_count *= 10
        need_pumpkin_count *= 10
        need_cactus_count *= 10
        need_power_count *= 10
