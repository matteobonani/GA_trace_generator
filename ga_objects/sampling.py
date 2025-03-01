from pymoo.core.sampling import Sampling
import numpy as np

class MySampling(Sampling):
    """Custom sampling class that returns the initial population for sampling."""
    def __init__(self, initial_population):
        super().__init__()
        self.initial_population = np.array(initial_population)

    def _do(self, problem, n_samples, **kwargs):
        return self.initial_population[:n_samples]

