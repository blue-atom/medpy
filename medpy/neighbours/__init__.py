"""
====================================
Neighbours (:mod:`medpy.neighbours`)
====================================
.. currentmodule:: medpy.neighbours

This package contains nearest neighbour methods.
 
Patch-wise :mod:`medpy.neighbours.knn`
===========================================
K-nearest-neighbours based methods. The interfaces are loosely based on the
``sklear.neighbours`` methods. The methods can be considered complementary to
the ones found there.

.. module:: medpy.neighbours.knn
.. autosummary::
    :toctree: generated/
    
    mkneighbors_graph
    pdist
    
"""

# Copyright (C) 2013 Oskar Maier
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import all functions/methods/classes into the module
from .knn import mkneighbors_graph, pdist

# import all sub-modules in the __all__ variable
__all__ = [s for s in dir() if not s.startswith('_')]


