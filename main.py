import csv
import os
import random
import sys
import time
def afisa(file):
    f = open(file, 'r')
    x = csv.reader(f)
    karta = []
    for line in x:
        karta.append(line)
    return karta

def beautiful_view(m, map):
    time.sleep(0.5)
    m2 = m[:]
    os.system('cls')
    for item in map:
        m2[item[0]][item[1]] = "."
    m2[map[-1][0]][map[-1][1]] = "M"
    draw = " "
    for row in m2:
        for i in row:
            i = str(i).replace("1", "█")
            i = str(i).replace("0", " ")
            draw = draw + i
        draw = draw + "\n"
    print(draw)

def move(character):
    beautiful_view(labirint, character)
    a = character[-1]
    possibility = [(a[0], a[1]+1), (a[0], a[1]-1), (a[0]+1, a[1]), (a[0]-1, a[1])]
    random.shuffle(possibility)
    print(possibility)
    for item in possibility:
        if item[1] < 0 or item[0] < 0 or item[0] > len(labirint) or item[0] > len(labirint):
            continue
        elif labirint[item[0]][item[1]]=="1":
            continue
        elif labirint[item[0]][item[1]]==".":
            continue
        elif labirint[item[0]][item[1]]=="B":
            character = character + (item,)
            print("Конец игры")
            sys.exit()
        else:
            new_character = character + (item,)
            move(new_character)

labirint = afisa('maze.csv')
move(((1,0),))