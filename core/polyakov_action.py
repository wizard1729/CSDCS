import numpy as np

def compute_polyakov_action(worldsheet, dt, T=1.0):

    X = worldsheet.X
    X_prev = worldsheet.X_prev

    dX_dt = (X - X_prev) / dt

    dX_dsigma = np.zeros_like(X)
    dX_dsigma[:,1:-1] = (X[:,2:] - X[:,:-2]) / (2*worldsheet.dsigma)
    dX_dsigma[:,0] = (X[:,1] - X[:,-1]) / (2*worldsheet.dsigma)
    dX_dsigma[:,-1] = (X[:,0] - X[:,-2]) / (2*worldsheet.dsigma)

    integrand = (dX_dt**2 - dX_dsigma**2)

    return 0.5 * T * np.sum(integrand)