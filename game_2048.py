"""
GAME LOGIC:
1. Table 4 x 4 is created which stores numbers and empty places (as -1)
2. Game starts with one number in random place of the table
3. Program waits till user provide w, a, s or d as direction to move numbers
4. Depenting on direction which user choose, numbers move to last free places and if neightbouring numbers are the same they are added
5. Game ends when user press ESC or if there are no free places in the table and no numbers can be added
"""

import msvcrt
import random
import os
import time


def add_spaces(number: int):
    if number != -1:
        str_number = str(number)
        length = len(str_number)
        if length == 1:
            return "  " + str_number + "   "
        elif length == 2:
            return "  " + str_number + "  "
        elif length == 3:
            return " " + str_number + "  "
        elif length == 4:
            return " " + str_number + " "
    else:
        return "      "
    

def print_game(table: list[list], points: int):
    print(
f"""
2048 GAME (play using WASD)
-----------------------------
|      |      |      |      |
|{add_spaces(table[0][0])}|{add_spaces(table[0][1])}|{add_spaces(table[0][2])}|{add_spaces(table[0][3])}|
|      |      |      |      |
-----------------------------
|      |      |      |      |
|{add_spaces(table[1][0])}|{add_spaces(table[1][1])}|{add_spaces(table[1][2])}|{add_spaces(table[1][3])}|
|      |      |      |      |
-----------------------------
|      |      |      |      |
|{add_spaces(table[2][0])}|{add_spaces(table[2][1])}|{add_spaces(table[2][2])}|{add_spaces(table[2][3])}|
|      |      |      |      |
-----------------------------
|      |      |      |      |
|{add_spaces(table[3][0])}|{add_spaces(table[3][1])}|{add_spaces(table[3][2])}|{add_spaces(table[3][3])}|
|      |      |      |      |
-----------------------------
POINTS: {points}
""")


def get_char():
    while True:
        try:
            x = msvcrt.getch().decode("utf-8")
        except:
            x = ""
        if x == 'w':
            return "up"
        elif x == 'a':
            return "left"
        elif x == 's':
            return "down"
        elif x == 'd':
            return "right"
        elif x == '\x1b':
            return "esc"


def start_table(table: list[list]):
    choices = [2, 4]
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    table[i][j] = random.choice(choices)

    k = random.randint(0, 3)
    l = random.randint(0, 3)
    while k == i and l == j:
        k = random.randint(0, 3)
        l = random.randint(0, 3)

    table[k][l] = random.choice(choices)
    return table


def update_table(table: list[list], arrow: str, points: int):
    if arrow == "up":
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j] != -1:
                    k = i
                    temp = table[k][j]
                    while k > 0:
                        if table[k - 1][j] == -1:
                            table[k - 1][j] = temp
                            table[k][j] = -1
                        elif table[k - 1][j] == temp:
                            table[k - 1][j] = temp * 2 * 11
                            table[k][j] = -1
                            break
                        elif table[k - 1][j] != -1 and table[k - 1][j] != temp:
                            break
                        k -= 1
                        
    elif arrow == "down":
        for i in range(len(table) - 1, -1, -1):
            for j in range(len(table) - 1, -1, -1):
                if table[i][j] != -1:
                    k = i
                    temp = table[k][j]
                    while k < len(table) -1:
                        if table[k + 1][j] == -1:
                            table[k + 1][j] = temp
                            table[k][j] = -1
                        elif table[k + 1][j] == temp:
                            table[k + 1][j] = temp * 2 * 11
                            table[k][j] = -1
                            break
                        elif table[k + 1][j] != -1 and table[k + 1][j] != temp:
                            break
                        k += 1
    
    elif arrow == "left":
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j] != -1:
                    k = j
                    temp = table[i][k]
                    while k > 0:
                        if table[i][k - 1] == -1:
                            table[i][k - 1] = temp
                            table[i][k] = -1
                        elif table[i][k - 1] == temp:
                            table[i][k - 1] = temp * 2 * 11
                            table[i][k] = -1
                            break
                        elif table[i][k - 1] != -1 and table[i][k - 1] != temp:
                            break
                        k -= 1
                        
    elif arrow == "right":
        for i in range(len(table) - 1, -1, -1):
            for j in range(len(table) - 1, -1, -1):
                if table[i][j] != -1:
                    k = j
                    temp = table[i][k]
                    while k < len(table) -1:
                        if table[i][k + 1] == -1:
                            table[i][k + 1] = temp
                            table[i][k] = -1
                        elif table[i][k + 1] == temp:
                            table[i][k + 1] = temp * 2 * 11
                            table[i][k] = -1
                            break
                        elif table[i][k + 1] != -1 and table[i][k + 1] != temp:
                            break
                        k += 1
    
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] % 11 == 0:
                table[i][j] //= 11
                points += table[i][j]
        
    return table, points


def add_element_to_table(table: list[list]):
    choices = [2, 4]
    while True:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if table[i][j] == -1:
            table[i][j] = random.choice(choices)
            break
    
    return table


def check_empty_places(table: list[list]):
    number_of_empty_places = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == -1:
                number_of_empty_places += 1
    return number_of_empty_places


def check_game_over(table: list[list]):
    if check_empty_places(table) == 0:
        for i in range(len(table) - 1):
            for j in range(len(table) - 1):
                if table[i][j] == table [i][j + 1] or table[i][j] == table[i + 1][j]:
                    return False
        return True
    else:
        return False


if __name__ == "__main__":
    
    game_points = 0
    game_table = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]
    
    game_table = start_table(game_table)

    while True:
        os.system("cls")
        print_game(game_table, game_points)

        if check_game_over(game_table):
            print("GAME OVER")
            break
        
        char = get_char()
        
        if char == "esc":
            print("\nGAME OVER\n")
            break
        
        temp = [x[:] for x in game_table]
        game_table, game_points = update_table(game_table, char, game_points)

        while temp == game_table:
            char = get_char()
        
            if char == "esc":
                print("\nGAME OVER\n")
                break
            game_table, game_points = update_table(game_table, char, game_points)
        
        os.system("cls")
        print_game(game_table, game_points)
        
        time.sleep(0.5)
        game_table = add_element_to_table(game_table)
        