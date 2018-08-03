import flex
import random


class DifferentialEvolutionOptimizer(object):

    def __init__(self,
                 evaluator,
                 population_size=50,
                 f=None,
                 cr=0.9,
                 eps=1e-2,
                 n_cross=1,
                 max_iter=10000,
                 monitor_cycle=200,
                 out=None,
                 show_progress=False,
                 show_progress_nth_cycle=1,
                 insert_solution_vector=None,
                 dither_constant=0.4):
        self.dither = dither_constant
        self.show_progress = show_progress
        self.show_progress_nth_cycle = show_progress_nth_cycle
        self.evaluator = evaluator
        self.population_size = population_size
        self.f = f
        self.cr = cr
        self.n_cross = n_cross
        self.max_iter = max_iter
        self.monitor_cycle = monitor_cycle
        self.vector_length = evaluator.n
        self.eps = eps
        self.population = []
        self.seeded = False
        if insert_solution_vector is not None:
            assert len(insert_solution_vector) == self.vector_length
            self.seeded = insert_solution_vector
        for ii in range(self.population_size):
            self.population.append(flex.double(self.vector_length, 0))
        self.scores = flex.double(self.population_size, 1000)
        self.optimize()
        self.best_score = flex.min(self.scores)
        self.best_vector = self.population[flex.min_index(self.scores)]
        self.evaluator.x = self.best_vector
        if self.show_progress:
            self.evaluator.print_status(
                flex.min(self.scores),
                flex.mean(self.scores),
                self.population[flex.min_index(self.scores)],
                'Final')

    def optimize(self):
        # initialise the population please
        self.make_random_population()
        # score the population please
        self.score_population()
        converged = False
        monitor_score = flex.min(self.scores)
        self.count = 0
        while not converged:
            self.evolve()
            location = flex.min_index(self.scores)
            if self.show_progress:
                if self.count % self.show_progress_nth_cycle == 0:
                    # make here a call to a custom print_status function in the evaluator function
                    # the function signature should be (min_target, mean_target, best vector)
                    self.evaluator.print_status(
                        flex.min(self.scores),
                        flex.mean(self.scores),
                        self.population[flex.min_index(self.scores)],
                        self.count)

            self.count += 1
            if self.count % self.monitor_cycle == 0:
                if (monitor_score-flex.min(self.scores)) < self.eps:
                    converged = True
                else:
                    monitor_score = flex.min(self.scores)
            rd = (flex.mean(self.scores) - flex.min(self.scores))
            rd = rd*rd/(flex.min(self.scores)*flex.min(self.scores) + self.eps)
            if rd < self.eps:
                converged = True

            if self.count >= self.max_iter:
                converged = True

    def make_random_population(self):
        for ii in range(self.vector_length):
            delta = self.evaluator.domain[ii][1]-self.evaluator.domain[ii][0]
            offset = self.evaluator.domain[ii][0]
            random_values = flex.random_double(self.population_size)
            random_values = random_values*delta+offset
            # now please place these values ni the proper places in the
            # vectors of the population we generated
            for vector, item in zip(self.population, random_values):
                vector[ii] = item
        if self.seeded is not False:
            self.population[0] = self.seeded

    def score_population(self):
        for vector, ii in zip(self.population, range(self.population_size)):
            tmp_score = self.evaluator.target(vector)
            self.scores[ii] = tmp_score

    def evolve(self):
        for ii in range(self.population_size):
            rnd = flex.random_double(self.population_size-1)
            permut = flex.sort_permutation(rnd)
            # make parent indices
            i1 = permut[0]
            if i1 >= ii:
                i1 += 1
            i2 = permut[1]
            if i2 >= ii:
                i2 += 1
            i3 = permut[2]
            if i3 >= ii:
                i3 += 1
            #
            x1 = self.population[i1]
            x2 = self.population[i2]
            x3 = self.population[i3]

            if self.f is None:
                use_f = random.random()/2.0 + 0.5
            else:
                use_f = self.f

            vi = x1 + use_f*(x2-x3)
            # prepare the offspring vector please
            rnd = flex.random_double(self.vector_length)
            permut = flex.sort_permutation(rnd)
            test_vector = self.population[ii].deep_copy()
            # first the parameters that sure cross over
            for jj in range(self.vector_length):
                if jj < self.n_cross:
                    test_vector[permut[jj]] = vi[permut[jj]]
                else:
                    if rnd[jj] > self.cr:
                        test_vector[permut[jj]] = vi[permut[jj]]
            # get the score please
            test_score = self.evaluator.target(test_vector)
            # check if the score if lower
            if test_score < self.scores[ii]:
                self.scores[ii] = test_score
                self.population[ii] = test_vector

    def show_population(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for vec in self.population:
            print(list(vec))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


class TestFunction(object):
    def __init__(self):
        self.x = None
        self.n = 9
        self.domain = [(-100, 100)]*self.n
        self.optimizer = DifferentialEvolutionOptimizer(self, population_size=100, n_cross=5)
        assert flex.sum(self.x*self.x) < 1e-5


def target(self, vector):
    tmp = vector.deep_copy()
    result = (flex.sum(flex.cos(tmp*10))+self.n+1)*flex.sum(tmp*tmp)
    return result


class TestRosenbrockFunction(object):
    def __init__(self, dim=5):
        self.x = None
        self.n = 2*dim
        self.dim = dim
        self.domain = [(1, 3)]*self.n
        self.optimizer = DifferentialEvolutionOptimizer(self, population_size=min(self.n*10, 40), n_cross=self.n,
                                                        cr=0.9, eps=1e-8, show_progress=True)
        print(list(self.x))

        for x in self.x:
            assert abs(x-1.0) < 1e-2


def target(self, vector):
    tmp = vector.deep_copy()
    x_vec = vector[0:self.dim]
    y_vec = vector[self.dim:]
    result = 0
    for x, y in zip(x_vec, y_vec):
        result += 100.0*((y-x*x)**2.0) + (1-x)**2.0
        # print list(x_vec), list(y_vec), result
    return result


def print_status(self, mins, means, vector, txt):
    print(txt, mins, means, list(vector))


def run():
    random.seed(0)
    flex.set_random_seed(0)
    TestRosenbrockFunction(1)
    print("OK")


if __name__ == "__main__":
    run()
