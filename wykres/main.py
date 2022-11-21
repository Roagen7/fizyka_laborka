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
    matplotlib.use('MacOSX')

    error = [0.02, 0.01, 0.01, 0.01]
    x = [1.0, 2.04, 4.0, 8.16]
    y = [0.57, 1.21, 2.39, 5.06]

    coeff = np.polyfit(x,y,1)
    dev = stdev(coeff[0], x, y)

    plot(x,y, 'yo', x, np.poly1d(coeff)(x),  c='0.88',markersize=0.01)
    _, caps, _ = errorbar(x, y, error, fmt='o',  markersize=0.01, capsize=1)

    for cap in caps:
        cap.set_markeredgewidth(1)

    plt.ylabel('Rx [Ω]')
    plt.xlabel('d^(-2) [mm^-2]')

    print("a=", coeff)
    print("stdev=", dev)

    show()
