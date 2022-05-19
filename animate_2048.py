'''
This program is to visualise computer choices when simulating 2048 game
'''
import os
import time

import game_2048 as g
from simulate_2048 import *


def simple_animate_2048():
    choices = {
        "choice_1": "up",
        "choice_2": "right",
        "choice_3": "left",
        "choice_4": "down",
    }
    game_points = 0
    game_table = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]

    game_table = g.start_table(game_table)

    while True:
        os.system("cls")
        g.print_game(game_table, game_points)
        time.sleep(0.5)

        if g.check_game_over(game_table):
            break
        
        char = choices["choice_1"]

        temp = [x[:] for x in game_table]
        game_table, game_points = g.update_table(game_table, char, game_points)

        if temp == game_table:
            char = choices["choice_2"]
            game_table, game_points = g.update_table(game_table, char, game_points)

            if temp == game_table:
                char = choices["choice_3"]
                game_table, game_points = g.update_table(game_table, char, game_points)

                if temp == game_table:
                    char = choices["choice_4"]
                    game_table, game_points = g.update_table(game_table, char, game_points)

        os.system("cls")
        g.print_game(game_table, game_points)
        
        time.sleep(0.5)
        game_table = g.add_element_to_table(game_table)


def animate_2048():
    game_points = 0
    game_table = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]

    game_table = g.start_table(game_table)

    while True:
        os.system("cls")
        g.print_game(game_table, game_points)
        time.sleep(.1)

        if g.check_game_over(game_table):
            break
        
        char, pts = determine_best_move(game_table, game_points, depth=2)
        # if input("\nPress Enter to continue"):
        #     pass

        temp = [x[:] for x in game_table]
        game_table, game_points = g.update_table(game_table, char, game_points)

        os.system("cls")
        g.print_game(game_table, game_points)
        
        time.sleep(.5)
        game_table = g.add_element_to_table(game_table)


if __name__ == "__main__":
    animate_2048()