import numpy as np


def objective_function(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]**2
    return sum / len(x)


bounds = [(-5, 5)] * 3


def differntial_evolution(objective_function, bounds, max_gen=5, mutation_factor=0.8,
                          crossover_probability=0.7, population_size=6):

    dimension = 3
    population = np.random.rand(population_size, dimension)
    lower_bound, upper_bound = np.asarray(bounds).T
    difference = np.fabs(lower_bound - upper_bound)
    initial_population = lower_bound + population * difference
    fitness = np.asarray([objective_function(ind) for ind in initial_population])
    best_index = np.argmin(fitness)
    best = initial_population[best_index]
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
            
            if new_fitness < fitness[j]:
                fitness[j] = new_fitness
                population[j] = trial_vector
                if new_fitness < fitness[best_index]:
                    best_index = j
                    best = new_population
        yield best, fitness[best_index]


for best, fitness in differntial_evolution(objective_function, bounds):
    print("best = ", best, "fitness = ", fitness)

