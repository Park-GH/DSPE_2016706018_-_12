# DSPE_2018706062_박건희_12

import numpy as np
import matplotlib.pylab as plt

fig = plt.figure()              # figure 객체 생성
ax = fig.add_subplot(1, 1, 1)   # 1X1개의 서브플롯을 추가하고, 첫번째 서브 플롯을 사용

x = np.arange(-10, 10, 0.1)     # x값을 -10 ~ 10까지 0.1단위로 입력

# w는 변수 0.5 ~ 3.0
for w in np.arange(0.5, 3, 0.5):
   f = 1/(1 + np.exp(-w*x))
   ax.plot(x, f)

ax.set_xticks(range(-10, 10))   # x축 눈금 범위 지정
ax.set_yticks(range(0, 2))      # y축 눈금 범위 지정
ax.set_xlabel('x')              # x축 라벨 지정
ax.set_ylabel('f(x)')           # y축 라벨 지정
plt.show()