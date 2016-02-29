# genetic_algorithm
**Genetic algorithm implementation with Python.**

### About Genetic Algorithms
In the field of artificial intelligence, a genetic algorithm (GA) is a search heuristic that mimics the process of natural selection. This heuristic is routinely used to generate useful solutions to optimization and search problems. Genetic algorithms belong to the larger class of evolutionary algorithms (EA), which generate solutions to optimization problems using techniques inspired by natural evolution, such as inheritance, mutation, selection, and crossover.
[Read more on Wikipedia...](https://en.wikipedia.org/wiki/Genetic_algorithm)

### Usage

**Before you start...**

If you would like to use genetic algorithm in order to find the optimal solution, you should do 2 things.

* **Specify the number of input parameters and the limits (min,max) of them.**
For example:
```Python
vec = [(0,10), (-0.5,0.5), (34,56)]
```
In this case we have got 3 input parameters and they can change their values between the given range.

* **We would like to find the best combinations of these input parameters. Thus we need to define the way we are able to calculate the score of a given parameter set.**
For example:
```Python
# Input parameters
v = [4, 0.3, 39]

# Calculate score
def get_vec_score(vec):
    """ Get Score of Vector """
    vec_score = 0
    vec_score = vec[0] * 2 + vec[1] ** 6 / vec[2]
    return int(vec_score)
    
# Calculate score for v
>>> get_vec_score(v)
>>> 8
```

If you would like to solve a given problem, you should change the way, how we calculate the score of a the vectors.
So open gp.py and look for ```get_vec_score``` function and adapt it to suit your needs.


**Import module**
```Python
>>> import ga
``` 

**Create new population**
```Python
>>> new_population = ga.Population(popsize=100, veclength=5, domain=[(0,1000)])
```

You can change the default parameters of the population.
* popsize
  * Initial size of the population (number of vectors)
* veclenght
  * Length of a vector in the population
* domain = [0,1000] * veclength
  * Limits of the range for all elements of a vector

**Start the evolution of the population and get the *optimal* result vector**
```Python
>>> new_population.evolve(elite=0.2, maxiter=20, mutprob=0.4)
[7, 2, 1, 135, 48]
```

You can customize the evolution process also.
* elite
  * Percentage ratio of survivors
* maxiter
  * Number of generations of a population
* mutprob
  * Probability of Mutation over Crossover in a vector
