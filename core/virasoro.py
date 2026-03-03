import numpy as np

def check_virasoro_constraints(worldsheet, dt):

    X = worldsheet.X
    X_prev = worldsheet.X_prev

    dX_dt = (X - X_prev) / dt

    dX_dsigma = np.zeros_like(X)
    dX_dsigma[:,1:-1] = (X[:,2:] - X[:,:-2]) / (2*worldsheet.dsigma)
    dX_dsigma[:,0] = (X[:,1] - X[:,-1]) / (2*worldsheet.dsigma)
    dX_dsigma[:,-1] = (X[:,0] - X[:,-2]) / (2*worldsheet.dsigma)

    constraint_plus = np.sum((dX_dt + dX_dsigma)**2, axis=0)
    constraint_minus = np.sum((dX_dt - dX_dsigma)**2, axis=0)

    return np.mean(np.abs(constraint_plus) + np.abs(constraint_minus))