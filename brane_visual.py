import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from geometry.brane_config import (
    d2_brane,
    warped_d2_brane,
    intersecting_brane,
    m2_brane
)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Choose configuration:

# 1️⃣ Simple D2
# X, Y, Z = d2_brane()

# 2️⃣ Warped D2
X, Y, Z = warped_d2_brane()

# 3️⃣ Intersecting branes
# (X1, Y1, Z1), (X2, Y2, Z2) = intersecting_brane()
# ax.plot_surface(X1, Y1, Z1, alpha=0.6)
# ax.plot_surface(X2, Y2, Z2, alpha=0.6)

# 4️⃣ M2-Brane
# X, Y, Z = m2_brane()

ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9)

ax.set_title("Brane Configuration Visualization")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect([1,1,0.5])

plt.show()