import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pyplot import plot, show, errorbar, savefig


def stdev(a, x, y): #stdev = S_a
    if len(x) != len(y):
        raise Exception("Invalid size: len(x) != len(y)")

    n = len(y)

    numerator = abs(sum([i * i for i in y]) - a * sum([x[i]*y[i] for i in range(n)]))
    denominator = n * sum([i * i for i in x])

    return math.sqrt(n/(n-2) * numerator / denominator)


if __name__ == '__main__':
   # matplotlib.use('Windows')

    error = [0.00, 0.00, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02] #zmienić todo
    x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]#zmienić todo
    y = [3.24, 7.16, 10.80, 14.62, 18.26, 21.99, 26.50, 29.74, 33.96, 37.59]#zmienić todo

    coeff = np.polyfit(x,y,1)
    dev = stdev(coeff[0], x, y)

    plot(x,y, 'yo', x, np.poly1d(coeff)(x),  c='0.88',markersize=0.01)
    _, caps, _ = errorbar(x, y, error, fmt='o',  markersize=0.01, capsize=1)

    for cap in caps:
        cap.set_markeredgewidth(1)

    plt.ylabel('F [N] * 10^-3') #zmienić todo
    plt.xlabel('I [A]') #zmienić todo

    print("a=", coeff)
    print("stdev=", dev)

    show()
