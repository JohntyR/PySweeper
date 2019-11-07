"""Main game loop, handles initialisation of the game window and main game loop"""
import pygame as pg
import utils as ut


def main():
    """Initialisation and main game loop"""
    # init pg, create surface, clock and restart button
    pg.init()
    screen = ut.init_game()
    clock = pg.time.Clock()
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

            # reset mine count, first click, restart button and timer
            mines_left = ut.MINE_COUNT
            first_click = True
            passed_time = 0
            timer_started = False

            restart_btn.is_clicked = False
        # --------------------------Event Queue-----------------------------------------------
        for event in pg.event.get():
            # Exit game if window closed
            if event.type == pg.QUIT:
                running = False
                break

            # Check for clicks
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check for game restart
                restart_btn.is_over = restart_btn.hovered(
                    cur_mouse_pos[0], cur_mouse_pos[1]
                )
                if restart_btn.is_over:
                    restart_btn.clicked()

                # Check for tile click
                for i, tile in enumerate(tile_set):
                    if tile.is_over:
                        # Generate mine sequence where first clicked tile is not a mine
                        if first_click:
                            # Generate mines and set appropriate tiles in tile_set to mines
                            mine_set = ut.generate_mine_sequence(i)
                            for mine_num in mine_set:
                                tile_set[mine_num].make_mine()
                            # Reset first click and start timer
                            first_click = False
                            timer_started = True
                            start_time = pg.time.get_ticks()

                        # Click tile, calculate adj bombs and mine count
                        if event.button == 1 and not tile.is_flagged:
                            # Loop through all applicable tiles and click as necessary
                            tiles_to_be_clicked = [i]
                            j = 0
                            while j < len(tiles_to_be_clicked):
                                # Get an array of indexes that are adjacent to the clicked tile
                                adj_array = ut.adjacent_bomb_count(
                                    tiles_to_be_clicked[j]
                                )

                                # Count how many are mines are in those adjacent tiles
                                mine_count = 0
                                for adj in adj_array:
                                    if tile_set[adj].is_mine:
                                        mine_count += 1
                                # If there are no mines, add all adjacent tiles to be clicked
                                if mine_count == 0:
                                    for adj in adj_array:
                                        if adj not in tiles_to_be_clicked:
                                            tiles_to_be_clicked.append(adj)

                                # Click tile, set mine count or change image to bomb
                                tile_set[tiles_to_be_clicked[j]].clicked(mine_count)

                                j += 1

                        # Flag the tile if right clicked
                        elif event.button == 3:
                            tile.right_clicked()

                            # Decrement mine count if flagged, increment if unflagged
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

        # Create text, get coords and blit the number of mines left
        mines_left_text = ut.generate_mine_counter_text(mines_left)
        mines_left_coords = ut.mines_left_coords(mines_left)
        screen.blit(mines_left_text, mines_left_coords)

        # Increment timer if timer has been started
        if timer_started:
            passed_time = pg.time.get_ticks() - start_time
        # Create text, get coords and blit the timer
        timer_text = ut.generate_timer_text(str(int(passed_time / 1000)))
        timer_coords = ut.timer_coords(str(int(passed_time / 1000)))
        screen.blit(timer_text, timer_coords)

        # ---------------------------draw tiles----------------------------------------------
        for tile in tile_set:
            # Check if tile is being hovered over and change image if yes
            tile.is_over = tile.hovered(cur_mouse_pos[0], cur_mouse_pos[1])
            if not tile.is_clicked and not tile.is_flagged:
                tile.change_image()

            # Display tile images or mine count if tile has been clicked
            if tile.is_clicked and not tile.is_mine:
                tile_text = ut.generate_mine_text(tile.mine_count)
                tile_text_coords = ut.mine_count_coords(tile_text, tile.text_mid_point)
                screen.blit(tile_text, tile_text_coords)
            else:
                screen.blit(tile.img, (tile.x_pos, tile.y_pos))

        # Losing condition: a mine has been clicked - create and blit text, stop timer
        if any((tile.is_mine and tile.is_clicked) for tile in tile_set):
            # Click all tiles
            for i, tile2 in enumerate(tile_set):
                adj_array = ut.adjacent_bomb_count(i)

                mine_count = 0
                for adj in adj_array:
                    if tile_set[adj].is_mine:
                        mine_count += 1

                tile2.clicked(mine_count)

            game_over_text = ut.game_over(True)
            game_over_coords = ut.game_over_coords(game_over_text)
            screen.blit(game_over_text, game_over_coords)
            timer_started = False

        # Winning condition: All mines have been flagged - create and blit text, stop timer
        if not first_click:
            mine_tile_set = [tile for tile in tile_set if tile.is_mine]
            if all(tile.is_flagged for tile in mine_tile_set):
                game_over_text = ut.game_over(False)
                game_over_coords = ut.game_over_coords(game_over_text)
                screen.blit(game_over_text, game_over_coords)
                timer_started = False

        # Refresh screen and set frame rate
        pg.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
