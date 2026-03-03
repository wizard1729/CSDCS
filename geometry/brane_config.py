import numpy as np


# ---------------------------
# D2-Brane (Flat Membrane)
# ---------------------------
def d2_brane(radius=1.0, resolution=100):

    theta = np.linspace(0, 2*np.pi, resolution)
    r = np.linspace(0, radius, resolution)

    Theta, R = np.meshgrid(theta, r)

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    Z = np.zeros_like(X)

    return X, Y, Z


# ---------------------------
# Warped D2-Brane
# ---------------------------
def warped_d2_brane(radius=1.0, resolution=100):

    theta = np.linspace(0, 2*np.pi, resolution)
    r = np.linspace(0, radius, resolution)

    Theta, R = np.meshgrid(theta, r)

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    Z = 0.3 * np.sin(3 * Theta) * np.exp(-R)

    return X, Y, Z


# ---------------------------
# Intersecting Branes
# ---------------------------
def intersecting_brane(radius=1.0, offset=0.5, resolution=100):

    theta = np.linspace(0, 2*np.pi, resolution)
    r = np.linspace(0, radius, resolution)

    Theta, R = np.meshgrid(theta, r)

    X1 = R * np.cos(Theta)
    Y1 = R * np.sin(Theta)
    Z1 = np.zeros_like(X1)

    X2 = R * np.cos(Theta)
    Y2 = R * np.sin(Theta)
    Z2 = np.ones_like(X2) * offset

    return (X1, Y1, Z1), (X2, Y2, Z2)


# ---------------------------
# M2-Brane (Curved Membrane)
# ---------------------------
def m2_brane(resolution=100):

    u = np.linspace(-1, 1, resolution)
    v = np.linspace(-1, 1, resolution)

    U, V = np.meshgrid(u, v)

    X = U
    Y = V
    Z = np.sin(np.pi * U) * np.cos(np.pi * V)

    return X, Y, Z