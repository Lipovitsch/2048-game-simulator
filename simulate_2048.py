'''
Simulation of 2048 game. File contains:
- simple_simulate_2048 method, which is just simple simulation based on static choices
- simulate_2048 method, which is advances simulation with recursive function which looks to forward moves

Simulation prints results as three plots. First plot represents max number (e.g. 2048) from each game, 
second plot represents number of points from game and the last plot is the same as first plot but as bar chart.
'''
import time
import matplotlib.pyplot as plt
import game_2048 as g


def simple_simulate_2048():
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

        game_table = g.add_element_to_table(game_table)
    
    return game_table, game_points


def determine_best_move(table: list[list], points, depth: int = 1):
    if depth == 0:
        return "", points

    choices = ["right", "up", "left", "down"]
    best_choice = ""
    hold_points = points
    illegal_move_counter = 0
    for choice in choices:
        if choice == "down" and illegal_move_counter != 3:
            continue

        if choice == "left" and illegal_move_counter != 2:
            same_number = False
            for j in range(len(table) - 1):
                if table[0][j] == table [0][j + 1]:
                    same_number = True
            if -1 in table[0] or same_number:
                continue

        temp = [x[:] for x in table]
        new_table, new_points = g.update_table([x[:] for x in table], choice, points)
        if temp == new_table:
            illegal_move_counter += 1
            continue
        else:
            # print(f"\n------------------- Choice: {choice} -------------------", end="")
            # g.print_game(new_table, new_points)
            bc, new_points = determine_best_move([x[:] for x in new_table], new_points, depth - 1)

            if new_table[0][0] <= new_table[0][1] and new_table[0][1] <= new_table[0][2] and new_table[0][2] <= new_table[0][3]:
                new_points += 100000
            if sum(new_table[0]) > sum(new_table[1]) + sum(new_table[2]) + sum(new_table[3]):
                new_points += 100000

            # if new_table[0][0] <= new_table[0][1]:
            #     new_points += 100000
            #     if new_table[0][1] <= new_table[0][2]:
            #         new_points += 100000
            #         if new_table[0][2] <= new_table[0][3]:
            #             new_points += 100000
            #             if new_table[1][0] <= new_table[0][3]:
            #                 new_points += 100000
            #                 if new_table[1][0] <= new_table[0][3]:
            #                     new_points += 100000    
            #                     if new_table[1][1] <= new_table[1][0]:
            #                         new_points += 100000
            #                         if new_table[1][1] <= new_table[1][2]:
            #                             new_points += 100000
            #                             if new_table[1][2] <= new_table[1][3]:
            #                                 new_points += 100000

            if new_points >= hold_points:
                hold_points = new_points
                best_choice = choice

    # print(f"Choose: {best_choice.upper()}")    
    return best_choice, hold_points


def simulate_2048(depth: int):
    game_points = 0
    game_table = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]

    game_table = g.start_table(game_table)

    while True:
        if g.check_game_over(game_table):
            break
        
        char, pts = determine_best_move([x[:] for x in game_table], game_points, depth)
        temp = [x[:] for x in game_table]
        game_table, game_points = g.update_table([x[:] for x in game_table], char, game_points)
        game_table = g.add_element_to_table([x[:] for x in game_table])
    
    return game_table, game_points


if __name__ == "__main__":
    # --- PARAMETERS ---
    n = 100
    depth = 2
    # ------------------

    max_results = []
    points_table = []

    for _ in range(n):
        table, points = simulate_2048(depth)
        max_from_each_table = [max(t) for t in table]
        max_results.append(max(max_from_each_table))
        points_table.append(points)
        # if (max(max_from_each_table) == 64):
        #     g.print_game(table, points)
    
    number_max_results = {}
    for i in range(3, 13):
        number_max_results[f"{2 ** i}"] = max_results.count(2 ** i)

    n_plot = range(1, n + 1)

    plt.figure(1, figsize=(15, 9))

    plt.subplot(311)
    plt.yscale('log', base=2)
    plt.scatter(n_plot, max_results)
    plt.title("Max values from games")

    plt.subplot(312)
    plt.scatter(n_plot, points_table)
    plt.title("Points from game")
    
    plt.subplot(313)
    plt.bar(list(number_max_results.keys()), list(number_max_results.values()))
    plt.title("Max values from games")

    plt.show()
    