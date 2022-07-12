# sir: numerical solver for the SIR infection model
# Copyright (C) 2022 Gabriele Sales
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
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as w


def linear_points(n=100):
    """
    Generate a cloud of 2D points, where y depends linearly on x.

    Some random noise is added to y.

    :param n: number of points to generate
    :return: a tuple containing two numpy arrays, for x and y coordinates
    """
    x = np.sort(np.random.rand(n))
    alpha = np.clip(np.random.randn(), -3, 3)
    beta = np.random.rand()
    y = beta * x + alpha + np.random.randn(x.shape[0]) * 1e-2
    return x, y


def regression_interactive(x: np.array, y: np.array) -> None:
    @interact(
        alpha=w.FloatSlider(min=-3, max=3, step=.01, value=0, description="Alpha:"),
        beta=w.FloatSlider(min=0, max=1, step=.01, value=0, description="Beta:"))
    def f(alpha, beta):
        y2 = beta * x + alpha

        plt.plot(x, y, "b.")
        plt.plot(x, y2, "r")

        plt.title("Linear Regression")
        plt.show()

    return f

