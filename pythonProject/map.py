from settings import *


text_map = [
    '111111111111',
    '1....2.....1',
    '1..222..2..1',
    '12.2....2..1',
    '1..2...22..1',
    '1....2.2...1',
    '1.2..222.2.1',
    '111111111111',
]

mini_map = set()
world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            world_map[(i * tile, j * tile)] = char
            mini_map.add((i * map_tile, j * map_tile))
