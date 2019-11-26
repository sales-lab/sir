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
import matplotlib as mpl
import numpy as np


def larger_figures():
    mpl.rc('figure', figsize=(14, 7))


def combinations(*choices):
    """
    Build a matrix with all combinations of input variables.

    :param choices: admissible values for each variable
    :return: a bi-dimensional numpy array
    """
    return np.asarray(np.meshgrid(*choices)).T.reshape((-1, len(choices)))
