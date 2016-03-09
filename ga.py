#!/usr/bin/env python3
# G E N E T I C   A L G O R I T H M

# Project   Genetic Algorithm with Python
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      29.02.2016
# Python    3.5.1
# License   MIT

import math
import random

class Population:

    def __init__(self, popsize=1000, veclength=20, domain=[(100,200)]):
        # Population Parameters
        self.popsize = popsize
        self.veclength = veclength
        self.domain = domain * veclength
        self.population = self.create_population()

    def create_population(self):
        """ Build Initial Population """
        population = [self.create_vector() for _ in range(self.popsize)]
        return population

    def create_vector(self):
        """ Create Random Vector """
        vec = [random.randint(self.domain[i][0],self.domain[i][1])
               for i in range(self.veclength)]
        return vec

    def get_ranked_population(self):
        """ Get Score of Population, Rank Population based on Scores """
        pop_score = [(self.get_vec_score(vec),vec) for vec in self.population]
        pop_score.sort()
        ranked_pop = [vec for (score,vec) in pop_score]
        # Print current best
        # print(pop_score[0][0])
        return ranked_pop

    @staticmethod
    def get_vec_score(vec):
        """ Get Score of Vector """
        vec_score = 0
        for v in vec:
            vec_score += (v + 0.1) * math.e / 3
        return int(vec_score)

    def evolve(self, elite=0.2, maxiter=20, mutprob=0.4):
        """ Evolve Population """
        # Evolve Parameters
        self.elite = elite
        self.maxiter = maxiter
        self.mutprob = mutprob
        # topelite: num of survivors of a generation
        self.topelite = int(elite * self.popsize)
        
        for i in range(self.maxiter):
            ranked_pop = self.get_ranked_population()
            self.population = ranked_pop[0:self.topelite]

            # Fill Population with Survivors Muted and Crossovered Forms
            while len(self.population) < self.popsize:
                if random.random() < self.mutprob:
                    # Mutation
                    c = random.randint(0,self.topelite-1)
                    self.population.append(self.mutate(self.population[c]))
                else:
                    # Crossover
                    c1 = random.randint(0,self.topelite-1)
                    c2 = random.randint(0,self.topelite-1)
                    self.population.append(
                        self.crossover(self.population[c1], self.population[c2]))

        # Return Optimal Vector
        return self.population[0]

    def mutate(self, r):
        """ Mutate Vector """
        i = random.randint(0,self.veclength-1)
        x = random.randint(self.domain[i][0],self.domain[i][1])
        r[i] = x
        return r

    def crossover(self, r1, r2):
        """ Crossover 2 Vectors """
        i = random.randint(1,self.veclength-2)
        return r1[0:i] + r2[i:]

