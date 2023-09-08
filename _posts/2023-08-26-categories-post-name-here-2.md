---
ㄴtitle: "[NIPA]AI+웹개발 취업캠프 SW심화 6주차 6회"
excerpt: "위클리 학습일지"

categories:
  - Categories2
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories2/post-name-here-16/

toc: true
toc_sticky: true

date: 2023-08-26
last_modified_at: 2023-08-26
---

## 🦥 인공지능 AI 능력시험 AICE Basic 1/2 

## AI의 이해

* 최적의 의사결정을 위한 AI
* 인공지능 - 모델, binary, epoch, category, train/test, 정확도, 훈련, Feature(X), 알고리즘, Label(Y), Numeric
* 머신러닝 - 지도학습, 비지도학습, 분류, 회귀, 군집화, 강화학습
* 딥러닝 - 인공신경망, 과적합, DNN, CNN, RNN, GAN, xAI
* 개발도구/언어 - Python, 라이브러리, 오픈소스, Tensorflow, Keras, 사이킷런 + 파이토치
* 기타 - TTS, BERT, STT, Computer Vision, NLP, Ko-BERT

#### 인공지능 - 알고리즘으로 데이터를 학습(Train)하여 모델을 만드는 기술, 데이터(Input Data) -> 알고리즘(머신러닝,딥러닝) -> 모델(f(x))

#### 기계에 부여하는 명령을 만드는 직업과 달리, 알고리즘으로 데이터를 학습하여 판단이나 예측을 하는 기술

#### 규칙, 데이터 -> 전통적인 프로그래밍 방식 -> 해답

#### 데이터, 해답 -> 머신 러닝 -> 규칙

#### AI모델링 자동화 플랫폼 - main.ai, AIDU ez, SAMSUNG SDS Brightics, AI Suite

#### 오픈소스 라이브러리

#### 

#### 인공지능 - 계산 학습 등 인간의 지적능력을 컴퓨터를 통해 구현하는 기술

#### 머신러닝 - 특정 부분을 스스로 학습해 성능을 향상

#### 딥러닝 - 인간의 뉴런과 비슷한 인공신경망으로 정보를 처리



### 머신러닝 

* #### 지도학습 Supervised Learning - Task Driven(Predict next value), 

  분류 ㅁ input -> 분류기 -> output  - R,G,B 범주형 데이터를 출력
  회귀 몸무게가 X인 사람의 키, 수치형 데이터를 출력
  Labeled observations Features ex(지역, 층수, 엘리베이터유무, 평수, 건축년도 등), Label ex(부동산 매매 가격) 
  -> Trainig set -> Machine learner -> Prediction model
  -> Test set -> Prediction model 
  --> prediction model -> stats(통계)
  Machine learner는 Training set을 학습하여 Prediction model을 생성 
  Prediction model은 Test set을 사용하여 성능을 평가 
  성능 평가는 주로 통계적 방법을 사용하여 수행됩니다. 
  예를 들어, **정확도**, **재현율**, **F1 점수** 등의 지표를 사용하여 Prediction model의 예측 정확도를 평가

  #### 응용분야 - 분류, 회귀 -> 위험 평가, 예측

* #### 비지도학습 Unsupervised Learning - Data Driven(Identify Clusters) 군집화(Clustering) 연관

  출력데이터(Label, Y, 정답)없이 입력데이터만 주고 패턴으로 학습
  과일 Input data -> 데이터의 특성 스스로 파악 -> 색
  입력데이터만 주어졌을 때 모델 스스로 데이터 안에서 어떠한 관계를 찾아 내는 것, 정답데이터가 주어지지 않는다는 점에서 지도학습과 차이점을 보임

  #### 응용분야 - 군집화, 연관 -> 상품추천, 특이사항 탐지

* #### 강화학습 Reinforcement Learning - Learn from Mistakes, Dynamic current data, direct(rewards)

  원본데이터 -> 환경 상태(state) 선택 알고리즘, 보상(reward) 더 많은 보상을 얻을 수 있는 행동 -> 행동

  #### 응용분야 - 바둑, 게임, 자율주행자동차, 드론 

### 지도학습 - 분류 사례

* X-Feature 무엇(X)으로 무엇(Y)을 예측하고 싶다! Y-Label

* BI/DW 고객 DATA 건물현황, 사용상품

* 위경도 좌표 DATA 분포지역 공단지역, 주거지역, 변화가

  -> 개인 vs 개인사업자 vs 법인사업자

### 지도학습 - 회귀 사례

* X-Feature 무엇(X)으로 무엇(Y)을 예측하고 싶다! Y-Label
* 서비스별 성능 데이터
* IT/NW시스템, 날짜 장비 등 기초정보, 과거 트래픽 정보, 정상/비정상 여부
  -> 미래 시점의 트래픽 예측 정확도 88%

### 비지도학습 - 사례

