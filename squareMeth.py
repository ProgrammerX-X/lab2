import numpy as np
import matplotlib.pyplot as plt

def squareMethod(a, b, n, f):
    summ = 0
    dx = (b-a)/n
    x_values = []
    y_values = []
    y1 = f(a)
    fig, axes = plt.subplots(1, 1, figsize=(6, 4))
    while a <= b:
        y = f(a)
        summ+=y*dx
        x_values.append(a)
        y_values.append(y)
        axes.scatter(a, y, color='r')
        a1 = a
        a1+=dx
        square_x = [a, a1, a1, a]
        square_y = [y1-0.1, y1-0.1, y, y]
        axes.fill(square_x, square_y, color='skyblue', edgecolor='black', linewidth=0.7)
        a+=dx
    print("Analitic value: ",summ)

    axes.plot(x_values, y_values, linestyle="-", label="square")
    plt.xlabel("X")
    plt.ylabel("Y")
    axes.grid(True)
    axes.legend()
    plt.show()