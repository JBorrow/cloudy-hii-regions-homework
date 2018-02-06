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
location = "../qh_var"

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten() # We don't want no grid

# Only set _outer_ plot labels.
for ax in axes[::3]:
    ax.set_ylabel("Density (cm$^{-3}$)")

for ax in axes[3:5]:
    ax.set_xlabel("Depth into cloud (cm)")

axes[5].set_xlabel("$S_*$")
axes[5].set_ylabel("Depth into cloud (cm)")


minima_H = []
minima_He = []
theory = []
s_star = []


for number, ax in enumerate(axes):
    number += 47 # We have no 0 density
    density = 10**2

    ovw = Table.read(f"{location}/{number}/hii_coolstar.ovr", format="ascii")

    if number != 52:
        make_plot(ax, ovw, density, temperature=35000)
        ax.set_title(f"$S_* = 10^{{{number}}}$")

    s_star.append(10**number)
    theory.append(R_S(10**number, density))
    minima_H.append(find_turning_point(ovw, "HII"))
    minima_He.append(find_turning_point(ovw, "HeII"))



axes[5].loglog(s_star, minima_H, label="H II")
axes[5].loglog(s_star, minima_He, label="He II")
axes[5].loglog(s_star, theory, label="Theory")

axes[3].legend()
axes[5].legend()

plt.tight_layout()

plt.savefig("qh_var.pdf")

