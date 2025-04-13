import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

x = np.array([.1,.2,.3])
w = np.zeros([3,3]) + 0.1

z = x.dot(w)
print(z)

a = sigmoid(z)
print(a)

w2 = np.zeros([3,2]) + 0.2
z2 = a.dot(w2)
print(z2)
a2 = sigmoid(z2)
print(a2)