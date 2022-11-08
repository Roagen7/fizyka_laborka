import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pyplot import plot, show, errorbar, savefig

matplotlib.use('MacOSX')

if __name__ == '__main__':
    x = [1,2,3]
    y = [4,5,6]
    error = [1,1,1]

    coeff = np.polyfit(x,y,1) # linear regression

    plot(x,y, 'yo', x, np.poly1d(coeff)(x), '--k')
    errorbar(x, y, error, fmt='o')
    plt.title('wykres y(x)')
    plt.ylabel('label y')
    plt.xlabel('label x')

    show()
