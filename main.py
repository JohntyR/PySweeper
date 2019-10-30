"""main game module"""
import pygame as pg
from utils import (
    generate_text,
    current_coordinates,
    create_screen,
    generate_tiles,
    generate_mine_sequence,
    game_over,
    game_over_coordinates,
    adjacent_bomb_count,
    generate_mine_count_text,
    mine_count_text_coordinates,
    mines_left_coordinates,
    return_mine_count,
    generate_mines_left_text,
    initialise_game,
)


def main():
    """main game loop"""
    initialise_game()

    # create surface
    screen = create_screen()

    # mines_left
    mines_left = return_mine_count()

    # main loop control
    running = True

    # generate tileset
    tile_set = generate_tiles()

    # generate mines
    mine_set = generate_mine_sequence()

    for mine_num in mine_set:
        tile_set[mine_num].make_mine()

    # main game loop
    while running:
        # get mouse co-ordinates
        current_mouse_pos = pg.mouse.get_pos()

        # event queue
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                for i, tile in enumerate(tile_set):
                    if tile.is_over:
                        if event.button == 1:
                            # get an array of indexes that are adjacent
                            adj_array = adjacent_bomb_count(i)

                            # count how many are mines
                            mine_count = 0
                            for adj in adj_array:
                                if tile_set[adj].is_mine:
                                    mine_count += 1

                            # set tile.is_clicked, set mine count, change image to bomb
                            tile.clicked(mine_count)

                        # flag the tile if right clicked
                        elif event.button == 3:
                            tile.right_clicked()
                            mines_left -= 1

        # draw screen
        screen.fill((0, 0, 0))

        # create and blit text for current mouse co-ordinates
        text = generate_text(current_mouse_pos[0], current_mouse_pos[1])
        text_coords = current_coordinates(current_mouse_pos[0], current_mouse_pos[1])
        screen.blit(text, text_coords)

        # create and blit text for number of mines left
        mines_left_text = generate_mines_left_text(mines_left)
        mines_left_coords = mines_left_coordinates(mines_left)
        screen.blit(mines_left_text, mines_left_coords)

        # draw tiles
        for tile in tile_set:
            # check if tile is being hovered over
            if tile.hovered(current_mouse_pos[0], current_mouse_pos[1]):
                tile.is_over = True
            else:
                tile.is_over = False

            # change tile image to hover
            if not tile.is_clicked and not tile.is_flagged:
                tile.change_image()

            # display tile images or mine count if already clicked
            if tile.is_clicked and not tile.is_mine:
                tile_text = generate_mine_count_text(tile.mine_count)
                tile_text_mid = tile.text_mid_point()
                tile_text_coords = mine_count_text_coordinates(tile_text, tile_text_mid)
                screen.blit(tile_text, (tile_text_coords[0], tile_text_coords[1]))
            else:
                screen.blit(tile.img, (tile.x_pos, tile.y_pos))

        # check if a mine has been clicked
        for tile in tile_set:
            if tile.is_mine and tile.is_clicked:
                running = False
                game_over_text = game_over()
                game_over_coords = game_over_coordinates(game_over_text)
                screen.blit(game_over_text, game_over_coords)
                pg.display.flip()
                pg.time.delay(5000)

        # check if all mines have been flagged
        mine_tile_set = [tile for tile in tile_set if tile.is_mine]
        if all(tile.is_flagged for tile in mine_tile_set):
            running = False
            game_over_text = game_over()
            game_over_coords = game_over_coordinates(game_over_text)
            screen.blit(game_over_text, game_over_coords)
            pg.display.flip()
            pg.time.delay(5000)

        # refresh screen
        pg.display.flip()


if __name__ == "__main__":
    main()
