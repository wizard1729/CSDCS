import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from core.worldsheet import WorldSheet
from core.polyakov_action import compute_polyakov_action
from core.virasoro import check_virasoro_constraints
from geometry.curvature import approximate_curvature
from simulation.evolve import evolve_string
from ai.vacuum_search import search_stable_vacuum
from analysis.fourier_spectrum import compute_fourier_spectrum


def run_simulation():

    ws = WorldSheet()
    dt = 0.002
    steps = 2000

    print("\n🔎 Performing Vacuum Optimization...")
    vacuum = search_stable_vacuum(ws)
    print("Initial Vacuum Energy:", vacuum)

    plt.ion()
    fig = plt.figure(figsize=(14,6))

    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)

    for t in range(steps):

        evolve_string(ws, dt)

        action = compute_polyakov_action(ws, dt)
        violation = check_virasoro_constraints(ws, dt)
        curvature = approximate_curvature(ws)

        modes, spectrum = compute_fourier_spectrum(ws)

        if t % 200 == 0:
            print(f"Step {t}")
            print("Action:", round(action,4))
            print("Virasoro Violation:", round(violation,6))
            print("Mean Curvature:", round(np.mean(curvature),4))
            dominant_mode = np.argmax(spectrum)
            print("Dominant Mode:", dominant_mode)
            print("-----------------------------")

        # -------------------
        # 3D STRING PLOT
        # -------------------
        ax1.clear()
        x, y, z = ws.X
        ax1.plot(x, y, z, linewidth=2)
        ax1.set_xlim(-2,2)
        ax1.set_ylim(-2,2)
        ax1.set_zlim(-2,2)
        ax1.set_box_aspect([1,1,1])
        ax1.view_init(elev=30, azim=t*0.4)
        ax1.set_title("3D String Dynamics")

        # -------------------
        # FOURIER SPECTRUM
        # -------------------
        ax2.clear()
        ax2.plot(np.abs(modes), spectrum)
        ax2.set_xlim(0,20)
        ax2.set_title("Fourier Mode Energy Spectrum")
        ax2.set_xlabel("Mode Number")
        ax2.set_ylabel("Energy")

        plt.pause(0.001)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    run_simulation()