* 선글라스 판매 예측
* A 마케터 20-30대 여성 선글라스 구매고객
* B 머신러닝 휴가 준비중인 여성고객, 남성과 여성 모두 포함된 열혈 스포츠 애호가
* 군집화(Clustering) 해변의상과 함께 선글라스 구입하는 여성 고객과 스포츠 의류와 함께 선글라스를 구입하는 경향이 높은 여성과 남성 군집 발견





![/GitHub/shin-sped.github.io/_site/assets/images/posts_img/readme/post-name-here 22/MachineLearningAlgorithms.png](/GitHub/shin-sped.github.io/_site/assets/images/posts_img/readme/post-name-here 22/MachineLearningAlgorithms.png)

### 딥러닝 - 뇌의 정보처리 방식을 모사한 "인공신경망"과 유사하게 여러 층(Layer)으로 깊이있게(Deep) 구성하여 학습을 진행

* ANN - 중요한(Feature)에 가중치(Weight)를 부여하여 학습, Input layer - hidden layer1, hidden layer 2 - output layer
* DNN - Deep Neural Network, 입력층, 여러 개의 은닉층, 출력층으로 구성된 가장 일반적인 모형, y = wx + b
  w(가중치), x(기울기), b(바이어스), input layer - hidden layer1, hidden layer2 - output layer
* RNN - Recurrent Neural Network 순황신경망,자신의 출력을 다시 입력으로 활용
  순서가 있는 데이터 학습에 특화(시계열 예측, 문장처리 등), ex(말, 글, 음악, 영화, 주식 시세, 시간 관련)
* GAN - Generative Adversarial Network 생성적 적대 신경망, 두 신경망 모델의 경쟁을 통해 학습
* Feature 추출을 기계가 직접, 알아서 함 - 정확도
  사람이 생각한 알고리즘 - 결과
  사람이 생각한 특징(SIFT, HOG 등) - 기계학습(SVM, KNN 등) - 결과
  신경망(딥러닝) - 결과
* 과적합(Over-fitting) - 학습데이터에만 잘 맞는 모델
* Too Slow - 복잡한 로직으로 학습시간 증가
* Black Box - 처리과정에 대한 설명이 어려움
* NLP(Natural Language Processing) - 자연어인식/처리 BERT, Ko-BERT
* Computer Vision - 영상인식/처리
* STT,(Speech to Text),  TTS(Text to Speech) -  음성인식/처리

### AI+X 

* AI는 완전히 새로운 것을 만든다기 보다는 기존 하더 일에 AI를 적용하여 자동화, 지능화를 도움
  ​

### AI 적용 프로세스

* 목적 - 고객 해지 방어 활동
* 목표1 - 사용패턴으로 해지예측
* 목표2 - 사용패턴 반영한 상품추천
* 목적과 목표에 따라 어떤 AI 모델을 만들 것인지 선택가능!
* 데이터가 편향되거나 손실되었다면 정확하지 않은 학습
* 중요한 것을 찾아서 준비 - 범주형? 수치형? 빈 값은 제거? 대체? 문자No 숫자Yes!
* 상관관계 - 의미 있는 데이터는 무엇인가?, 데이터의 분포와 관계는 어떠한가?
* 사전 준비단계 - 피쳐 엔지니어링 데이터는 범주형? 수치형?
* 결측치 처리 - 빈 값은 제거, 대체
* 데이터 인코딩 - AI는 숫자로 이해
* 선택과 반복 - 학습 유형(정답 유무), 알고리즘(이미지 학습), 개발도구(딥러닝 코드 개발!)
* 펴가와 결정 - 오차율(Loss), 정확도(Accuracy), 오차율은 낮게, 정확도는 높게

### AI 과제 정의서(sample)

* 과제명 - 선글라스 판매량 증대를 위한 고객 타겟팅 방식 개선

* 배경 및 문제 정의 - 현상/상황 : 마케터의 직관을 바탕으로 타겟 고객 선정
  핵심문제 및 원인: 마케터 역량에 따른 직관력 상이, 미처 고려하지 못한 고객군 존재

* 가설 - 선글라스를 구매하는 고객의 뚜렷한 특징이 있을 것이다.

* 기대효과 - [As-is] 경험에 의존한 마케팅 타겟 선정으로 영업효과 높지 않음
  [To-be] 선글라스 구매하는 고객의 패턴을 분석하여 명확한 타겟 선정, 영업효과 극대화

  ### 분석모델 - 활용 데이터(Input), 적용하는 AI 기능(AI솔루션/분석방법):, 적용결과(Output/Effect) 

  구매 패턴 분석 데이터 선글라스 구매고객의 Demo Data(성별, 연령, 구매시간, 주소 등)

  비지도학습 > 군집 K-Means Clustering을 통해 선글라스 구매 고객군 분류하여 마케팅 타겟군으로 활용

* ​

  ​

### AI 업무 적용 사례



	### 	회귀 예측(수치형)

### 	분류 예측(범주형)

### 	자연어 처리(Text)

### 	IT 인프라 이상징후 자동 판단

### 	고객 경험 데이터 분석을 통한 맞춤형 서비스 추천

### 	얼리어답터 단기기변 타켓








  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
