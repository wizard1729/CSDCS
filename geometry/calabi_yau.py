import numpy as np

def calabi_yau_moduli(alpha=0.0, resolution=200):

    x = np.linspace(-1.5, 1.5, resolution)
    y = np.linspace(-1.5, 1.5, resolution)

    X, Y = np.meshgrid(x, y)

    Z = (1 - X**(5+alpha) - Y**(5+alpha))

    Z_real = np.zeros_like(Z)
    mask = Z > 0
    Z_real[mask] = Z[mask]**(1/(5+alpha))

    return X, Y, Z_real