# We could create a parent class for a generic random variable,
# so that each r.v. can be a child class

# imports
import numpy as np
from scipy.stats import binom
# from IPython.display import display, Math, Latex

# this will be the parent class
class RandomVariable:
    """
    General class for a Random Variable
    """
    def __init__(self, rv_name = None, **params):
        self.rv_name = rv_name
        self.params = params

    def __str__(self):
        return(f"A {self.rv_name} random variable instance.")

# let's try a few simple examples first, to see how to better define the parent class...

class BinomialRV(RandomVariable):
    """
    Class of a Binomial Random Variable.
    """
    def __init__(self, n = 1, p = 0.5):
        """
        Parameters:
        n, number of independent Bernoulli experiments
        p, success probability on each Bernoulli experiment
        """
        self.rv_name = 'Binomial'
        self.n = n
        self.p = p
        self.q = 1 - p

        super().__init__(rv_name=self.rv_name, n = 1, p = 0.5)

    def expectation(self):
        """
        E(X) = n*p
        """
        # Latex(r'$\mu = \frac{1}{n} \sum_{i=1}^n x_i$')
        # display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))

        return self.n * self.p
    
    def variance(self):
        """
        Var(X) = n*p*q
        """
        return self.n * self.p * self.q
    
    def mgf(self):
        return lambda t: (self.q + self.p * np.exp(t))**self.n
    
    def pmf(self):
        spy_binom = binom(self.n,self.p)
        return lambda x: spy_binom.pmf(x)