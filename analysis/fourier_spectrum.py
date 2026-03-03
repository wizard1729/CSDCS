import numpy as np

def compute_fourier_spectrum(worldsheet):
    """
    Compute Fourier spectrum of string along sigma.
    Returns mode amplitudes and energy per mode.
    """

    X = worldsheet.X[2]  # Analyze Z-direction vibration

    fft_vals = np.fft.fft(X)
    power_spectrum = np.abs(fft_vals)**2

    modes = np.fft.fftfreq(len(X), d=worldsheet.dsigma)

    return modes, power_spectrum