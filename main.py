"""Main game loop, handles initialisation of the game window and main game loop"""
import pygame as pg
import utils as ut


def main():
    """Initialisation and main game loop"""
    # init pg and create surface - screen
    pg.init()
    screen = ut.init_game()

    # Create restart button
    restart_btn = ut.add_button()

    # main loop control
    running = True

    # main game loop
    while running:
        # get mouse co-ordinates
        cur_mouse_pos = pg.mouse.get_pos()

        # -------------------------------restart game----------------------------------
        if restart_btn.is_clicked:
            # generate tileset
            tile_set = ut.generate_tiles()

            # reset mine count, first click, restart button
            mines_left = ut.MINE_COUNT
            first_click = True
            restart_btn.is_clicked = False
        # --------------------------event queue-----------------------------------------------
        for event in pg.event.get():
            # exit game if window closed
            if event.type == pg.QUIT:
                running = False
                break

            # check for clicks
            if event.type == pg.MOUSEBUTTONDOWN:
                restart_btn.is_over = restart_btn.hovered(
                    cur_mouse_pos[0], cur_mouse_pos[1]
                )
                if restart_btn.is_over:
                    restart_btn.clicked()

                for i, tile in enumerate(tile_set):
                    if tile.is_over:
                        # Ensure that first tile clicked is not a mine and generate mine sequence
                        if first_click:
                            # generate mines and set mines in tile_set
                            mine_set = ut.generate_mine_sequence(i)
                            for mine_num in mine_set:
                                tile_set[mine_num].make_mine()
                            # first click has now been made
                            first_click = False

                        # click tile, calculate adj bombs and mine count
                        if event.button == 1 and not tile.is_flagged:
                            # create a list of tiles to be clicked
                            # loop through list and calc mine count, and click
                            tiles_to_be_clicked = [i]
                            j = 0
                            while j < len(tiles_to_be_clicked):
                                # get an array of indexes that are adjacent to the clicked tile
                                adj_array = ut.adjacent_bomb_count(
                                    tiles_to_be_clicked[j]
                                )

                                # count how many are mines are in those adjacent tiles
                                mine_count = 0
                                for adj in adj_array:
                                    if tile_set[adj].is_mine:
                                        mine_count += 1

                                if mine_count == 0:
                                    for adj in adj_array:
                                        if adj not in tiles_to_be_clicked:
                                            tiles_to_be_clicked.append(adj)

                                # set tile.is_clicked, set mine count or change image to bomb
                                tile_set[tiles_to_be_clicked[j]].clicked(mine_count)

                                j += 1

                        # flag the tile if right clicked
                        elif event.button == 3:
                            tile.right_clicked()

                            # decrement mine count if flagged, increment if unflagged
                            if tile.is_flagged:
                                mines_left -= 1
                            else:
                                mines_left += 1

        # ---------------------------draw game controls and background-----------------------
        # Screen and tile background
        screen.fill(ut.BACKGROUND_COLOUR)
        ut.draw_tile_background(screen)

        # Blit restart button
        screen.blit(restart_btn.img, (restart_btn.x_pos, restart_btn.y_pos))

        # create text, get coordiantes and blit the number of mines left
        mines_left_text = ut.generate_mine_counter_text(mines_left)
        mines_left_coords = ut.mines_left_coords(mines_left)
        screen.blit(mines_left_text, mines_left_coords)

        # ---------------------------draw tiles----------------------------------------------
        for tile in tile_set:
            # check if tile is being hovered over
            tile.is_over = tile.hovered(cur_mouse_pos[0], cur_mouse_pos[1])

            # change tile image to hover
            if not tile.is_clicked and not tile.is_flagged:
                tile.change_image()

            # display tile images or mine count if already clicked
            if tile.is_clicked and not tile.is_mine:
                tile_text = ut.generate_mine_text(tile.mine_count)
                tile_text_coords = ut.mine_count_coords(tile_text, tile.text_mid_point)
                screen.blit(tile_text, tile_text_coords)
            else:
                screen.blit(tile.img, (tile.x_pos, tile.y_pos))

        # Losing condition - check if a mine has been clicked
        for tile in tile_set:
            if tile.is_mine and tile.is_clicked:
                game_over_text = ut.game_over(True)
                game_over_coords = ut.game_over_coords(game_over_text)
                screen.blit(game_over_text, game_over_coords)
                break

        # Winning condition - check if all mines have been flagged
        if not first_click:
            mine_tile_set = [tile for tile in tile_set if tile.is_mine]
            if all(tile.is_flagged for tile in mine_tile_set):
                game_over_text = ut.game_over(False)
                game_over_coords = ut.game_over_coords(game_over_text)
                screen.blit(game_over_text, game_over_coords)

        # refresh screen
        pg.display.flip()


if __name__ == "__main__":
    main()
