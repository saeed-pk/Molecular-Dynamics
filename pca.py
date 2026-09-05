import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import gaussian_kde

# =========================
# INPUT FILE
# =========================
input_file = "PCA.dat"

# =========================
# LOAD DATA
# =========================
data = pd.read_csv(input_file, sep=r"\s+", comment='#')

# Expecting columns: Frame, Mode1 (PC1), Mode2 (PC2)
pc1 = data.iloc[:, 1].values
pc2 = data.iloc[:, 2].values

print("Loaded frames:", len(pc1))

# =========================
# 2D KERNEL DENSITY ESTIMATION (PROBABILITY)
# =========================
xy = np.vstack([pc1, pc2])
kde = gaussian_kde(xy)

# Grid for evaluation
x_grid = np.linspace(pc1.min(), pc1.max(), 80)
y_grid = np.linspace(pc2.min(), pc2.max(), 80)
X, Y = np.meshgrid(x_grid, y_grid)

Z = kde(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

# Normalize probability
Z = Z / Z.max()

# =========================
# PLOT 3D SURFACE
# =========================
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(
    X,
    Y,
    Z,
    cmap='viridis',
    edgecolor='none',
    alpha=0.9
)

# =========================
# AXIS LABELS
# =========================
ax.set_xlabel(
    "PC1 (Mode 1)",
    fontsize=20,
    fontname='Times New Roman',
    fontweight='bold',
    labelpad=15
)

ax.set_ylabel(
    "PC2 (Mode 2)",
    fontsize=20,
    fontname='Times New Roman',
    fontweight='bold',
    labelpad=15
)

ax.set_zlabel(
    "Probability Density",
    fontsize=20,
    fontname='Times New Roman',
    fontweight='bold',
    labelpad=15
)

# =========================
# TITLE
# =========================
ax.set_title(
    "Principal Component Analysis (PCA)\nD1Cl1",
    fontsize=20,
    fontname='Times New Roman',
    fontweight='bold',
    pad=2
)

# Bring title closer to the plot
plt.subplots_adjust(top=0.98)

# =========================
# TICK LABELS
# =========================
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='z', which='major', labelsize=10)

for label in ax.get_xticklabels():
    label.set_fontname('Times New Roman')
    label.set_fontweight('bold')

for label in ax.get_yticklabels():
    label.set_fontname('Times New Roman')
    label.set_fontweight('bold')

for label in ax.get_zticklabels():
    label.set_fontname('Times New Roman')
    label.set_fontweight('bold')

# =========================
# COLORBAR ON LEFT SIDE
# =========================
try:
    cbar = fig.colorbar(
        surf,
        ax=ax,
        shrink=0.6,
        aspect=15,
        pad=0.08,
        location='left'
    )
except TypeError:
    # For older matplotlib versions
    cbar = fig.colorbar(
        surf,
        ax=ax,
        shrink=0.6,
        aspect=15,
        pad=0.08
    )
    cbar.ax.yaxis.set_ticks_position('left')
    cbar.ax.yaxis.set_label_position('left')

cbar.set_label(
    'Probability Density',
    fontsize=20,
    fontname='Times New Roman',
    fontweight='bold'
)

for label in cbar.ax.get_yticklabels():
    label.set_fontname('Times New Roman')
    label.set_fontweight('bold')
    label.set_fontsize(10)

# =========================
# SAVE FIGURE
# =========================
plt.savefig(
    "PCA_3D_probability_surface.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()

print("3D PCA probability plot saved.")
