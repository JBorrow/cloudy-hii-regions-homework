"""
This script makes the differential plot. This differential plot shows how we
detect the edges of the HII clouds.

Created by: Josh Borrow
Created on: 4th February 2018
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table

from helper import *

# Global variable.
temp_var_location = "../temp_var_lowdensity"


fig, ax = plt.subplots(figsize=(8, 6))

for number in range(1, 11):
    filename = f"{temp_var_location}/{number*10000}/hii_coolstar.ovr"
    ovw = Table.read(filename, format="ascii")

    grad = np.gradient(ovw["HII"])

    ax.plot(ovw["depth"], grad, label=fr"$T = {number} \times 10^4$ K")


plt.ylabel(r"$\mathrm{d}n_{HII}/\mathrm{d}r$ (cm$^{-4}$)")
plt.xlabel("Depth into cloud, $r$ (cm)")

ax.legend()

plt.savefig("differential.pdf")

