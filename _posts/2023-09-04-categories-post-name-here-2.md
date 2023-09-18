---
title: "[NIPA]AI+웹개발 취업캠프 SW심화 8주차 1회"
excerpt: "데일리 학습일지"

categories:
  - Categories2
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories2/post-name-here-22/

toc: true
toc_sticky: true

date: 2023-09-04
last_modified_at: 2023-09-04
---

## 🦥 본문

```python
from keras.models import Model, Sequential
from keras.layers import Dense, Input
from keras.layers import LeakyReLU
#from keras.layers import relu
#from keras.layers import softnmax
#from keras.layers import Tahn
#from keras.layers import sign
from tensorflow.keras.optimizers import Adam
from keras.datasets import mnist
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = (x_test.astype(np.float32) - 127.5)/127.5
mnist_data=x_test.reshape(10000, 784)
print(mnist_data.shape)
len(mnist_data)


def create_generator():
    generator = Sequential()
    generator.add(Dense(units=256,input_dim=100))
    generator.add(LeakyReLU(0.2))
    #generator.add(ReLU(0.2))
    generator.add(Dense(units=512))
    generator.add(LeakyReLU(0.2))
    #generator.add(ReLU(0.2))
    generator.add(Dense(units=784, activation='tanh'))
    return generator
g = create_generator()
g.summary()


def create_discriminator():
    discriminator = Sequential()
    discriminator.add(Dense(units=512,input_dim=784))
    discriminator.add(LeakyReLU(0.2))
    #discriminator.add(relu(0.2))
    discriminator.add(Dense(units=256))
    discriminator.add(LeakyReLU(0.2))
    #discriminator.add(relu(0.2))
    discriminator.add(Dense(units=1, activation='sigmoid'))
    discriminator.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5))
    return discriminator

d = create_discriminator()
d.summary()



def create_gan(discriminator, generator):
    discriminator.trainable = False
    gan_input = Input(shape=(100,))
    x = generator(gan_input)
    gan_output = discriminator(x)
    gan = Model(inputs=gan_input, outputs=gan_output)
    gan.compile(loss='binary_crossentropy', optimizer='adam')
    return gan

gan = create_gan(d, g)
gan.summary()


def plot_generated_images(generator):
    noise = np.random.normal(loc=0, scale=1, size=[100, 100])
    generated_images = generator.predict(noise)
    generated_images = generated_images.reshape(100,28,28)
    plt.figure(figsize=(10, 10))
    for i in range(generated_images.shape[0]):
        plt.subplot(10, 10, i+1)
        plt.imshow(generated_images[i], interpolation='nearest')
        plt.axis('off')
    plt.tight_layout()
    
    
batch_size = 128
epochs = 10000

for e in tqdm(range(epochs)):
    noise = np.random.normal(0,1, [batch_size, 100])
    generated_images=g.predict(noise)
    image_batch=mnist_data[np.random.randint(low=0,high=mnist_data.shape[0],size=batch_size)]
    X = np.concatenate([image_batch, generated_images])
    y_dis = np.zeros(2*batch_size)
    y_dis[:batch_size] = 1
    d.trainable = True
    d.train_on_batch(X, y_dis)

    noise = np.random.normal(0,1, [batch_size, 100])
    y_gen = np.ones(batch_size)
    d.trainable = False
    gan.train_on_batch(noise, y_gen)

    if e == 0 or e % 1000 == 0:
        plot_generated_images(g)
        
        
 
```



## RELU

