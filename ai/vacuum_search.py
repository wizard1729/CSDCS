import numpy as np

def vacuum_energy(worldsheet):
    return np.var(worldsheet.X)

def search_stable_vacuum(worldsheet, iterations=30):

    best_energy = vacuum_energy(worldsheet)
    best_config = worldsheet.X.copy()

    for _ in range(iterations):

        perturb = 0.01 * np.random.randn(*worldsheet.X.shape)
        trial = worldsheet.X + perturb

        energy = np.var(trial)

        if energy < best_energy:
            best_energy = energy
            best_config = trial.copy()

    worldsheet.X = best_config
    worldsheet.X_prev = best_config.copy()

    return best_energy