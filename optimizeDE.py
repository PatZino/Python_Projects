from __future__ import division

import numpy as np

from scipy.optimize import differential_evolution, rosen

N_VARS = 2
VAR_BOUND = (-5, 5)
REPLICATES = 100

bounds = [VAR_BOUND] * N_VARS

print ('offset\t<iters>\t<error>')

for offset in (0, 1, 10, 100, -10):
    total_iters = 0
    total_error = 0

    for i in range(REPLICATES):
        result = differential_evolution(
            lambda x: rosen(x) + offset,
            bounds
            )

        total_iters += result.nit
        total_error += np.sum(np.square(result.x - 1))

    print('{:5n}\t{:6.1f}\t{:0.0e}'.format(
        offset,
        total_iters / REPLICATES,
        total_error / REPLICATES
        ))