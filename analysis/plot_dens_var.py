"""
Plots the cloud radius as a function of cloud density.

Created by: Josh Borrow
Created on: 4th February 2018
"""


import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table

from helper import *

# Global variable that tells you where the outputs live
location = "../dens_var"


fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten() # We don't want no grid

# Only set _outer_ plot labels.
for ax in axes[::3]:
    ax.set_ylabel("Density (cm$^{-3}$)")

for ax in axes[3:5]:
    ax.set_xlabel("Depth into cloud (cm)")

# The final region is a 'special' plot.
axes[5].set_title("Edge of regions")
axes[5].set_xlabel("$n_H$ (cm$^{-3}$)")
axes[5].set_ylabel("Depth into cloud (cm)")


minima_H = []
minima_He = []
theory = []
nh = []


for number, ax in enumerate(axes[:-1]):
    number += 1 # We have no 0 density
    density = 10**number

    ovw = Table.read(f"{location}/{number}/hii_coolstar.ovr", format="ascii")
    make_plot(ax, ovw, density, temperature=35000)

    nh.append(density)
    theory.append(R_S(1e49, density))
    minima_H.append(find_turning_point(ovw, "HII"))
    minima_He.append(find_turning_point(ovw, "HeII"))


# Make the final 'special' plot.
axes[5].loglog(nh, theory, label="Theory ($R_S$)", color="black", alpha=0.5)
axes[5].loglog(nh, minima_H, label="H II", color="green")
axes[5].loglog(nh, minima_He, label="He II", color="red")

axes[3].legend()
axes[5].legend()

plt.tight_layout()

plt.savefig("density.pdf")

