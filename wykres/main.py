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

    error = [0.54, 0.7, 0.86, 1.03, 1.20, 1.38]
    error_x = [0.02 for x in range(len(error))]
    x = [0.04, 0.2, 0.36, 0.53, 0.7, 0.86]
    y = [9.56, 41.20, 73.33, 107.91, 142.98, 177.56]

    coeff = np.polyfit(x,y,1)
    dev = stdev(coeff[0], x, y)

    plot(x,y, 'yo', x, np.poly1d(coeff)(x),  c='0.88',markersize=0.01)
    _, caps, _ = errorbar(x, y, yerr = error,xerr = error_x, fmt='o',  markersize=0.01, capsize=1)

    for cap in caps:
        cap.set_markeredgewidth(1)

    plt.ylabel('B [mT]')
    plt.xlabel('Im [A]')

    print("a=", coeff)
    print("stdev=", dev)

    show()
