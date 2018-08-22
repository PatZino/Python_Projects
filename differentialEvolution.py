import numpy as np


#  fobj = lambda x: sum(x**2)/len(x)
def fobj(x):
    value = 0
    for i in range(len(x)):
        value += x[i]**2
        return value / len(x)


bounds = [(-5, 5)] * 4


def differntial_evolution(fobj, bounds, max_gen=5, mutation_probability=0.8, crossover_probability=0.7, population_size=10):
    dimension = 4
    pop = np.random.rand(population_size, dimension)
    #  print(pop)

    min_b, max_b = np.asarray(bounds).T
    # print(min_b, max_b)

    diff = np.fabs(min_b - max_b)
    # print(diff)

    pop_denorm = min_b + pop * diff
    # print(pop_denorm)

    fitness = np.asarray([fobj(ind) for ind in pop_denorm])
    # print("fitness = ", fitness)

    best_idx = np.argmin(fitness)
    # print("best_idx = ", best_idx)

    best = pop_denorm[best_idx]
    # print("best = ", best)

    for i in range(max_gen):
        for j in range(population_size):
            idxs = [idx for idx in range(population_size) if idx != j]
            # print("idxs = ", idxs)
            a, b, c = pop[np.random.choice(idxs, 3, replace=False)]
            # print("a, b, c =", a, b, c)
            mutant = np.clip(a + mutation_probability * (b - c), 0, 1)
            # print("mutant = ", mutant)
            cross_points = np.random.rand(dimension) < crossover_probability
            # print("cross_points", cross_points)
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimension)] = True
                # print("cross_points eee = ", cross_points)
            trial = np.where(cross_points, mutant, pop[j])
            # print("trial = ", trial)
            trial_denorm = min_b + trial * diff
            # print("trial_denorm = ", trial_denorm)
            f = fobj(trial_denorm)
            # print("f = ", f)
            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
        yield best, fitness[best_idx]


for best, fitness in differntial_evolution(fobj, bounds):
    print("best = ", best, "fitness = ", fitness)
