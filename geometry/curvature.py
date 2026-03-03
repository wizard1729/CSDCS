import numpy as np

def approximate_curvature(worldsheet):

    X = worldsheet.X
    ds2 = worldsheet.dsigma**2

    second_derivative = np.zeros_like(X)

    second_derivative[:,1:-1] = (
        X[:,2:] - 2*X[:,1:-1] + X[:,:-2]
    ) / ds2

    curvature = np.linalg.norm(second_derivative, axis=0)

    return curvature