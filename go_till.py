def till_column():
	for _ in range(get_world_size()):
		till()
		move(North)
	
	


def go_till():
	while True:
		# for _ in range(get_world_size()):
		# print(get_world_size())
		# print('Tilling column')
		if spawn_drone(till_column):
			quick_print(get_pos_x())
			move(East)
		if get_pos_x() == 0:
			print('Finished tilling')
			break
