import numpy as np

X = np.array([1.0, 0.5])
W1 = np.array([[0.1,.3,.5],[.2,.4,.6]])
B1 = np.array([.1,.2,.3])


print(X.shape, W1.shape, B1.shape)

A1 = np.dot(X,W1) + B1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

Z1 = sigmoid(A1)



W2 = np.array([[.1,.4],[.2,.5],[.3,.6]])
B2 = np.array([.1,.2])

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)


W3 = np.array([[.1,.3],[.2,.4]])
B3 = np.array([.1,.2])
A3 = np.dot(Z2,W3) + B3
Y = A3

print(A1)
print(Z1)
print(A2)
print(Z2)
print(Y)

#### softmax

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

a = np.array([.3,2.9,4.])
print(softmax(a))

a = np.array([1010, 1000, 990])
print(softmax(a))
#### softmax 함수의 개선
def softmax(x):
    return np.exp(x - max(x)) / np.sum(np.exp(x - max(x)))


a = np.array([.3,2.9,4.])
print(softmax(a))