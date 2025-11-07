from __builtins__ import *


def hat_flip():
    # clear()
    change_hat(Hats.Pumpkin_Hat)
    change_hat(Hats.Dinosaur_Hat)


def move_to_x(new_x):
    x_curr = get_pos_x()
    moves_needed = new_x - x_curr
    if moves_needed > 0:
        dir = East
    else:
        dir = West
    for _ in range(abs(moves_needed)):
        if not move(dir):
            hat_flip()


def move_to_y(new_y):
    y_curr = get_pos_y()
    moves_needed = new_y - y_curr
    if moves_needed > 0:
        dir = North
    else:
        dir = South
    for _ in range(abs(moves_needed)):
        if not move(dir):
            hat_flip()


def main():
    set_world_size(16)
    # set_execution_speed(3)
    do_a_flip()
    change_hat(Hats.Dinosaur_Hat)
    while True:
        target_x, target_y = measure()


        move_to_x(target_x)
        move_to_y(target_y)

        if get_entity_type() != Entities.Apple:
            hat_flip()


if __name__ == '__main__':
    main()
