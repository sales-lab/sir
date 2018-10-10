# sir: numerical solver for the SIR infection model
# Copyright (C) 2018 Gabriele Sales
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from typing import Iterable, Tuple

import numpy as np
from scipy.integrate import odeint
from ipywidgets import interact
import ipywidgets as widgets

import matplotlib.pyplot as plt


Population = Tuple[float, float, float]
Params = Tuple[float, float, float, float, float]


def sir(t: Iterable[float],
        pop: Population = (990., 10., 0.),
        params: Params = (3., .02, .0005, .05, .01)):
    """
    Simulates and then plots the behaviour of the SIR model.

    :param t: a vector of time points
    :param pop: a 3-element tuple with the population size for S, I and R
    :param params: a tuple with the (rb, rd, ri, rr, rs) parameters
    """
    t = list(t)
    p = odeint(_timestep, pop, t, params)

    for i in range(3):
        plt.plot(t, p[:, i], color='brg'[i], label='SIR'[i])

    plt.title('SIR model simulation')
    plt.legend(loc='upper right')
    plt.xlabel('Days')
    plt.show()


def _timestep(pop: Population, _, *params: Params) -> Population:
    s, i, r = pop
    rb, rd, ri, rr, rs = params

    return (rb + rs*r - ri*s*i,
            ri*s*i - rr*i - rd*i,
            rr*i - rs*r)


def sir_interactive():
    """
    Runs an interactive widget for exploring the effect of the parameter rD on the SIR model.
    """
    @interact(
        days=widgets.IntSlider(min=100, max=1000, step=10, value=365, continuous_update=False),
        rd=widgets.FloatSlider(min=0, max=.5, step=.01, value=.02, continuous_update=False))
    def f(days, rd):
        t = np.arange(days)
        params = (3., rd, .0005, .05, .01)

        p = odeint(_timestep, (990., 10., 0.), t, params)

        for i in range(3):
            plt.plot(t, p[:, i], color='brg'[i], label='SIR'[i])

        plt.title('SIR model simulation (%d days)' % days)
        plt.legend(loc='upper right')
        plt.xlabel('Days')

        plt.show()

    return f
