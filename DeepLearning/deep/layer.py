from deep.base import Module
import numpy as np

class Relu(Module):

    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = np.copy(x)
        out[self.mask] = 0
        return out

    def backward(self, dout):
        dx = np.copy(dout)
        dx[self.mask] = 0
        return dx
    
class Leaky_Relu(Module):
    def __init__(self, alpha):
        self.alpha = alpha
        self.mask = None


    def forward(self, x):
        x = (0 <= x)
        out = np.copy(x)
        out[self.mask] *= self.alpha
        return out
    
    def backward(self, dout):
        dx = np.ones_like(dout)
        dx[self.mask] = self.alpha
        return dx * dout


class Sigmoid(Module):
    def __init__(self):
        self.out = None

    def forward(self, x):
        self.out = 1 / (1 + np.exp(-x))
        return self.out
    
    def backward(self,dout):
        return dout * self.out * (1 - self.out)
    
class Softmax(Module):
    def __init__(self):
        self.out = None

    def forward(self,x):
        x -= np.max(x,axis = 1,keepdims = True)
        exp_x = np.exp(x)
        self.out = exp_x / np.sum(exp_x, axis=1, keepdims=True)
        return self.out
    
class Affine(Module):
    def __init__(self,W,b):
        self.W = W
        self.b = b
        self.dw = None
        self.db = None

    def forward(self, x):
        self.x = np.copy(x)
        self.out = np.dot(x,self.W) + self.b
        return self.out
    
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dw = np.dot(self.x.T,dout)
        self.db = np.sum(dout, axis=0)
        return dx
    
    def update(self, lr):
        self.W -= lr * self.dw
        self.b -= lr * self.db