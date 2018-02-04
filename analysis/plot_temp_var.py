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
locations = {
    "lowdensity": "../temp_var_lowdensity",
    "highdensity": "../temp_var_highdensity",
}

density_switch = {
    "lowdensity": 1,
    "highdensity": 3,
}


for filename, location in locations.items():
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten() # We don't want no grid

    # Only set _outer_ plot labels.
    for ax in axes[::3]:
        ax.set_ylabel("Density (cm$^{-3}$)")

    for ax in axes[3:5]:
        ax.set_xlabel("Depth into cloud (cm)")

    # The final region is a 'special' plot.
    axes[5].set_title("Edge of regions")
    axes[5].set_xlabel("Temperature of star (K)")
    axes[5].set_ylabel("Depth into cloud (cm)")


    minima_H = []
    minima_He = []
    theory = []
    temps = []

    # We want to skip half of the files, so we use an iterator instead of a more
    # pythonic iteration setup.
    ax = 0


    for number in range(1, 11):
        density = 10**(density_switch[filename])
        temperature = int(number * 1e4)

        ovw = Table.read(f"{location}/{temperature}/hii_coolstar.ovr", format="ascii")

        if number % 2:
            make_plot(axes[ax], ovw, density, temperature)
            ax += 1

        temps.append(temperature)
        theory.append(R_S(1e49, density))
        minima_H.append(find_turning_point(ovw, "HII"))
        minima_He.append(find_turning_point(ovw, "HeII"))


    # Make the final 'special' plot.
    axes[5].semilogy(temps, theory, label="Theory ($R_S$)", color="black", alpha=0.5)
    axes[5].semilogy(temps, minima_H, label="H II", color="green")
    axes[5].semilogy(temps, minima_He, label="He II", color="red")

    axes[3].legend()
    axes[5].legend()

    plt.tight_layout()

    plt.savefig(f"{filename}.pdf")