```python
from keras.models import Model, Sequential
from keras.layers import Dense, Input, LeakyReLU, Activation, ReLU
from tensorflow.keras.optimizers import Adam
from keras.datasets import mnist
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = (x_test.astype(np.float32) - 127.5)/127.5
mnist_data=x_test.reshape(10000, 784)
print(mnist_data.shape)
len(mnist_data)

def create_generator():
    generator = Sequential()
    generator.add(Dense(units=256,input_dim=100))
    generator.add(LeakyReLU(0.2))
    generator.add(ReLU(0.2))
    generator.add(Dense(units=512))
    generator.add(LeakyReLU(0.2))
    generator.add(ReLU(0.2))
    generator.add(Dense(units=784, activation='tanh'))
    return generator
g = create_generator()
g.summary()


def create_discriminator():
    discriminator = Sequential()
    discriminator.add(Dense(units=512,input_dim=784))
    discriminator.add(LeakyReLU(0.2))
    discriminator.add(ReLU(0.2))
    discriminator.add(Dense(units=256))
    discriminator.add(LeakyReLU(0.2))
    discriminator.add(ReLU(0.2))
    discriminator.add(Dense(units=1, activation='sigmoid'))
    discriminator.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5))
    return discriminator

d = create_discriminator()
d.summary()



def create_gan(discriminator, generator):
    discriminator.trainable = False
    gan_input = Input(shape=(100,))
    x = generator(gan_input)
    gan_output = discriminator(x)
    gan = Model(inputs=gan_input, outputs=gan_output)
    gan.compile(loss='binary_crossentropy', optimizer='adam')
    return gan

gan = create_gan(d, g)
gan.summary()


def plot_generated_images(generator):
    noise = np.random.normal(loc=0, scale=1, size=[100, 100])
    generated_images = generator.predict(noise)
    generated_images = generated_images.reshape(100,28,28)
    plt.figure(figsize=(10, 10))
    for i in range(generated_images.shape[0]):
        plt.subplot(10, 10, i+1)
        plt.imshow(generated_images[i], interpolation='nearest')
        plt.axis('off')
    plt.tight_layout()
    
batch_size = 128
epochs = 10000

for e in tqdm(range(epochs)):
    noise = np.random.normal(0,1, [batch_size, 100])
    generated_images=g.predict(noise)
    image_batch=mnist_data[np.random.randint(low=0,high=mnist_data.shape[0],size=batch_size)]
    X = np.concatenate([image_batch, generated_images])
    y_dis = np.zeros(2*batch_size)
    y_dis[:batch_size] = 1
    d.trainable = True
    d.train_on_batch(X, y_dis)

    noise = np.random.normal(0,1, [batch_size, 100])
    y_gen = np.ones(batch_size)
    d.trainable = False
    gan.train_on_batch(noise, y_gen)

    if e == 0 or e % 1000 == 0:
        plot_generated_images(g)
        
        
        

```



## softmax, tanh, sign

```Python
from keras.models import Model, Sequential
from keras.layers import Dense, Input, LeakyReLU, Activation, ReLU, Softmax, Tanh, Sign
from tensorflow.keras.optimizers import Adam
from keras.datasets import mnist
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

def create_generator():
    generator = Sequential()
    generator.add(Dense(units=256, input_dim=100, activation=tanh))
    generator.add(Dense(units=512, activation=tanh))
    generator.add(Dense(units=784, activation=softmax))
    return generator

g = create_generator()
g.summary()

def create_discriminator():
    discriminator = Sequential()
    discriminator.add(Dense(units=512, input_dim=784, activation=tanh))
    discriminator.add(Dense(units=256, activation=tanh))
    discriminator.add(Dense(units=1, activation=sign))
    discriminator.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5))
    return discriminator

d = create_discriminator()
d.summary()

def create_gan(discriminator, generator):
    discriminator.trainable = False
    gan_input = Input(shape=(100,))
    x = generator(gan_input)
    gan_output = discriminator(x)
    gan = Model(inputs=gan_input, outputs=gan_output)
    gan.compile(loss='binary_crossentropy', optimizer='adam')
    return gan

gan = create_gan(d, g)
gan.summary()

def plot_generated_images(generator):
    noise = np.random.normal(loc=0, scale=1, size=[100, 100])
    generated_images = generator.predict(noise)
    generated_images = generated_images.reshape(100, 28, 28)
    plt.figure(figsize=(10, 10))
    for i in range(generated_images.shape[0]):
        plt.subplot(10, 10, i + 1)
        plt.imshow(generated_images[i], interpolation='nearest')
        plt.axis('off')
    plt.tight_layout()

batch_size = 128
epochs = 10000

for e in tqdm(range(epochs)):
    noise = np.random.normal(0, 1, [batch_size, 100])
    generated_images = g.predict(noise)
    image_batch = mnist_data[np.random.randint(low=0, high=mnist_data.shape[0], size=batch_size)]
    X = np.concatenate([image_batch, generated_images])
    y_dis = np.zeros(2 * batch_size)
    y_dis[:batch_size] = 1
    d.trainable = True
    d.train_on_batch(X, y_dis)

    noise = np.random.normal(0, 1, [batch_size, 100])
    y_gen = np.ones(batch_size)
    d.trainable = False
    gan.train_on_batch(noise, y_gen)

    if e == 0 or e % 1000 == 0:
        plot_generated_images(g)
```





내용

  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
