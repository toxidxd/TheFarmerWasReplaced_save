from __builtins__ import *

def gen_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def complete_maze():
	ix, dirs = 0, [East, South, West, North]
	while get_entity_type() != Entities.Treasure:
		ix += 1 - move(dirs[ix % 4])*2
	harvest()

while True:
	clear()
	gen_maze()
	complete_maze()
