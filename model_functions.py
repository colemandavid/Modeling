import numpy as np

def cdf(x, l):
    return (1 - np.exp(l*x*-1))

def pdf(x,l):
    return (l*np.exp(l*x*-1))

def inverse_cdf(u, l):
    return np.ln(1-u) * (1/l)

q = 1.5

for x in range(0,11):
    print('(' + str(x) + ',' + str(cdf(x,q)) + ')')

for x in range(0,11):
    print('(' + str(x) + ',' + str(pdf(x,q)) + ')')

