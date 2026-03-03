import numpy as np

class WorldSheet:
    def __init__(self, sigma_points=300):
        self.sigma_points = sigma_points
        self.sigma = np.linspace(0, 2*np.pi, sigma_points)
        self.dsigma = self.sigma[1] - self.sigma[0]

        self.X = np.zeros((3, sigma_points))
        self.X_prev = np.zeros((3, sigma_points))

        self.initialize_string()

    def initialize_string(self):

        # Base circular closed string
        self.X[0] = np.cos(self.sigma)
        self.X[1] = np.sin(self.sigma)
        self.X[2] = 0

        # Add stable vibrational modes
        for n in range(1, 4):
            amp = 0.2 / n
            self.X[2] += amp * np.sin(n * self.sigma)

        self.X_prev = self.X.copy()

    def laplacian_sigma(self):

        lap = np.zeros_like(self.X)
        ds2 = self.dsigma ** 2

        lap[:,1:-1] = (
            self.X[:,2:] - 2*self.X[:,1:-1] + self.X[:,:-2]
        ) / ds2

        lap[:,0] = (
            self.X[:,1] - 2*self.X[:,0] + self.X[:,-1]
        ) / ds2

        lap[:,-1] = (
            self.X[:,0] - 2*self.X[:,-1] + self.X[:,-2]
        ) / ds2

        return lap