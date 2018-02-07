"""
This plots the mean temperature _inside_ the Hii region.

Created by: Josh Borrow
Created on: 7th February 2018
"""

import numpy as np
import matplotlib.pyplot as plt

from astropy.table import Table
from helper import *

# Global variable that thells you where the files are.
locations = ("../temp_var_lowdensity", "../temp_var_highdensity")
labels = ("$n_h = 10^1$ cm$^{-3}$", "$n_h = 10^3$ cm$^{-3}$")

fig, (ax) = plt.subplots(1, 1)

for location, label in zip(locations, labels):
    cloud = []
    star = []


    for number in range(1, 11):
        density = 10
        temperature = number * 1e4

        ovw = Table.read(f"{location}/{int(temperature)}/hii_coolstar.ovr", format="ascii")

        edge_of_region = find_turning_point(ovw, "HII")
        temp = np.mean(ovw["Te"][ovw["depth"] < edge_of_region])
        
        cloud.append(temp)
        star.append(temperature)


    ax.plot(star, cloud, label=label)


ax.set_xlabel("Stellar temperature (K)")
ax.set_ylabel("Mean cloud temperature (K)")

ax.legend()

plt.savefig("cloud_temp.pdf")

