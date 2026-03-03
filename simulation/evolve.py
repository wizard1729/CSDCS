def evolve_string(worldsheet, dt=0.002):

    lap = worldsheet.laplacian_sigma()

    X_new = (
        2 * worldsheet.X
        - worldsheet.X_prev
        + dt**2 * lap
    )

    worldsheet.X_prev = worldsheet.X.copy()
    worldsheet.X = X_new