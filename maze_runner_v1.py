from __builtins__ import *


def gen_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def run_maze():
    ix, dirs = 0, [East, South, West, North]
    while get_entity_type() != Entities.Treasure:
        ix += 1 - move(dirs[ix % 4]) * 2

    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def complete_maze():
    ix, dirs = 0, [East, South, West, North]
    while get_entity_type() != Entities.Treasure:
        ix += 1 - move(dirs[ix % 4]) * 2
    harvest()
    clear()


set_world_size(8)
# set_execution_speed(5)1
clear()
while True:
    gen_maze()

    for i in range(10):
        print(i)
        run_maze()

    complete_maze()
