from const import TILE, MAP_TILE


text_map = [
    '111111111111',
    '1......1...1',
    '111111.....1',
    '1......11111',
    '1.......1..1',
    '1......11..1',
    '1..1.......1',
    '111111111111'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE