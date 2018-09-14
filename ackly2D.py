import numpy as np


def ackley(x):
    a = 20
    b = 0.2
    c = 2*np.pi
    first = 0
    secondPart = 0
    """
    for i in range(len(x)):
        firstPart += (-b * (((x[i] ** 2) * 0.5) + ((y[i] ** 2) * 0.5)))
        secondPart += (np.cos(c * x[i]) + np.cos(c * y[i]))
        result = -a * np.exp(firstPart) - np.exp(secondPart) + a + np.exp(1)
    return result
    """
    for i in range(len(x)):
        first += (x[i] ** 2)
        firstPart = (first / len(x)) ** 0.5
        secondPart += (np.cos(c * x[i]))
        result = -a * np.exp(-b * firstPart) - np.exp(secondPart / len(x)) + a + np.exp(1)
    return result


print("ackley = ", ackley([0.1, 0.2, 0.3, 0.4]))

bounds = [(-5, 5)] * 8


def differntial_evolution(ackley, bounds, max_gen=100, mutation_factor=0.8,
                          crossover_probability=0.7, population_size=30):
    dimension = 8
    population = np.random.rand(population_size, dimension)
    print("population : \n", population)
    lower_bound, upper_bound = np.asarray(bounds).T
    print("lower_bound =", lower_bound, " upper_bound =", upper_bound)
    difference = np.fabs(lower_bound - upper_bound)
    print("difference : \n", difference)
    initial_population = lower_bound + population * difference
    print("initial pop: \n", initial_population)
    #  fitness = np.asarray([ackley(ind, ind2) for ind in [initial_population] for ind2 in [initial_population]

    fitness = np.asarray([ackley(ind) for ind in initial_population])
    print("fitness : ", fitness)
    """
    print("initial pop", initial_population[0][1])
    exit(1)
    fitness_list = []
    for i in range(0, 10):
        fitness_list.append(ackley(initial_population[i][:]))
    fitness = np.asarray(fitness_list)

    #fitness = np.asarray([ackley(ind, ind2) for ind in [initial_population] for ind2 in [initial_population]])
    print("fitness : \n", fitness)
    
    """

    """ 
    best_index = np.unravel_index(np.argmin(fitness), fitness.shape)
    print("best_index : \n", best_index)
    best = initial_population[best_index[0]]
    print("best : \n", best, "\n")
    """

    best_index = np.argmin(fitness)
    print("best_index : \n", best_index)
    best = initial_population[best_index]
    print("best : \n", best, "\n")

    for i in range(max_gen):
        for j in range(population_size):
            indices = [index for index in range(population_size) if index != j]

            x0, x1, x2 = population[np.random.choice(indices, 3, replace=False)]

            mutant_vector = np.clip(x0 + mutation_factor * (x1 - x2), 0, 1)
            #  print("\n mutant_vector[", j, "]\n", mutant_vector)

            crossover = np.random.rand(dimension) < crossover_probability

            if not np.any(crossover):
                crossover[np.random.randint(0, dimension)] = True

            trial_vector = np.where(crossover, mutant_vector, population[j])

            new_population = lower_bound + trial_vector * difference
            #  print("\n new population[", j, "]", new_population)

            new_fitness = ackley(new_population)
            #  print("new fitness : ", new_fitness)
            #  print("fitness[", j, "]", fitness[j], "\n")

            #  print("new_fitness.all() < fitness[j].all() :", new_fitness < fitness[j])

            if new_fitness < fitness[j]:
                fitness[j] = new_fitness
                population[j] = trial_vector
                if new_fitness< fitness[best_index]:
                    best_index = j
                    best = new_population
        yield best, fitness[best_index]


for best, fitness in differntial_evolution(ackley, bounds):
    print("best = ", best, "fitness = ", fitness)

