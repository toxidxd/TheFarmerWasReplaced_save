clear()


def move_like_snake(x0, y0, xmax, ymax):
    xnew = get_pos_x() - x0
    ynew = get_pos_y() - y0
    if xnew == 0 and ynew > 0:
        move(South)
    elif ynew % 2 == 0:
        if xnew == xmax - 1:
            move(North)
        else:
            move(East)
    elif xnew == 1 and ynew != ymax - 1:
        move(North)
    else:
        move(West)


def water():
    if get_water() < 0.75:
        use_item(Items.Water)


def ProTill():
    if get_ground_type() != Grounds.Soil:
        till()


def PumpkinIsReady():
    NewMeasure = measure()
    move(East)
    MeasureEnd = measure()
    move(West)
    return NewMeasure == MeasureEnd


def PlantPumpkin():
    while get_entity_type() != Entities.Pumpkin:
        plant(Entities.Pumpkin)
        water()


def Plant_and_water_Pumpkin():
    while get_entity_type() != Entities.Pumpkin:
        plant(Entities.Pumpkin)
        water()
        use_item(Items.Fertilizer)


def Plant_and_fertilize_Pumpkin():
    while get_entity_type() != Entities.Pumpkin:
        plant(Entities.Pumpkin)
        water()
        use_item(Items.Fertilizer)


# go_to new position
def go_to_new_pos(new_pos_x, new_pos_y):
    if new_pos_y > 0:
        for i in range(new_pos_y):
            move(North)
    else:
        for i in range(abs(new_pos_y)):
            move(South)
    if new_pos_x > 0:
        for i in range(new_pos_x):
            move(East)
    else:
        for i in range(abs(new_pos_x)):
            move(West)


# measuring the difference between positions
def measure_pos(x_dead, y_dead, x, y):
    ky = y_dead - y
    kx = x_dead - x
    if kx > 16:
        kx = kx - 32
    elif kx < -16:
        kx = kx + 32
    if ky > 16:
        ky = ky - 32
    elif ky < -16:
        ky = ky + 32
    return kx, ky


WorldSize = get_world_size()
while num_items(Items.Pumpkin) < 2000000000:
    for i in range(WorldSize * WorldSize):
        ProTill()
        PlantPumpkin()
        move_like_snake(0, 0, WorldSize, WorldSize)
    # check dead_pumpkin
    dead_pumpkins = []
    all_pumpkins = True
    for i in range(WorldSize * WorldSize):
        ent = get_entity_type()
        if ent == Entities.Dead_Pumpkin:
            dead_pumpkins.append((get_pos_x(), get_pos_y()))
            PlantPumpkin()
            all_pumpkins = False
        elif ent == Entities.Pumpkin and not can_harvest():
            dead_pumpkins.append((get_pos_x(), get_pos_y()))
            water()
            all_pumpkins = False
        move_like_snake(0, 0, WorldSize, WorldSize)
    # go_to dead_pumpkins and plant
    while get_entity_type() != None:
        y = get_pos_y()
        x = get_pos_x()
        # find near dead_pumpkins but not 0
        for (x_dead, y_dead) in dead_pumpkins:
            if (x, y) != (x_dead, y_dead):
                new_pos_x, new_pos_y = measure_pos(x_dead, y_dead, x, y)
                break
        # go_to new position
        last_pos_x = -new_pos_x
        last_pos_y = -new_pos_y
        if (new_pos_x, new_pos_y) != (0, 0):
            go_to_new_pos(new_pos_x, new_pos_y)
        # checking for dead pumpkins and replanting
        if dead_pumpkins != []:
            ent = get_entity_type()
            if ent == Entities.Dead_Pumpkin:
                Plant_and_fertilize_Pumpkin()
            elif not can_harvest() and ent == Entities.Pumpkin:
                water_more()
            elif can_harvest() and ent == Entities.Pumpkin and (get_pos_x(), get_pos_y()) in dead_pumpkins:
                dead_pumpkins.remove((get_pos_x(), get_pos_y()))
            elif ent == None:
                break
        else:
            harvest()