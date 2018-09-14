import numpy as np


def objective_function(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]**2
    return sum / len(x)


bounds = [(-5, 5)] * 5


def differntial_evolution(objective_function, bounds, max_gen=10, mutation_factor=0.8,
                          crossover_probability=0.7, population_size=10):
    """
    differential evolution program to minimize a function
    """

    dimension = 5
    population = np.random.rand(population_size, dimension)
    lower_bound, upper_bound = np.asarray(bounds).T
    difference = np.fabs(lower_bound - upper_bound)
    initial_population = lower_bound + population * difference
    print("initial pop: ", initial_population)
    fitness = np.asarray([objective_function(ind) for ind in initial_population])
    print("fitness : ", fitness)
    best_index = np.argmin(fitness)
    best = initial_population[best_index]
    print("best : ", best)
    for i in range(max_gen):
        for j in range(population_size):
            indices = [index for index in range(population_size) if index != j]

            x0, x1, x2 = population[np.random.choice(indices, 3, replace=False)]
            
            mutant_vector = np.clip(x0 + mutation_factor * (x1 - x2), 0, 1)
            
            crossover = np.random.rand(dimension) < crossover_probability

            if not np.any(crossover):
                crossover[np.random.randint(0, dimension)] = True

            trial_vector = np.where(crossover, mutant_vector, population[j])
            
            new_population = lower_bound + trial_vector * difference

            new_fitness = objective_function(new_population)

            #  print("\nnew fitness : ", new_fitness)
            #  print("fitness[", j, "]", fitness[j])

            #  print("new_fitness.all() < fitness[j].all() :", new_fitness < fitness[j])

            if new_fitness < fitness[j]:
                fitness[j] = new_fitness
                population[j] = trial_vector
                if new_fitness < fitness[best_index]:
                    best_index = j
                    best = new_population
        yield best, fitness[best_index]


print(differntial_evolution.__doc__)
for best, fitness in differntial_evolution(objective_function, bounds):
    print("best = ", best, "fitness = ", fitness)

