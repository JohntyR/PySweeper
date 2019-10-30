"""testing"""


def adjacent_bomb_count(tile_i):
    """Calculate the number of bombs in the adjacent indexes of specified tile"""
    if tile_i == 0 or tile_i % 10 == 0:
        adjacent_tiles = [-10, -9, 1, 10, 11]
    elif tile_i % 10 == 9:
        adjacent_tiles = [-11, -10, -1, 9, 10]
    else:
        adjacent_tiles = [-11, -10, -9, -1, 1, 9, 10, 11]

    new_adjacent_tiles = [tile_i + x for x in adjacent_tiles if 0 <= tile_i + x <= 99]

    return new_adjacent_tiles


print(f"0: {adjacent_bomb_count(0)}")
print(f"2: {adjacent_bomb_count(2)}")
print(f"10: {adjacent_bomb_count(10)}")
print(f"9: {adjacent_bomb_count(9)}")
print(f"79: {adjacent_bomb_count(79)}")
print(f"98: {adjacent_bomb_count(98)}")
