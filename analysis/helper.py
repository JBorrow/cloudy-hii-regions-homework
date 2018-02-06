"""
Helper functions for the analysis scripts.

These are mainly physics and plotting functions.

Created by: Josh Borrow
Created on: 4th February 2018
"""


import numpy as np


def R_S(n_gamma, density, beta=3e-13):
    """
    Stromgren radius.
    
    The beta factor is given in cgs units.
    n_gamma is photons/second and density is hydrogen atoms per cubic
    cenitmetre with the default beta value.
    """
    prefactor = 3/(4 * np.pi)
    secondary = n_gamma / ((density**2) * beta)
    
    return (prefactor * secondary)**(1/3)


def format_number(number):
    """
    Formats a number into LaTeX style ready for plotting.
    """
    float_str = "{0:.2g}".format(number)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str


def make_plot(ax, overview, density, temperature):
    """
    Make a single plot on an axis of the:

    + Hydrogen density,
    + HI density,
    + HII density.
    """

    ax.plot(overview["depth"], overview["hden"], label="H")
    ax.plot(overview["depth"], overview["hden"]*overview["HI"], label="H I")
    ax.plot(overview["depth"], overview["hden"]*overview["HII"], label="H II")

    flux = 1e49
    stromgren = R_S(flux, density)

    formatted_R_S = format_number(stromgren)
    formatted_n_H = format_number(density)

    ax.set_title(
        f"$n_H$ = ${formatted_n_H}$ cm$^{{-3}}$, $R_S$ = ${formatted_R_S}$ cm"
    )


    ax.set_xscale("log", nonposx='clip')
    ax.set_yscale("log", nonposy='clip')

    return


def find_turning_point(ovw, region="HII"):
    """
    Uses the given region to find the depth of where the gradient is at a
    minimum. This should give the edge of the region.
    """

    grad = np.gradient(ovw[region])
    
    minimum_depth = ovw["depth"][grad == np.amin(grad)]
    
    try:
        return float(minimum_depth)
    except:
        return float(minimum_depth[0])



