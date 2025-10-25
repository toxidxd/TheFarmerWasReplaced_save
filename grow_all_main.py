import grow_hay
import grow_wood
import grow_till_field
import grow_carrot
import grow_pumpkin
import grow_cactus

from __builtins__ import *

need_hay_count = 200000
need_wood_count = 200000
need_carrot_count = 100000
need_pumpkin_count = 100000
need_cactus_count = 50000

if num_items(Items.Hay) < need_hay_count:
    print('Hay')
    clear()
    while num_items(Items.Hay) < need_hay_count:
        grow_hay.planting_grass()

if num_items(Items.Wood) < need_wood_count:
    print('Wood')
    clear()
    grow_till_field.go_till()

    while num_items(Items.Wood) < need_wood_count:
        grow_wood.planting_trees()

if num_items(Items.Carrot) < need_carrot_count:
    print('Carrot')
    clear()
    grow_till_field.go_till()

    while num_items(Items.Carrot) < need_carrot_count:
        if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
            break
        grow_carrot.planting_carrots()

if num_items(Items.Pumpkin) < need_pumpkin_count:
    print('Pumpkin')
    clear()
    grow_till_field.go_till()

    grow_pumpkin.grow_pump()

    while num_items(Items.Pumpkin) < need_pumpkin_count:
        if num_items(Items.Carrot) < 100:
            break
        # pumpv2.second_grow()
        grow_pumpkin.regrow_dead_pump()
        grow_pumpkin.harvest_pumps()

if num_items(Items.Cactus) < need_cactus_count:
    print('Cactus')
    clear()
    grow_till_field.go_till()

    while num_items(Items.Cactus) < need_cactus_count:
        if num_items(Items.Pumpkin) < 100:
            break
        grow_cactus.planting_cactus()
