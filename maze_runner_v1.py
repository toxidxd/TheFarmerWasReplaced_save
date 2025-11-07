from __builtins__ import *

# def gen_maze():
#     plant(Entities.Bush)
#     substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
#     use_item(Items.Weird_Substance, substance)
#
# def complete_maze():
#     ix, dirs = 0, [East, South, West, North]
#     while get_entity_type() != Entities.Treasure:
#         # print(move(dirs[ix % 4])*2)
#         ix += 1 - move(dirs[ix % 4])*2
#     harvest()
#
# while True:
#     clear()
#     set_world_size(10)
#     gen_maze()
#     complete_maze()


ALL_DIRECTIONS = [North, South, East, West]


def opposite_direction(direction):
    if direction == North:
        return South
    elif direction == East:
        return West
    elif direction == South:
        return North
    elif direction == West:
        return East


def explore_option(direction):
    if get_entity_type() == Entities.Treasure:
        harvest()
        return True

    if not move(direction):
        return False

    for explore_direction in ALL_DIRECTIONS:
        if opposite_direction(explore_direction) != direction:
            if explore_option(explore_direction):
                return True

    move(opposite_direction(direction))


while True:
    # clear()
    change_hat(Hats.Pumpkin_Hat)
    set_world_size(8)
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    for direction in ALL_DIRECTIONS:
        if explore_option(direction):
            break
