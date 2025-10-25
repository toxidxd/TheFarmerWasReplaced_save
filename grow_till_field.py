from __builtins__ import *


def go_till():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            till()
            move(North)
        move(East)
