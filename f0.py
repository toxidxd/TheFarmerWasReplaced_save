set_world_size(3)
while True:
    for i in range(get_world_size()):
        if get_ground_type() == Grounds.Rice_Terrace:
            harvest()
        # Прыжок неточен: выкопай оставшиеся блоки
        while get_ground_type() != Grounds.Clay:
            dig()
    
        plant(Entities.Rice)
    
        move(East)