import numpy as np
import matplotlib.pyplot as plt

def trapezoidMethod(a, b, n, f):
    summ = 0
    dx = (b-a)/n
    x_values = []
    y_values = []
    count = 1
    y1 = f(a)
    s = 0
    fig, axes = plt.subplots(1, 1, figsize=(6, 4))

    while a <= b:
        y = f(a)
        summ+=y*dx
        x_values.append(a)
        y_values.append(y)
        axes.scatter(a, y, color='r')
        a1 = a
        a1+=dx
        if count == 1:
            s += ((f(a)+f(a+dx))/2)*dx
        elif count == n:
            s += ((f(a+count*dx)+f(b))/2)*dx
        else:
            s += ((f(a+dx)+f(a+count*dx))/2)*dx
        square_x = [a, a1, a1, a]
        square_y = [y1-0.1, y1-0.1, f(a+dx), y]
        axes.fill(square_x, square_y, color='skyblue', edgecolor='black', linewidth=0.7)
        a+=dx
        count+=1
    print("S sum trap: ", s)
    print("Analitic value: ",summ)

    axes.plot(x_values, y_values, linestyle="-", label="square")
    plt.xlabel("X")
    plt.ylabel("Y")
    axes.grid(True)
    axes.legend()
    plt.show()