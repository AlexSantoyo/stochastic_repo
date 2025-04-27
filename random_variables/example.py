# to write some examples

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import random_variables as myrvs

n = 10
p = 0.75
binom1 = myrvs.BinomialRV(n,p)

print(binom1.expectation())
print(binom1.variance())

binom_pmf = binom1.pmf()

plt.bar(range(11),binom_pmf(range(11)))
plt.show()