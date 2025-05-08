import numpy as np
from deep.layer import Relu

if __name__ == "__main__":
    x = np.array([-1,0,2])
    relu = Relu()
    y = Relu.forward(x)
    print(y)
    dy = Relu.backward(np.ones_like(x))
    print(dy)