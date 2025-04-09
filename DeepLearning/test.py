<<<<<<< HEAD
import os,sys
sys.path.append(os.pardir)
import numpy as np

def softmax(x):
    return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)))

def cross_entropy_error(y,t):
    h = 1e-7
    return -np.sum(t*np.log(y+h))
=======
import numpy as np
>>>>>>> 8f87a1cc8bfbe9979473fbcc6e6e676ee8299bc0





# 오차 함수

def sum_squares_error(y,t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y,t):
    h = 1e-7
    return - np.sum(t * np.log(y+h))


# 활성화 함수
def sigmoid(x):
    return 1  / (1 + np.exp(-x))

def softmax(x):
    return np.exp(x - np.max(x)) / np.sum(x - np.max(x))

def centeral_diff(f,x):
    h = 1e-4
<<<<<<< HEAD
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
=======
    return f(x+h) - f(x-h) / 2*h
>>>>>>> 8f87a1cc8bfbe9979473fbcc6e6e676ee8299bc0
