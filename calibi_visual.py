import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from geometry.calabi_yau import calabi_yau_slice

X, Y, Z = calabi_yau_slice()

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='plasma', linewidth=0)

ax.set_title("Calabi–Yau Hypersurface Slice")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()