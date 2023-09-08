---
title: "[NIPA]AI+웹개발 취업캠프 SW심화 7주차 5회"
excerpt: "데일리 학습일지"

categories:
  - Categories2
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories2/post-name-here-21/

toc: true
toc_sticky: true

date: 2023-09-01
last_modified_at: 2023-09-01
---

## 🦥 본문



```python
## 패션 MNIST


첫 번째 줄은 tensorflow 라이브러리에서 keras 모듈을 가져옵니다.

두 번째 줄은 keras.datasets 모듈의 load_data() 함수를 사용하여 Fashion-MNIST 데이터 세트를 로드합니다.

load_data() 함수는 두 개의 튜플을 반환합니다. (train_input, train_target) 튜플은 훈련 이미지와 레이블을 포함하고, (test_input, test_target) 튜플은 테스트 이미지와 레이블을 포함합니다.

from tensorflow import keras

(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()


데이터의 모양은 다음과 같은 세 가지 요소로 구성됩니다.

샘플의 개수,
특성의 개수,
채널의 개수
* 이 경우, 훈련 이미지의 모양은 (60000, 28, 28)입니다. 이는 60,000개의 샘플이 있고, 각 샘플은 28x28 픽셀의 흑백 이미지라는 것을 의미합니다. 훈련 레이블의 모양은 (60000,)입니다. 이는 60,000개의 레이블이 있다는 것을 의미합니다.

* 테스트 이미지의 모양은 (10000, 28, 28)입니다. 이는 10,000개의 샘플이 있고, 각 샘플은 28x28 픽셀의 흑백 이미지라는 것을 의미합니다. 테스트 레이블의 모양은 (10000,)입니다. 이는 10,000개의 레이블이 있다는 것을 의미합니다.

print(train_input.shape, train_target.shape)

print(test_input.shape, test_target.shape)

import matplotlib.pyplot as plt
# 10개의 subplot을 생성합니다.
fig, axs = plt.subplots(1, 10, figsize=(10,10))

# 훈련 이미지의 첫 번째 10개를 subplot에 표시합니다.
for i in range(10):
  axs[i].imshow(train_input[i], cmap='gray_r')
  axs[i].axis('off')

# 그래프를 표시합니다.
plt.show()

print([train_target[i] for i in range(10)])
#  Fashion-MNIST 데이터 세트의 훈련 레이블의 첫 번째 10개를 출력

이 코드는 NumPy의 unique() 함수를 사용하여 Fashion-MNIST 데이터 세트의 훈련 레이블의 고유한 값과 개수를 반환합니다.

np.unique() 함수는 입력 배열에서 고유한 값을 반환합니다. return_counts=True 매개변수를 지정하면 각 고유한 값에 대한 개수를 함께 반환합니다.

이 코드는 Fashion-MNIST 데이터 세트의 훈련 레이블에는 0부터 9까지의 10가지 고유한 값이 있으며, 각 값에 6000개의 레이블이 있음을 보여줍니다. 즉, 각 의류 유형에는 6000개의 이미지가 있습니다.

결과값 해석

첫 번째 배열은 고유한 값을 나타냅니다.
두 번째 배열은 각 고유한 값에 대한 개수를 나타냅니다.
이 결과값은 Fashion-MNIST 데이터 세트의 균형 잡힌 분포를 보여줍니다. 각 의류 유형에는 동일한 수의 이미지가 있습니다.

추가적인 주석으로는 다음과 같은 내용이 있습니다.

np.unique() 함수는 데이터 세트의 레이블을 정리하는 데 유용한 도구입니다.
return_counts=True 매개변수는 데이터 세트의 균형 잡힌 분포를 확인하는 데 유용한 정보를 제공합니다.

import numpy as np

print(np.unique(train_target, return_counts=True))

## 로지스틱 회귀로 패션 아이템 분류하기

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)

print(train_scaled.shape)

from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log', max_iter=5, random_state=42)

scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score']))

## 텐서플로와 케라스

import tensorflow as tf
from tensorflow import keras

## 인공신경망으로 모델 만들기

from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42
)

print(train_scaled.shape, train_target.shape)

print(val_scaled.shape, val_target.shape)

dense = keras.layers.Dense(10, activation='softmax', input_shape=(784,))

model = keras.Sequential(dense)

## 인공신경망으로 패션 아이템 분류하기

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')


print(train_target[:10])

model.fit(train_scaled, train_target, epochs=5)

model.evaluate(val_scaled, val_target)
```






  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
