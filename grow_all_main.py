import grow_hay
import grow_wood
import grow_carrot
import grow_pumpkin
import grow_cactus
import grow_till_field

from __builtins__ import *

need_hay_count = 1000000
need_wood_count = 1000000
need_carrot_count = 1000000
need_pumpkin_count = 1000000
need_cactus_count = 100000
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
        print(need_carrot_count)
        grow_carrot.planting_carrot(need_carrot_count)

    if num_items(Items.Pumpkin) < need_pumpkin_count:
        print('Pumpkin')
        grow_pumpkin.planting_pumpkin(need_pumpkin_count)

    if num_items(Items.Cactus) < need_cactus_count:
        print('Cactus')
        grow_till_field.go_till()
        grow_cactus.planting_cactus(need_cactus_count)

    else:
        need_hay_count *= 1.2
        need_wood_count *= 1.2
        need_carrot_count *= 1.2
        need_pumpkin_count *= 1.2
        need_cactus_count *= 1.2
        need_power_count *= 1.2
