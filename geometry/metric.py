import numpy as np

def induced_metric(worldsheet, dt):

    X = worldsheet.X
    X_prev = worldsheet.X_prev

    dX_dt = (X - X_prev) / dt

    dX_dsigma = np.zeros_like(X)
    dX_dsigma[:,1:-1] = (X[:,2:] - X[:,:-2]) / (2*worldsheet.dsigma)
    dX_dsigma[:,0] = (X[:,1] - X[:,-1]) / (2*worldsheet.dsigma)
    dX_dsigma[:,-1] = (X[:,0] - X[:,-2]) / (2*worldsheet.dsigma)

    g_tt = np.sum(dX_dt**2, axis=0)
    g_ss = np.sum(dX_dsigma**2, axis=0)
    g_ts = np.sum(dX_dt * dX_dsigma, axis=0)

    return g_tt, g_ss, g_ts