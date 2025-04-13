

### 손실 함수 (Loss function)
1. (SSE) Sum of Squres for Error
$$
E = \frac{1}{2}\sum_k^{}(y_k - t_k)^2
$$
```python
def sum_of_squares_for_error(y,t):
	return 0.5 * np.sum((y - t)**2)
```
1. (CEE) Cross Enpropy Error
$$
	E = -\sum_k^{}t_k\log{(y_k)}
$$
```python
def cross_enpropy_error(y,t):
	h = 1e-7
	return -np.sum(t * np.log(y + h))
```
- 파이썬으로 구현시 h = 1e-7 을 더해주는 이유는 ln(자연로그)에 0에 가까워질수록 마이너스 무한대로 발산하기 때문에 오류를 방지하기 위해 작은 값인 1e-7을 더해주는 것이다.
### 활성화 함수(Activate funtion)
1. Sigmoid
$$
	\sigma(x) = \frac{1}{1+e^{-x}}
$$
```python
def sigmoid(x):
	return 1 / (1 + np.exp(-x))
```
1. Softmax
$$
	\sigma(x) = \frac{1 + e^x}{\sum_k (1+e^x)}
$$
```python
def softmax(x):
	return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)))
```
- 파이썬으로 구현시 exp에 x의 최댓값을 빼주는데 이유는 지수함수의 결과가 너무 커져 오버플로우가 발생할 가능성이 있기 때문에 모든 exp에서  x의 최댓값을 빼주는 것이다. $e^{x - max(x)}$를 풀어쓴다면 $e^x / e^{max(X)}$ 이므로 등식의 성질에 따라 동일하게 적용된다.
1. ReLU
$$
		\sigma(x) = max(0,x)
		\begin{cases}
			x & \quad \text{if}\ x>0\\
			0 & \quad \text{if}\ x\leq0
		\end{cases}
$$
```python
def relu(x):
	return x if x > 0 else 0
```
1. Leaky ReLU
$$
\sigma(x) = max(ax, x) 
\begin{cases}
	\text{if} \ x \ > 0\\
	\text{if} \ x \ \leq 0
\end{cases}
$$
```python
def leaky_relu(x,a : float)
	return max(ax, x)
```
### 수치미분
1. 전방 미분
$$
	f(x) = \frac{f(x+h) - f(h)}{h}
$$
2. 후방 미분
$$
	f(x) = \frac{f(x) - f(x-h)}{h}
$$
3. 중앙 미분
$$
	f(x) = \frac{f(x+h) - f(x-h)}{2h}
$$
```python
def numerical difference(f, x):
	h = 1e-4
	return (f(x+h) - f(x-h)) / (2 * h)
```
- 1 ~ 3번 중 중앙 미분이 제일 정확도가 높기 때문에 역전파의 결과를 증명하는 기울기 확인 과정에 사용된다.. 또한 0으로 수렴하는 과정을 표현할 수 없기 때문에 가장 작은 값을 더해야 하는데 소수점 자리가 크면 결과가 틀려질 수 있기 때문에 1e-4를 적당한 값으로 이용한다.
### 인공신경망 학습 순서
#### 구조
1. 입력층
	- 사용자의 입력이 들어가는 첫 부분이다. 가장 유명한 mnist의 샘플로 예를 들어보겠다. 샘플의 크기는 28*28 pixel 로 이루어진 이미지이다. 이것을 1차원으로 변경하면 784가 되고 입력층의 노드는 784개가 되는 것이다.
2. 히든층
	- 히든층이 깊을수록 시간과 computing power가 더 많이 소모되지만 모델의 성능이 좋아진다. 다만 깊어진다고 좋은 것은 아니고 적절한 파라미터 설정 및 활성화 함수, 역전파 등 을 잘 선정해야 한다. 보통 이진 분류에서는 sigmoid 함수를 쓰고  다차원 분류 문제에서는 gradient vanashing 이 발생하기 때문에 ReLU를 사용했지만 이마저 음수값의 경우 전부 0으로 변환해버린다는 문제가 있어 변형함수인 Leaky ReLU 함수가 등장하게 되었다.
3. 출력층
	- 1번 입력층을 이어 예를 들겠다. mnist 는  0 ~ 9까지의 손글씨 그림으로 이루어져있다. 그러면 우리가 예측해야 하는 결과는 0 ~ 9, 즉 10개가 되는 것이다. 그러므로 이 예시에서는 출력층의 노드는 10개가 된다. 이처럼 얻고자 하는 결과의 수에 따라 출력층을 정하면 된다.
#### 순전파
 - 사용자의 입력이 입력층 -> 히든층 -> 출력층 으로 가중치와 활성화 함수에 의해 값이 변화하면서 사용자에게 출력이 될 때 까지의 과정을 의미한다. 그냥 입력부터 출력까지의 전 과정이라고 보면 된다.
#### 역전파
 - 학습과정에서 사용되는 과정으로 loss function 을 통해 오차를 구하고 미분의 연쇄법칙을 이용하여 가중치의 결과를 조정해나간다. 이 가중치를 조정하는 과정에는 하이퍼파라미터인 learning rate의 영향을 받는다. 줄여서 lr(학습률) 은 낮을수록 학습하는 과정은 빠르나 최적점에 도착하는 시간이 느리고 높을수록 학습하는 과정이 빨라 최적점을 지나치거나 발산하여 훈련과정에 훈련 데이터셋이 적합해져서 일반화를 하지 못하는 현상인 over fitting 이 발생할 수 있기 때문에 조절을 잘하는 것이 중요하다.
#### 경사하강법
- 역전파의 계산식인 $x_{new} = x_{old} - lr\frac{\delta e}{\delta x}$ 은 오차함수의 결과에 따라 차이에 대한 미분값을 구하고 이를 가중치에 적용하여 최적화 시키는 과정이다. 이를 통해 모델은 최적점에 맞춰가는 과정을 커친다.