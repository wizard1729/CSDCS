# CSDCS — Computational Superstring Dynamics & Compactification Simulator

CSDCS is a computational physics sandbox for simulating classical string dynamics, Fourier mode spectrum analysis, Calabi–Yau hypersurface visualization, and brane configuration modeling.

This project explores geometric and spectral structures inspired by string theory using numerical methods and scientific visualization.

---

## 🚀 Features

### 1️⃣ Classical Closed String Simulator
- Discretized worldsheet evolution
- Leapfrog finite-difference solver
- Polyakov action computation
- Virasoro constraint monitoring
- Induced worldsheet metric
- Curvature estimation
![WhatsApp Image 2026-03-03 at 20 31 52](https://github.com/user-attachments/assets/294fff03-2ee6-4bf4-90e7-49eb9482b57a)
![WhatsApp Image 2026-03-03 at 20 31 51 (1)](https://github.com/user-attachments/assets/4bac7981-8b09-4ba8-ae54-cde7471333b5)
![WhatsApp Image 2026-03-03 at 20 31 51](https://github.com/user-attachments/assets/cd4c684e-d4f7-4559-af84-d00ce7f88d3f)

### 2️⃣ Fourier Mode Spectrum Analyzer
- FFT decomposition along σ
- Energy distribution across modes
- Dominant harmonic tracking
- Spectral evolution visualization

### 3️⃣ Calabi–Yau Hypersurface Visualization
- Real slice of Fermat-type hypersurface
- Algebraic geometry surface plotting
- Moduli deformation support

### 4️⃣ Brane Configuration Visualization
- D2-brane (flat membrane)
- Warped D2-brane
- Intersecting branes
- M2-brane analog surface

---

## 📂 Project Structure

```
CSDS/
├── core/
│   ├── __init__.py
│   ├── worldsheet.py
│   ├── polyakov_action.py
│   ├── curvature.py
│   └── virasoro.py
├── geometry/
│   ├── __init__.py
│   ├── metric.py
│   ├── curvature.py
│   ├── calabi_yau.py
│   ├── brane_config.py
│   └── branes.py
├── simulation/
│   ├── __init__.py
│   └── evolve.py
├── analysis/
│   ├── __init__.py
│   └── fourier_spectrum.py
├── ai/
│   ├── __init__.py
│   └── vacuum_search.py
├── main.py
├── calabi_visual.py
├── brane_visual.py
└── README.md
```

---

## 🧮 Mathematical Background

### Polyakov Action

\[
S = \frac{T}{2} \int d^2\sigma \left( (\partial_\tau X)^2 - (\partial_\sigma X)^2 \right)
\]

### Virasoro Constraints

\[
(\partial_\tau X \pm \partial_\sigma X)^2 = 0
\]

### Fourier Decomposition

\[
X(\sigma,\tau) = \sum_n a_n(\tau) e^{in\sigma}
\]

### Calabi–Yau Slice

\[
x^5 + y^5 + z^5 = 1
\]

---

## 🖥️ Installation

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

**Activate:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install numpy matplotlib
```

## ▶️ Running the Simulations

### 🔹 Full String + Spectrum Simulation

```bash
python main.py
```

**Displays:**
- 3D string dynamics
- Fourier energy spectrum
- Console physics diagnostics

### 🔹 Calabi–Yau Visualization

```bash
python calabi_visual.py
```

**Displays:**
- 3D algebraic hypersurface slice

### 🔹 Brane Configurations

```bash
python brane_visual.py
```

**Displays:**
- D2 / Warped D2 / M2 brane surfaces

---

## ⚠️ Important Notes

**This project:**
- ✔ Simulates classical string dynamics
- ✔ Provides geometric visualizations inspired by string theory
- ✔ Implements spectral analysis

**This project does NOT:**
- ✘ Solve full quantum superstring theory
- ✘ Compute exact Ricci-flat metrics
- ✘ Perform full DBI action dynamics
- ✘ Implement supersymmetric fermionic fields

It is a computational visualization and numerical modeling framework inspired by string theory structures.

---

## 📈 Future Extensions

- Symplectic integrator for Hamiltonian evolution
- Mode evolution heatmaps
- Brane collision dynamics
- Compactified extra dimension modeling
- Flux vacuum landscape exploration
- GPU acceleration (PyTorch / CUDA)
- Ricci curvature numerical approximation

---

## 👤 Author

Anurag Lal

Computational Superstring Dynamics & Compactification Simulator (CSDCS)  
Built for advanced numerical exploration of geometric and spectral structures inspired by string theory.

---

## 📜 License

For educational and research exploration purposes.
