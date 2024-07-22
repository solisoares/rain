import os
import random
import time
from typing import List

BUFF_HEIGHT = 30
BUFF_WIDTH = 60

ASCII_DROP = "❅️"
RAIN_DENSITY = 1  # 0 -> 100 inclusive
TICK = 0.1

WIND = True

LOG = False

buff = []


def update_buff(buff: List[List], values: List) -> List[List]:
    buff.pop()
    buff.insert(0, values)
    return buff


def print_rain(buff):
    if LOG:
        print(
            f"[LOG] ASCII_DROP:{ASCII_DROP} | RAIN_DENSITY:{RAIN_DENSITY} | TICK:{TICK} | WIND:{WIND}",
            end="",
        )

    # clouds
    print("""
               ⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢛⣛⣛⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿
               ⣪⢿⡿⠿⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⢰⣶⢪⡭⣠⢨⣤⣤⣀⡈⢓⡜⢿⣿⣿⣿⣿⣿⣿
               ⣿⢻⣿⣿⣾⣿⡔⢿⣿⣦⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡀⢴⠊⢠⣶⣦⡰⠻⠻⢿⣻⣿⢿⣿⣬⠻⢿⣿⣿⣿⣿
               ⣿⣾⠿⣻⢟⠟⢻⡆⠿⢿⣶⠿⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣢⣾⢸⣿⣿⣿⣿⣿⣿⣿⣟⣟⣟⣟⠯⠴⡔⢉⠛⠿⠿
               ⣿⣿⣿⣿⠿⣿⣿⣿⣛⢻⣶⣾⣿⡔⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢫⠶⠶⣷⣴⣿⣿⣿⣶⣙⣛⣭⣴⣶⣌⣛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡩⢠⢚⣒⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠿⢿⣷⣷⣷⣿⣷⣶
               ⢃⣿⣿⣿⢃⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣐⣪⠻⣿⣿⠟⢫⠶⠶⣬⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣣⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⡾⣸⣷⣾⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣋⠇⠜⢟⡛⡿⡿
               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠈⣭⣾⣿⣿⡘⣡⣾⢆⣭⣽⣹⣟⠙⢨⢴⣒⠲⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣛⣓⣊⢭⣛⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⡨⢼⢨⢯⢷⢿⣮⠦⠼⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾
               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⡀⠘⠾⢵⣙⣻⣿⡿⢃⣿⣿⣿⣿⣿⣿⢩⡶⠦⢄⢺⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣰⣽⣛⠿⣿⣿⣿⣿⣿⣿⣧⣐⢲⠤⣴⠵⠷⢖⣒⣒⣋⣴⣾⣿⣿⣿⣶⣶⣭⣝⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣬⣭⣭⣭⣭⣭⣴⣶⣿⣿⣿⣿⣿⣿⣿⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣻⣩⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
    # rain
    for line in buff:
        for i in range(0, random.randint(0, 1 if WIND == True else 0)):
            line.insert(0, " ")
            line.pop()
        print(" " * (15), end="")
        for item in line:
            print(item, end=" ")
        print()


while True:
    # TODO: I think this density thing is not well implemented
    current_values = [
        ASCII_DROP if random.randint(0, 100) >= (100 - RAIN_DENSITY) else " "
        for i in range(BUFF_WIDTH)
    ]
    if len(buff) < BUFF_HEIGHT:
        buff.append(current_values)
    else:
        update_buff(buff, current_values)
        os.system("clear")
        print_rain(buff)
        time.sleep(TICK)
