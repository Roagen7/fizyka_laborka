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

def statyczne():
    return [0.05, 0.1, 0.150, 0.200, 0.250], \
           [0.088, 0.180, 0.271, 0.359, 0.449]
def dynamiczne():
    x = [0.05, 0.1, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450]
    y = [5.18,
8.95,
10.66,
11.65,
13.14,
14.49,
15.56,
16.42,
17.39]
    y = [(t / 20) * (t / 20) for t in y]
    return x,y

if __name__ == '__main__':
    matplotlib.use('MacOSX')

    x, y = statyczne()
    error = [0.002 for t in y]

    print(y)
    coeff = np.polyfit(x,y,1) # linear regression
    dev = stdev(coeff[0], x, y)

    plot(x,y, 'yo', x, np.poly1d(coeff)(x),  c='0.88',markersize=0.01)
    _, caps, _ = errorbar(x, y, error, fmt='o',  markersize=0.01, capsize=1)

    for cap in caps:
        cap.set_markeredgewidth(1)

    #plt.title('')
    plt.ylabel('x[m]')
    plt.xlabel('m [kg]')

    print("a=", coeff)
    print("stdev=", dev)

    show()
