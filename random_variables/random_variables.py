# We could create a parent class for a generic random variable,
# so that each r.v. can be a child class

# imports
import numpy as np
from scipy.stats import binom

# this will be the parent class
class RandomVariable:
    def __init__(self):
        pass

# let's try a few simple examples first, to see how to better define the parent class...

class BinomialRV:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.q = 1 - p

    def expectation(self):
        return self.n * self.p
    
    def variance(self):
        return self.n * self.p * self.q
    
    def mgf(self):
        return lambda t: (self.q + self.p * np.exp(t))**self.n
    
    def pmf(self):
        spy_binom = binom(self.n,self.p)
        return lambda x: spy_binom.pmf(x)