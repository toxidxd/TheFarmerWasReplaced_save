from __builtins__ import *


rightOf = {North: West, West: South, South: East, East: North}
leftOf = {North: East, West: North, South: West, East: South}
oposites = {North: South, East: West, South: North, West: East}

currentDirection = North


def goto(pos, direction, getPos):
    distance = abs(pos - getPos())
    borderDistance = get_world_size() - distance

    moveDirection = direction
    if pos < getPos():  # invert
        moveDirection = oposites[direction]

    if distance > borderDistance:
        moveDirection = oposites[moveDirection]

    while pos != getPos():
        move(moveDirection)


def gotoxy(x, y):
    goto(x, East, get_pos_x)
    goto(y, North, get_pos_y)


def getPoints():
    points = []
    num = max_drones()
    size = get_world_size()

    perLine = 1
    while perLine * perLine < num:
        perLine += 1

    spacing = size // (perLine + 1)

    for i in range(num):
        line = i // perLine
        col = i % perLine

        x = (line + 1) * spacing
        y = (col + 1) * spacing

        points.append((x, y))

    return points


def getRequiredSubstance():
    return get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)


def canSpawnMaze():
    return num_items(Items.Weird_Substance) > getRequiredSubstance()


def spawnMaze():
    if get_ground_type() != Grounds.Grassland:
        till()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, getRequiredSubstance())


def moveAndCheck(direction):
    move(direction)
    if get_entity_type() == Entities.Treasure:
        harvest()
        return True
    return False


def step():
    global currentDirection

    if can_move(rightOf[currentDirection]):
        currentDirection = rightOf[currentDirection]
        return moveAndCheck(currentDirection)

    if can_move(currentDirection):
        return moveAndCheck(currentDirection)

    currentDirection = leftOf[currentDirection]
    return moveAndCheck(currentDirection)


def findTreasure():
    while True:
        if step():
            return


def droneCallback(threshold):
    while num_items(Items.Gold) < threshold and canSpawnMaze():
        findTreasure()
        spawnMaze()
    clear()


def mazeMode(threshold):
    points = getPoints()

    def getcallback(point):
        def callback():
            x, y = point
            gotoxy(x, y)
            droneCallback(threshold)

        return callback

    while len(points) > 1:
        spawn_drone(getcallback(points.pop()))

    for i in range(get_world_size()):
        move(East)

    spawnMaze()
    droneCallback(threshold)

mazeMode(999999999)