import os,sys
sys.path.append(os.pardir)
import numpy as np

def softmax(x):
    return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)))

def cross_entropy_error(y,t):
    h = 1e-7
    return -np.sum(t*np.log(y+h))

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp = x[idx]

        x[idx] = tmp + h
        fwh1 = f(x)

        x[idx] = tmp - h
        fwh2 = f(x)

        grad[idx] = (fwh1 - fwh2) / (2*h)
        x[idx] = tmp
        
    return grad

class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y,t)

        return loss
net = SimpleNet()

print(net.W)

x = np.array([0.6,0.9])
p = net.predict(x)

print(p)

t = np.array([0,0,1])
net.loss(x,t)

def f(W):
    return net.loss(x,t)

dw = numerical_gradient(f, net.W)
