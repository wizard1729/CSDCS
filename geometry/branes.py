import numpy as np

def d2_brane(radius=0.5, resolution=100):

    theta = np.linspace(0, 2*np.pi, resolution)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(theta)

    return x, y, z