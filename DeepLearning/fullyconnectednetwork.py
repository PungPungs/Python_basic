import numpy as np
from collections import OrderedDict

def cross_entropy_error(y,t):
    h = 1e-7
    return -np.sum(t * np.log(y + h))

def softmax(x):
    exp_x = x - np.max(x)
    return exp_x / np.sum(exp_x)

class Affine:
    def __init__(self,w,b):
        self.W = w
        self.b = b
        self.dx = None
        self.orignal_x_shape = None

    def forward(self, x):
        self.orignal_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out
    
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout,axis=0)

        dx = dx.reshape(*self.orignal_x_shape)

        return dx
    
class softmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None


    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    
    def backward(self, dout = 1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx

class FullyConnectedNetwork:
    def __init__(self, feature_size, output_size, hidden_size):
        self.params = {}
        self.layer = OrderedDict()
        hidden_layer = 5

        self.params['W1'] = np.random.rand(feature_size, hidden_size)
        self.params['b1'] = np.random.rand(hidden_size)
        for i in range(2,hidden_layer):
            self.params[f'W{i}'] = np.random.rand(hidden_size,hidden_size)
            self.params[f'b{i}'] = np.zeros(hidden_size)
        self.params[f'W{hidden_layer}'] = np.random.rand(hidden_size, output_size)
        self.params[f'b{hidden_layer}'] = np.zeros(output_size)

        for i in range(1,hidden_layer+1):
            self.layer[f'Affine{i}'] = Affine(self.params[f'W{i}'],self.params[f'b{i}'])      
        self.activeLayer = softmaxWithLoss()

    def predict(self,x):
        self.x = np.copy(x)
        for layer in self.layer.values():
            x = layer.forward(x)
        return x
    
    def loss(self,x,t):
        self.y = self.predict(x)
        self.t = t
        loss = self.activeLayer.forward(self.y,t)
        return loss
    
    def backward(self):
        self.activeLayer.backward()

if __name__ == "__main__":
    x = np.random.randn(3,5)
    network = FullyConnectedNetwork(5,3,5)
    result = network.predict(x)
    result = network.backward()
    print(result)