from __builtins__ import *


# clear()
# pet_the_piggy()
# do_a_flip()
# while True:

# def planting_grass():
#     for i in range(get_world_size()):
#         for j in range(get_world_size()):
#                 #if can_harvest():
#             harvest()
#             move(North)
#         move(East)
def drone_task():
    for _ in range(get_world_size()):
        harvest()
        move(North)


def planting_grass(need_count=0):
    clear()
    change_hat(Hats.Cactus_Hat)
    while num_items(Items.Hay) < need_count:
        if spawn_drone(drone_task):
            move(East)


def main():
    print('Hay')
    planting_grass(1000000000)

if __name__ == '__main__':
    main()