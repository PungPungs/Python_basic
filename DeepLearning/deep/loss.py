from deep.base import Module
from deep.layer import Softmax
import numpy as np
    
class CrossEntropy(Module):
    def __init__(self):
        self.y = None
        self.t = None

    def forward(self,y,t):
        self.t = t
        self.y = y
        return -np.sum(t * np.log(y + 1e-7))

    def backward(self):
        return (self.y - self.t)
    
class SoftmaxWithLoss(Module):

    def __init__(self):
        self.cross_entropy = CrossEntropy()
        self.softmax = Softmax()
        self.y = None
        self.t = None

    def forward(self,x, t):
        self.t = t
        self.y = self.softmax.forward(x)
        return self.cross_entropy.forward(self.y,t)

    def backward(self):
        batch = self.t.shape[0]
        return (self.y - self.t) / batch
    
