import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace
import math

def plot(n):
    primes_list = find_primes_in_octave(n)
    perfect_squares_list = find_perfect_squares_in_octave(n)

    plt.figure(figsize = (18, 7))

    #draw point at orgin
    plt.plot(0,0, color = 'red', marker = 'o')
    plt.gca().annotate('O (0, 0)', xy=(0 - 0.1, 0 + 0.1), xycoords='data', fontsize=10)
    
    #draw circle
    r = 1.0
    angles = linspace(0 * pi, 2 * pi, 100 )
    xs = r * cos(angles)
    ys = r * sin(angles)
    plt.plot(xs, ys, color = 'green')
  

    count = 0
    for i in range(n,2 * n):
        color = "purple"
        angle = 360/n * count
        y = cos(angle * pi /180)
        x = sin(angle * pi/180)
        if i in primes_list:
            color = "blue"
            plt.plot([0,x], [0,y], marker='o', color=color)
            plt.gca().annotate(str(i), xy=(x,y), xycoords='data', fontsize=8)
        elif i in perfect_squares_list:
            color = "red"
            plt.plot([0,x], [0,y], marker='o', color=color)
            plt.gca().annotate(str(i), xy=(x,y), xycoords='data', fontsize=8)
        else:
            plt.plot(x, y, marker='o', color=color)
        if i == n:
            plt.gca().annotate(f"{n} / {2* n}", xy=(x, y + 0.1), xycoords='data', fontsize=15)
        count = count + 1
    plt.gca().set_aspect('equal')
    plt.show()

def find_primes_in_octave(n):
    primes_list = []
    for i in range(n, (2 * n) + 1):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                primes_list.append(i)
    return primes_list

def find_perfect_squares_in_octave(n):
    perfect_squares_list = []
    for i in range(n, (2 * n) + 1):
        if math.sqrt(i) == math.floor(math.sqrt(i)):
            perfect_squares_list.append(i)
    return perfect_squares_list

if __name__ == '__main__':
    plot(4)

