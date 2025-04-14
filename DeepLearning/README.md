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
	- 사용자의 입력이 들어가는 부분이다. 다중 분류로 가위,바위,보 중 2개(가위,보)를 골라 출력을 한 개만 하고 특성이 3개, 그러면 (2,3) 이 입력으로 들어간다. 
2. 히든층
	- 히든층은 가중치, (입력값 * 가중치) , 활성화의 구조로 구성되어 있다. 입력이 (2,3), 설정한 노드 수가 n개, 히든층이 50개 라고 하면 처음 가중치는 (입력값의 행 * n)  이후 일반적으로는 n * n 개의 의 가중치 50개를 생성한다. 이후 가중치, 입력값 * 가중치 + 편항 + 활성화 함수로 이동하면서 출력층까지 도달한다. 여기서 활성화 함수는 차원을 그대로 출력 시킨다. 만약 n이 10이라고 했을 때 (2,3) * (3,10) -> (2 * 10) * 50 이렇게 출력층까지 순전파를 진행한다. 
3. 출력층
	- 정답은 1개이다. 그러므로 출력은 1개이다. 그러면 (2,10) * (10,1) -> (2,1) 로 마지막 가중치가 설정될 것이다. 그러면 `([.8,.5])` 라고 출력이 나온다면 예측 과정에서는 나머지 값들이 필요 없기 때문에 0.8 에 해당하는 즉 가위의 확률이 젤 높기 때문에 0번 인덱스 : 즉 가위를 출력하는 것이다. 이러한 과정이 되기 까지 역전파라는 과정이 필요하며 `([.8,.5])` 값에 대해 연쇄법칙을 이용하여 가중치와 편항을 수정해나간다.
#### 순전파
 - 사용자의 입력이 입력층 -> 히든층 -> 출력층 으로 가중치와 활성화 함수에 의해 값이 변화하면서 사용자에게 출력이 될 때 까지의 과정을 의미한다. 그냥 입력부터 출력까지의 전 과정이라고 보면 된다.
#### 역전파
 - 학습과정에서 사용되는 과정으로 loss function 을 통해 오차를 구하고 미분의 연쇄법칙을 이용하여 가중치의 결과를 조정해나간다. 이 가중치를 조정하는 과정에는 하이퍼파라미터인 learning rate의 영향을 받는다. 줄여서 lr(학습률) 은 낮을수록 학습하는 과정은 빠르나 최적점에 도착하는 시간이 느리고 높을수록 학습하는 과정이 빨라 최적점을 지나치거나 발산하여 훈련과정에 훈련 데이터셋이 적합해져서 일반화를 하지 못하는 현상인 over fitting 이 발생할 수 있기 때문에 조절을 잘하는 것이 중요하다.
#### 경사하강법
- 역전파의 계산식인 $x_{new} = x_{old} - lr\frac{\delta e}{\delta x}$ 은 오차함수의 결과에 따라 차이에 대한 미분값을 구하고 이를 가중치에 적용하여 최적화 시키는 과정이다. 이를 통해 모델은 최적점에 맞춰가는 과정을 커친다.


### 오차역전파
#### 계산그래프
1. 수식을 한 단계식 푼 그래프로 복잡한 수식을 이해하기 쉽게 풀어낼 수 있다.
#### Affine
1. 순전파에서 수행하는 행렬곱을 기하학에서는 Affain transformation 이라고 한다.
```python
class Affine:
	def __init__(self,w,b):
		# w,b 는 이전의 w,b 를 저장하기 위한 그릇이다.
		self.w = w
		self.b = b
		self.dw = None
		self.db = None

	def forward(self,x, w):
		# 입력 받은 x, 입력 받은 가중치 w 의 합성곱 + 편항의 결과를 다음 노드로 전달한다.
		self.x = x
		self.w = w
		out = np.dot(x, w) + self.b
		return out

	def backward(self,dout):
		# dout은 n + 1의 편미분 x의 값이다. f(x,w) = xw 형태를 지닌다. 그러면 x에 대한 편미분은 w, w에 대한 편미분은 x이다.그러므로 가중치를 업데이트 하기 위해 x의 값이 필요하고, n - 1의 가중치 업데이트를 위한 x를 전달해주어야 하는 것이다.
		# 또한 편항은 가중치 전체의 합이기 때문에 z에 대한 편미분은 b인 것이다.
		dx = np.dot(dout, self.w.T)
		self.dw = np.dot(self.x.T, dout)
		self.db = np.sum(self.db, axis = 0)
		return dx
```