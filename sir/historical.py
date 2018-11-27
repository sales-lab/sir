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
from os.path import join, dirname

import numpy as np


def historical_data():
    """
    Return pseudo-historical time series of a disease outbreak.

    :return: an Nx3 numpy array representing time course measurements of the S, I and R variables.
    """
    return np.load(join(dirname(__file__), 'historical.npy'))
