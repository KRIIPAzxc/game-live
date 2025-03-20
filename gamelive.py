
import os
import random
import sys
import time
import keyboard
sym = "█ "



speed = 2
size = int(input("size: "))
matrix = [[' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
cmatrix = []

stdout = os.fdopen(sys.stdout.fileno(), 'wb', size * int(size/2))
os.system(f'mode con cols={size} lines={int(size/2)} ')

def generate():
    matrix = []
    for y in range(int(size/2)):
        matrix.append([])
        for x in range(size):
            _sym = sym[int(random.random()*len(sym))]
            matrix[y].append(_sym)
    return matrix
            
def output(matrix):
    text = ""
    for line in matrix:
        for item in line:
            text += item
        text += "\n"
    stdout.write(''.join(text).encode())
    stdout.flush()

def nebors(x,y,matrix):
    count = 0
    nb = []
    for _y in range(3):
        for _x in range(3):
            #if (_y != 0 or _x != 0) and (_y != 2 or _x != 2) and (_y != 0 or _x != 2) and (_y != 2 or _x != 0):
            cy = y + _y - 1
            cx = x + _x - 1
            try:
                if (cx >= 0 and cy >= 0):
                    nb.append(matrix[cy][cx])
                    #print(nb)
            except: 
                1
    count = nb.count(sym[0])
    #print(count)
    return count
        

def step(matrix):
    live = (2,3)
    birth = (3,3)
    y = 0
    cmatrix = []
    for line in matrix:
        x = 0
        cmatrix.append([])
        for item in line:
            _nebors = nebors(x,y,matrix)
            if item == sym[0]:
                _nebors -= 1
            
            if item == sym[0] and _nebors in live:
                cmatrix[y].append(sym[0])
            elif item == sym[1] and _nebors in birth:
                cmatrix[y].append(sym[0])
            else:
                cmatrix[y].append(sym[1])
            x +=1
        y +=1

    output(cmatrix)
    return cmatrix
matrix = generate()
output(matrix)

def main(matrix,speed):
    while True:
        if keyboard.is_pressed("ctrl"):
            break
        if keyboard.is_pressed("alt"):
            matrix = generate()
        if keyboard.is_pressed("=") and speed != 5:
            speed += 1
        if keyboard.is_pressed("-") and speed != 1:
            speed -= 1
        matrix = step(matrix)
        time.sleep(0.05 / speed)

main(matrix,speed)
