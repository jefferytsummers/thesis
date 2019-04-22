from matplotlib import pyplot as plt
import numpy as np

def main():
    pxshift = [80,        84,    111,    135,   165,    206,    223,     248,     293]
    ncshift = [4.9e-3, 6.6e-3, 5.2e-3, 8.7e-3, 8.0e-3, 9.8e-3, 11.5e-3, 11.9e-3, 13.2e-3]
    bestfit = [24283*_-43.6 for _ in ncshift]

    plt.xlabel(r'Chamber Index Shift $\delta n_c$')
    plt.ylabel(r'Pixel Shift')
    plt.plot(ncshift, bestfit)
    plt.errorbar(ncshift, pxshift, 18, 1e-4, linestyle="None")
    plt.show()
    return 0


main()
