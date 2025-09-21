# ed2assignment

import numpy as np
import matplotlib.pyplot as plt

phi = np.arctan(0.01)

x_ax  = np.array([1, 0])
ct_ax = np.array([0, 1])

rot = np.array([
    [np.cos(phi), -np.sin(phi)],
    [np.sin(phi),  np.cos(phi)]
])

x_p  = np.dot(rot, x_ax)
ct_p = np.dot(rot, ct_ax)

plt.plot([0, x_p[0]],  [0, x_p[1]], 'r--', label="x'")
plt.plot([0, ct_p[0]], [0, ct_p[1]], 'b--', label="ct'")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel("x",size=15)
plt.ylabel("ct",size=15)
plt.legend()
plt.title(f"Lorentz boost with φ = {phi}")
plt.show()
