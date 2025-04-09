import numpy as np





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
    return f(x+h) - f(x-h) / 2*h
