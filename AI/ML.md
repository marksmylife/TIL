## NaN(결측치) 찾아서 다른 값 변경
```python
# 기존 avalone 데이터는 결측치가 존재하지 않는다.
abalone_df.isnull().sum().sum()

# 가상으로 결측치 생성
nan_abalone_df = abalone_df.copy()
nan_abalone_df.loc[2,'length'] = np.nan

# 결측치를 특정 값으로 채우기
zero_abalone_df = nan_abalone_df.fillna(0)
zero_abalone_df

# 결측치를 결측치가 속한 컬럼의 평균값으로 대체하기
nan_abalone_df.mean()

# 결측치에 평균값 넣기
nan_abalone_df.fillna(nan_abalone_df.mean())
```

## apply 함수 활용
DataFrame타입의 객체에서 호출가능한 apply함수에 대해 살펴보자.
본인이 원하는 행과 열에 연산 혹은 function을 적용할 수 있다.
열 기준으로 집계하고 싶은 경우 axis=0
행 기준으로 집계하고 싶은 경우 axis=1




## 컬럼 내 유니크한 값 뽑아서 갯수 확인

# 기초부터 쌓아가는 머신러닝 #3 : matplotlib과 seaborn 라이브러리를 활용한 데이터 시각화
* 시각화 라이브러리
  * matplotlib : 파이썬으로 기본적인 차트들을 쉽게 그릴 수 있도록 도와주는 시각화 라이브러리
  * seaborn : matplotlib 기반으로 만들어진 통계 데이터 시각화 라이브러리
```python
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

plt.rcParams['figure.figsize']=[10,8]
sns.set(style='whitegrid')
sns.set_palette('pastel')
warnings.filterwarnings('ignore')


# % 한글이 깨지는 경우 %
from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
matplotlib.rcParams['axes.unicode_minus'] = False 


# Loding "tips" dataset from seaborn
tips = sns.load_dataset('tips')
tips.head()

# 데이터를 봤으면 반듯이 형태 확인
tips.shape 
 ```



## 기초부터 쌓아가는 머신러닝 #4 :  선형회귀 이론 및 실습
* 선형회귀는 하나 이상의 특성과 연속적인 타깃 변수 사이의 관계를 모델링 하는 것
* 연속적인 출력 값을 예측하는 것
* 특성이 하나인 선형 모델 공식
  Y = W0 + W1*X
  where W0 : y축 절편, W1 : 특성의 가중치
* ✔ 목적 : 특성과 타깃 사이의 관계를 나타내는 선형 방정식의 가중치(W)를 학습하는 것
---
* 선형 회귀 모델의 훈련과 비용함수
  * 모델의 훈련이란
    ✔ 모델이 훈련 데이터에 잘 맞도록 모델 파라미터를 설정하는 것
    ✔ 모델이 훈련 데이터에 얼마나 잘 들어맞는지 측정해야 함

* 모델 훈련에 필요한 비용함수 종류
  * ✔ MSE (Mean Squared Error)
    1. 회귀 모델의 주요 손실 함수
    2. 참값과 예측값의 차이인 오차들의 제곱 평균으로 정의
    3. 제곱을 해주기 때문에 이상치(outlier)에 민감

  * ✔ MAE (Mean Absolute Error)
    1. 참값과 예측값의 차이인 오차들의 절대값 평균
    2. MSE보다 이상치에 덜 민감

  * ✔ RMSE (Root Mean Squared Error)
    1. MSE에 root을 취해 준 것
    2. 참값과 비슷한 값으로 변환하기 때문에 해석이 쉬워짐

***보통 quadratic(2차 곡선형태) 형태의 미분 편의성이 좋기 때문에, 회귀 모형의 비용함수로 MSE를 많이 사용***
---






## .coef
* *머신 러닝 모델에서 사용되는 용어
* 주로 선형 회귀(Linear Regression) 또는 로지스틱 회귀(Logistic Regression)와 같은 회귀 모델에서 사용
* 모델에서의 가중치(weight) 또는 계수(coefficient)를 나타냅니다.
* 선형 회귀 모델에서 `.coef`는 각 특성의 계수를 반환
* 이러한 계수는 각 특성이 예측값에 어떻게 기여하는지를 나타내며, 양수인 경우 해당 특성이 예측값을 증가시키고 음수인 경우 감소시킵니다. 또한, 계수의 크기는 해당 특성의 중요도를 나타냅니다
* `.coef` 값을 분석하면 모델이 어떤 특성을 중요하게 여기고 어떤 특성을 무시하는지를 이해할 수 있습니다.