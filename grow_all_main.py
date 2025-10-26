import grow_hay
import grow_wood
import grow_carrot
import grow_pumpkin
import grow_cactus
import grow_sunflower
import grow_till_field

from __builtins__ import *

def get_power():
    if num_items(Items.Power) < 1000:
        print('Sunflower')
        clear()
        grow_till_field.go_till()

        while num_items(Items.Power) < need_power_count:
            if num_items(Items.Carrot) < 1000 or num_items(Items.Power) > need_power_count:
                break
            if spawn_drone(grow_sunflower.harvest_column):
                move(East)


need_hay_count = 1000000
need_wood_count = 1000000
need_carrot_count = 1000000
need_pumpkin_count = 1000000
need_cactus_count = 16000000
need_power_count = 10000

# set_world_size(10)
# set_execution_speed(5)
while True:
    if num_items(Items.Hay) < need_hay_count:
        print('Grass')
        clear()
        while num_items(Items.Hay) < need_hay_count:
            get_power()
            # grass.planting_grass()
            if spawn_drone(grow_hay.planting_grass):
                move(East)

    if num_items(Items.Wood) < need_wood_count:
        print('Trees')
        clear()
        grow_till_field.go_till()

        while num_items(Items.Wood) < need_wood_count:
            get_power()
            if spawn_drone(grow_wood.harvest_column):
                move(East)

    if num_items(Items.Carrot) < need_carrot_count:
        print('Carrots')
        clear()
        grow_till_field.go_till()

        while num_items(Items.Carrot) < need_carrot_count:
            get_power()
            if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
                break
            if spawn_drone(grow_carrot.harvest_column):
                move(East)

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
