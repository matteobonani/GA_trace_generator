from cvxopt.modeling import constraint
from pymoo.core.callback import Callback
import matplotlib.pyplot as plt
import numpy as np


class UpdatePopulationCallback(Callback):
    def __init__(self):
        super().__init__()

        self.constraint_history = []
        self.n_violations_scores = []
        self.diversity_scores = []
        self.generation = 0


    def notify(self, algorithm):
        """
        Update the problem's current population and gather data for plotting.
        """
        population = algorithm.pop.get("X")

        algorithm.problem.set_current_population(population)

        # gather fitness and constraint scores for the current population
        G = algorithm.pop.get("G")
        if G is not None and G.size > 0:
            constraint_scores = G[:, 0]  # assuming G[0] corresponds to constraint violations
            self.constraint_history.append(np.mean(constraint_scores))
        F = algorithm.pop.get("F")
        diversity_scores = F[:, 0]  # assuming F[0] is the diversity score
        if F.shape[1] > 1:  # if G[1] exists (multi obj GA)
            n_violations_scores = F[:, 1]
            self.n_violations_scores.append(np.mean(n_violations_scores))

        self.diversity_scores.append(np.mean(diversity_scores))


        self.generation += 1


    def get_data(self):
        """
        Push data in the collector for plots.
        """
        return {
            "constraint_history": self.constraint_history,
            "n_violations_history": self.n_violations_scores,
            "diversity_history": self.diversity_scores,
            "generations": self.generation,
        }
    def test(self):
        self.generation += 1


    def plot_progress(self):
        """
        Plot the average fitness and constraint scores over generations.
        """
        plt.figure(figsize=(10, 5))

        # Plot average constraint scores
        plt.subplot(1, 2, 1)
        plt.plot(range(self.generation), self.n_violations_scores, label='Avg. Constraint Score', color='orange')
        plt.xlabel('Generation')
        plt.ylabel('Constraint Score')
        plt.title('Average Constraint Scores Over Generations')
        plt.grid(True)
        plt.legend()
        step_size = max(1, self.generation // 4)
        plt.xticks(range(0, self.generation, step_size))
        # plt.ylim(0, max(self.fitness_history) * 1.1)


        # Plot average fitness
        plt.subplot(1, 2, 2)
        plt.plot(range(self.generation), self.constraint_history, label='Avg. Fitness')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Average Fitness Over Generations')
        plt.grid(True)
        plt.legend()
        step_size = max(1, self.generation // 4)
        plt.xticks(range(0, self.generation, step_size))
        # plt.ylim(0, max(self.fitness_history) * 1.1)

        plt.tight_layout()
        # plt.pause(0.1)  # Pause for a brief moment to update the plots
        plt.show(block=False)


