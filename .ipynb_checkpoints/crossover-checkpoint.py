import numpy as np
import pandas as pd
import random
from pymoo.core.crossover import Crossover


class TraceCrossover(Crossover):
    def __init__(self, variable_boundaries):
        """
        Initialize the crossover operator for trace generation.
        """
        super().__init__(2, 2)  # Two parents produce two offspring
        self.variable_boundaries = variable_boundaries



    def _do(self, X, **kwargs):
        """
        Perform crossover for a population of traces.
        """
        n_parents, n_matings, n_var = X.shape
        Y = np.zeros_like(X)

        for k in range(n_matings):

            # Get two parents
            parent1 = X[0, k, :]
            parent2 = X[1, k, :]


            # Choose a random crossover point respecting boundaries
            crossover_idx = random.randint(1, len(self.variable_boundaries) - 2)
            crossover_point = self.variable_boundaries[crossover_idx]

            # Generate offspring by swapping parts at the crossover point
            child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
            child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])


            Y[0, k, :] = child1
            Y[1, k, :] = child2

        return Y
