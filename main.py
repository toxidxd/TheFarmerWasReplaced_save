import grass
import wood
import till_field
import carrot
import pumpkin
import cactus
import power

from __builtins__ import *

need_power_count = 20000
need_grass_count = 10000000
need_trees_count = 10000000
need_carrots_count = 1000000000
need_pumps_count = 10000000
need_cactus_count = 15000000

# set_world_size(10)
# set_execution_speed(5)
while True:
    if num_items(Items.Power) < need_power_count:
        print('Power')
        clear()
        till_field.go_till()

        while num_items(Items.Power) < need_power_count:
            if num_items(Items.Carrot) < 1000:
                break
            if spawn_drone(power.harvest_column):
                move(East)

    if num_items(Items.Hay) < need_grass_count:
        print('Grass')
        clear()
        while num_items(Items.Hay) < need_grass_count:
            # grass.planting_grass()
            if spawn_drone(grass.planting_grass):
                move(East)

    if num_items(Items.Wood) < need_trees_count:
        print('Trees')
        clear()
        till_field.go_till()

        while num_items(Items.Wood) < need_trees_count:
            if spawn_drone(wood.harvest_column):
                move(East)

    if num_items(Items.Carrot) < need_carrots_count:
        print('Carrots')
        clear()
        till_field.go_till()

        while num_items(Items.Carrot) < need_carrots_count:
            if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
                break
            if spawn_drone(carrot.harvest_column):
                move(East)

    if num_items(Items.Power) < need_power_count:
        print('Power')
        clear()
        till_field.go_till()

        while num_items(Items.Power) < need_power_count:
            if num_items(Items.Carrot) < 1000:
                break
            if spawn_drone(power.harvest_column):
                move(East)

    if num_items(Items.Pumpkin) < need_pumps_count:
        print('Pumps')
        clear()
        till_field.go_till()

        pumpkin.grow_pump()

        while num_items(Items.Pumpkin) < need_pumps_count:
            if num_items(Items.Carrot) < 1000:
                break
            # pumpv2.second_grow()
            if spawn_drone(pumpkin.harvest_pumps):
                move(East)
        # pumpv2.regrow_dead_pump()
        # pumpv2.harvest_pumps()

    if num_items(Items.Power) < need_power_count:
        print('Power')
        clear()
        till_field.go_till()

        while num_items(Items.Power) < need_power_count:
            if num_items(Items.Carrot) < 1000:
                break

            if spawn_drone(power.harvest_column):
                move(East)

    if num_items(Items.Cactus) < need_cactus_count:
        print('Cactus')
        clear()
        till_field.go_till()

        while num_items(Items.Cactus) < need_cactus_count:
            if num_items(Items.Pumpkin) < 1000:
                break

            if spawn_drone(cactus.planting_cactus):
                move(East)
