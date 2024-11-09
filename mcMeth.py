import numpy as np
import matplotlib.pyplot as plt

def monteCarloMethod(a, b, n, f):
    x_max = b-a
    y_max = f(b)
    f_max = x_max*y_max

    x_rand = np.random.uniform(a, b, n)
    y_rand = np.random.uniform(0, y_max, n)

    in_graph = y_rand <= f(x_rand)
    m = np.sum(in_graph)

    i = (m / n)*f_max*(b-a)

    fig, axes = plt.subplots(1, 1, figsize=(6, 4))

    x = np.linspace(a, b, 200)
    y = f(x)

    axes.plot(x, y, color='blue')

    axes.scatter(x_rand[in_graph], y_rand[in_graph], color='green', s=1)
    axes.scatter(x_rand[~in_graph], y_rand[~in_graph], color = 'red', s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    axes.legend()
    plt.show()

    print("Points: ", m)