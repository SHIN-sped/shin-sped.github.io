---
title: "[NIPA]AI+웹개발 취업캠프 SW기초 3주차 5회"
excerpt: "위클리 학습일지"

categories:
  - Categories1
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories1/post-name-here-12/

toc: true
toc_sticky: true

date: 2023-08-04
last_modified_at: 2023-08-04
---

## 😀 코딩 초보자를 위한 파이썬(Python) 입문(Beginner)






#### 귀도 반 로섬 - 파이썬 언어 개발자

#### 장점 - 

1. #### 단순성, 효율성 및 이해하기 쉬운 구문

2. #### 가독성은 협업 및 유지 관리를 향상시켜 팀이 프로젝트에서 원활하게 작업

3. #### Django 및 Flask와 같은 널리 사용되는 프레임워크를 통한 확장성 덕분에 개발자는 강력한 웹 애플리케이션을 손쉽게 구축

4. #### Pandas 및 NumPy와 같은 풍부한 라이브러리가 데이터의 심층 탐색 및 시각화를 용이하게 하는 데이터 분석

5. #### C/C++와의 원활한 상호 작용을 통해 개발자는 저수준 언어의 속도를 활용하면서 Python의 고급 추상화 기능을 활용

6. #### 사물 인터넷(IoT) 영역에서 Python의 가볍고 구현하기 쉬운 특성은 스마트 장치 및 센서 응용 프로그램을 개발

7. #### 웹 크롤링 및 스크래핑에 대한 적응력을 통해 개발자는 웹사이트에서 귀중한 데이터를 효율적으로 추출

8. #### TensorFlow 및 PyTorch와 같은 라이브러리가 기계 학습 및 딥 러닝 모델의 발전을 주도

9. #### 반복적인 작업과 워크플로를 자동화하고 작업 프로세스를 합리화하며 전반적인 효율성

10. #### 자동화 도구 및 스크립팅에서 일상적인 작업을 단순화

```python
python3 --version
Python 3.8.6 #안전성
```

## 자료형(data type)

```python

# 문자형 자료형 나타내기
print ("Hello python")
print ("안녕 파이썬")
print ("안녕"*7)

# 익스케이프 문자
print ("안녕하세요.")
print ('저는 홍길동입니다.')
print ('안녕하세요. \n저는 홍길동입니다.')
print ('김밥 : 3000원 \t 방문포장 : 2000원')
print ('여자들은 떡볶이를 좋아해.\r남자분들은')

# 숫자형 자료형
# 정수형
print(7)
print(-7)

# 실수형
print(3.14)
print(-3.14)

# 숫자를 표현하는 여러가지 방법
print(10000000)
print(3+4)
print(-3+-4)

# boolean 자료형
# 참/ 거짓을 나타내는 자료형

print ( 3 > 4 ) # 거짓 false
print ( 3 < 4) # 참 True
print (not(3>4)) # 거짓 --> 부정 --> 참


# 데이터 타입 알아보기
name = "에피노"
gender = "여자"
age = 15
num = 17.1
is_highschool = age>=17
print(type(name))
print(type(age))
print(type(is_highschool))
print(type(num))

```



## 변수(Variable) - 공간을 주고, 그 공간 안에 값을 집어 넣어주는 것을 의미

```python
name = '홍길동'
print (name)
name1, name2 = '파이썬', '학생'
print (name1, name2)
name1 = name2 = "자바"
print (name1, name2)

print ("철수는 남자아이이고, 17살 입니다.")
name = "철수"
gender = "남자"
age = 17
is_highschool= age>=17

print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다.")
print (name, "는", gender, "아이이고", str(age), "살입니다.")
print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다."+"\n"+ name + "는 고등학생입니까?" + str(is_highschool))
print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다."+"\n"+ name + "는 고등학생입니까?" + str(is_highschool))
```

## 연산(Operator)

```python
# 연산자

print ( 1 + 1) # 2
print ( 2 - 1 ) # 1
print ( 5 * 3) # 15
print (int( 4 / 2)) # 2

print ( 2**2 ) # 2^2 = 4
print ( 3**4 ) # 3^4 = 81
print ( 7%5 ) # 나머지 : 2
print ( 5//2 ) # 몫 : 2
print ( 5%2 ) # 나머지 : 1 

print ( 1 > 3 ) # False 
print ( 1 <= 6) # True
print ( 7==7 ) # True
print ( 7!=7) # False

# 논리 연산
print (1>2) and (2>3) # False --> and는 두 연산자가 모두 True인 경우에만 True 보여줌
print (1<2) and (2<3)
print (1>2 & 2>3) # 두 연산자 간의 and 연산 진행
print (1<2) or (2<3) # True --> or 연산은 두 연산자가 모두 false 경우에만 false 값을 보여줌
print (1<2) or (2>3) 
print (1<2 | 2>3) # 두 연산자 간의 or 연산 진행

# 맴버 연산
print ( 1 in (1,2,3,4)) # True ==> 왼쪽의 값이 오른쪽의 피연산자의 맴버에 값에 있을 경우 True
print ( 1 not in (2,3,4,5)) # True ==> " 없을 경우 True

# 간단한 연산
print ( 3 + 4 + 5 ) 
print ( 3+ 4 * 5)
print ( (3+4) * 5 )
number = (3+4)*5
print (number)
number = number + 1
print (number) # 36
number = number + 1
print (number) # 37
number += 1
print (number)#38
number *= 2
print (number)

# 최소/최대/절대/반올림
print (min(7,9)) # 7
print (max(7,9)) # 9
print (abs(-7)) # 7
print (round(3.14)) # 3
print (round(3.91)) # 4

# 랜덤한 값 구하기
from random import *

print (random()) # 0.0부터 1.0미만의 실수가 나오게됩니다.
#정수로 바꾸는 방법
print (int(random()*10))
# 1~10까지의 랜덤한 숫자를 구하고 싶다!
print (int(random()*10)+1) # 1부터 10까지의 랜덤한 숫자를 나타냅니다.
print (randint(1,10)) # 1부터 10이하의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
```



## 문자열

```python
# 문자열 표현하기
sentence = "hello my name is python"
print(sentence)
sentence = "python is useful"
print(sentence)
sentence = 'python\'s favorite language is java'
print(sentence)
sentence='''hello my name is python
python is useful
python's favorite language is java'''
print(sentence)

# 인덱싱
word = "Python"
print(word[0])
print(word[3])
print(word[-1])
word = "2021-python"
print(word[0:2])
print(word[:4])
print(word[4:])
#print(word[이상:미만:간격])
word = "1234567"
print(word[::2])
print(word[1:6:3]) #2,5

# 포맷
a = "파이썬님의 무게는 70.5kg입니다."
name = "파이썬"
weight = 70.544
print( name + "님의 무게는  "+ str(weight) +"kg입니다.")
print("%s님의 무게는 %0.1fkg입니다"%(name, weight))
# %d = 정수 %s = 문자 %f = 실수형을 의미합니다. 
print("%s님의 무게는 %skg입니다."% (name,weight))
print("{}님의 무게는 {:0.1f}kg 입니다.".format(name, weight))
print("{name}님의 무게는 {weight}kg 입니다.".format(name="자바", weight=60.8))

# 문자열 관련 함수
# find, index, count, upper, lower, strip, replace, split, len
word = 'apple'
```



## 리스트, 튜플

```python
# 리스트
print(list1)
print(list1[0])
print(list1[1] + list1[3])

# 리스트 슬라이싱
print(list1[0:1])
print(list1[0:4:2])

# 리스트 다중 리스트
list1 = [1,2,3,4,5,[1,2,3,4,5,[1,2,3,4,5]]]
print(list1[5][0])
print(list1[5][5][0])

# 리스트 연산과 함수
print(len(list1))
# print(list1 + list1)
# print(list1 * 2)
print( 1 in list1)
print( 7 not in list1)
print(min(list1))
print(max(list1))

# 함수
list1 = [1,2,3,4,5]


list1.append(6)
print(list1)
list1.insert(2, 7)
print(list1)
list1.extend([6,7,8,9,0])
list1 += [6,7,8,9,0]
list1.pop(0)
print(list1)
print(list1.pop(0))
print(list1)
list1.remove(4)
list1.clear()
print(list1.count(3))
list1.extend([1,2,3,4,5])
list1.reverse()
print(list1)
list1.sort()
print(list1)

# 튜플
# 인덱싱, 슬라이싱, 더하기 ,곱하기
tuple1 = 1,2,3,4
tuple2 = ('a', 'b', 'c', 'd')

# 튜플 더하고 곱하기
new_tuple = tuple1 + tuple2
print(new_tuple)
# new_tuple = (1, 2, 3, 4, 'a', 'b', 'c', 'd')
print(tuple2*3)
print(len(new_tuple))
print(new_tuple[0])
print(new_tuple[:3])

# 집합 자료형
set이라는 것을 사용합니다.
set 동일한 값은 하나로 취급합니다. (중복된값)
set1 = set("hello hellen")
print(set1)
list1 = list(set1)
print(list1)
리스트로 변환을 해서 인덱싱이나 슬라이싱을 할 수 있죠.

# 교집합 / 합집합 / 차집합
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])

# 합집합을 구하는 공식
print(set1 | set2)
print(set1.union(set2))

# 차집합을 구하는 공식
print( set1 - set2)
print( set1.difference(set2))

# 교집합을 구하는 공식
print( set1 & set2)
print( set1.intersection(set2))

# 집합 자료형의 함수
set1.add(5)
print(set1)
set2.update([1,2])
print(set2)
set1.remove(5)
print(set1)


```



## 딕셔너리

```python
# json 형식
api = {
    name:"에피노"
    성별 : "남자"
    전화번호 : "010-1111-1111"
    회원가입 일자 : "2021-12-01"
}

# 함수
dic = {'a' : 1, 'b' : 2 , 'c': 3 }
print(dic)
print(dic['a'])

dic = {'a' : [1,2], 'b' : 2 ,'b' : 3}
print(dic)
print(dic['b'])


# update
dic.update({'f' : 5})
print(dic)

# del (삭제)
del dic['f']
print(dic)

# fromkeys
list1 = ['a','b','c','d']
tuple1 = 1,2,3,4
dic1 = {}.fromkeys(list1)
dic2 = {}.fromkeys(list1, 1)
dic3 = {}.fromkeys(tuple1)
dic4 = {}.fromkeys(tuple1, 1)

print(dic1)
print(dic2)
print(dic3)
print(dic4)

# keys / values / items / get
dic = {'a' : 1, 'b' : 2 , 'c':3 , 'd' : 4}
print(dic.keys())
print(dic.values())s
print(dic.items()) # 키와 값을 튜플형식으로 반환을 합니다.
print(dic.get('a'))
print(dic.get('f'))
print(dic.get('f', "값이 존재하지 않습니다."))

# pop/popitem
print(dic.pop('a'))
print(dic)
print(dic.popitem()) # 맨마지막 키 밸류만 튜플로 보여주고 삭제
print(dic)

# 반복문을 통한 응용
for k in dic.keys():
    print("키 : " + k)
for v in dic.values() :
    print("값 : " + str(v))
for k,v in dic.items():
    print("키 : "+k )
    print("값 : " + str(v))
```

## 조건문, 반복문(if_for_while)

```python
# if문
day = "금요일"
if day == "공휴일" :
    print("출근 안해")
elif day == "금요일" :
    print("오전에만 일합시다.")
else :
    print("출근하는 날")

# if 기본 유형
# if 조건문 :
#     if 조건문 :
#         실행명령문
#         if 조건문 :
#             실행명령문
#     elif :
#     else :
# elif 조건문 :
#     실행명령문
# else :
#     실행명령문

# for 기본형식
# for 변수 in 리스트, 튜플, 문자열 :
#     실행 명령문
for i in [1,2,3,4] :
    print(i)
room = [101, 102, 103, 104, 105, 201, 202, 203, 204, 205]

for i in room :
    print("{}호가 배정 되었습니다.".format(i))

for range
for room in range(100,111) :
    print("%d호가 배정되었습니다."%room)
print("\n")
for room in range(100,111,2) :
    print("%d호가 배정되었습니다."%room)

# for if
score = [90, 60, 70, 30, 40, 100]
num = 0
for sco in score :
    num += 1
    if sco == 100 :
        print("{}번 시험자는 100점으로 합격하였습니다. 장학생 대상자입니다.".format(num))
    elif sco >= 60 :
        print("{}번 시험자는 합격입니다. 축하드립니다.".format(num))
    else :
        print("{}번 시험자는 불합격입니다.".format(num))

# 이중 포문
for i in range(1,5) :
    for j in range(1,5) :
        print(" i : {}, j : {}".format(i,j))

# 구구단
for i in range(2,10) :
    print("-----{}단 시작!-----".format(i))
    for j in range(1,10) :
        print("{} X {} = {}".format(i, j, i*j))

# while문 기본 형식
# while 조건문 :
#     수행할 문장
#     수행할 문장
#     수행할 문장
#     수행할 문장
#     수행할 문장

# while문의 continue와 break사용하기
num = 0
leave = [6, 17, 20, 30]
while num < 30 :
    num += 1
    if num in leave :
        continue
    elif num == 18 :
        print("죄송합니다. 재료가 모두 소진되었습니다.")
        break
    print("{}번 손님 입장해주세요!".format(num))


```



## Input

```Python
#input
a = int(input("정수 입력 : "))
print("a의 값 : {}".format(a))
print(type(a))

#리스트를 만들어보기
input_list = []

for i in range(1,6) :
    i += 1
    val = input("정수 입력 : ")
    input_list.append(val)

print(input_list)

# input과 while문 사용해보기

password = "0322"

while True :
    print("택배를 찾아가시려면 비밀번호를 입력해주세요.")
    input_pass = input("비밀번호 입력 : ")
    if input_pass == password :
        print("보관함의 문이 열렸습니다. 택배를 가져가주세요.")
        break
    elif input_pass != password :
        print("비밀번호가 틀렸습니다. 다시 입력해주세요.")

# 다양한 입출력
print("에피노", "자바", "파이썬", sep="vs")
print("뭘할래?" + "축구", "야구", "농구", sep = "vs", end="?")

# 오른쪽 정렬(rjust) 왼쪽 정렬(ljust)
menu = {"김밥" : 3000, "순대" : 2000, "라면" :4500 }
for menu1, pey in menu.items():
    # print(menu1,pey)
    print(menu1.ljust(5), str(pey).rjust(10), sep=":")

# zfill 
num = 0
while num <= 10 :
    print("대기번호 : "+ str(num).zfill(5))
    num += 1

# 3자리마다 콤마 1,000원
print("내월급 : {0:,}원".format(2000000))
print("내자산 : {0:+,}원".format(2000000))

# 정렬
print("{0: >5}".format(10))
print("{0: <5}".format(10))
print("{0: >+5}".format(10))
print("{0: >+5}".format(-10))

# 빈칸채우기
print("{0:*>10}".format(10))
print("{0:*<10}".format(10))


```



## 함수

```Python

# 함수
def sum (a,b) :
    result = a+b
    return result

print(sum (1,2))

# 결과값이 없을 수도 있다.

def bank_open(name) :
    print("%s님의 계좌가 개설되었습니다."%name)

bank_open("에피노")

# 입력값이 없는 함수
def hello_bank() :
    print("안녕하세요. 에피노뱅크입니다.")

hello_bank()

# 초기값도 미리 설정할 수 있습니다. 
def bank_open(name, bank_num, open=True):
    if open == True :
        print("%s님의 계좌가 개설되었습니다."%name)
        print("%s님의 계좌번호는 %s입니다."%(name, bank_num))
    else :
        print("%s님의 계좌 개설이 거부되었습니다."%name)

bank_open("에피노", "010-1111-1111")

# lambda 함수
def add(a,b):
    return a+b

print(add(1,2))

add = lambda a,b : a+b # 함수와 똑같은 역할을 한다
print(add(1,2))

list1 = [lambda a,b :a+b, lambda a,b : a/b] #리스트에 추가가 가능하다. def같은 함수는 리스트에 추가가 불가능
print(list1[1](2,1))
```



## 예제문제

```python
# datatype

# 예제

# 변수명 : station / bus_num / min

# 예제 1번
# 다음 문장을 위 변수명을 사용하여 완성해 보세요.
# 서울역행 207버스가 7분 후 도착합니다.
# 인천공항행 405번 버스가 3분 후 도착합니다.
station = '서울역'
bus_num = 207
min = 7
print(station + "행 " + str(bus_num) + "버스가 " + str(min) + "분 후 도착합니다.")
station = '인천공항'
bus_num = 405
min = 3
print(station + "행 " + str(bus_num) + "버스가 " + str(min) + "분 후 도착합니다.")

# 예제 2번
# 질문에 대한 답을 True/False로 나타내보세요.
# 질문 : 인천공행행 버스는 잠시 후에 도착하나요? (도착시간이 5분보다 적으면 잠시후 도착이라고 함.)
soon_arrive = min <= 5
print(station+"행 버스는 잠시 후 도착합니까?" + str(soon_arrive))

# 예제 3번
# 위에서 나타낸 변수의 값과 변수의 데이터 타입을 나타내시오. (사용하는 변수는 마지막 변수와 값을 사용)
print("station 값 : " + station + "\n" + "station 타입 : " + str(type(station)))
print("bus_num 값 : " + str(bus_num) + "\n" + "bus_num 타입 : " + str(type(bus_num)))
print("min 값 : " + str(min) + "\n" + "min 타입 : " + str(type(min)))
print("soon_arrive 값 : " + str(soon_arrive) + "\n" + "soon_arrive 타입 : " + str(type(soon_arrive)))


# Operator

# 예제
# 성인이 되어서 취직한 친구들과 1년중 두번은 정기적으로 만나기로 했습니다.

# 조건 1 랜덤으로 뽑아야합니다.
# 조건 2 하반기(7 ~ 12)와 상반기(1 ~ 6)에 한번씩 만나야합니다.

# 출력문 : 정기모임은 상반기 X월 하반기 X월에 진행합니다.

# 조건 1
from random import *

# 조건 2
day1 = randrange(1,7)
day2 = randrange(7,13)

# 출력문
print ("정기 모임은 상반기" + str(day1) + "월 하반기 " + str(day2) + "월에 진행합니다." )

print("hello python student")

def auto_oper (a,b) :
    print("더하기를 실행합니다.")
    print("{} + {} = {}".format(a, b, a+b))
    print("빼기를 진행합니다.")
    print("{} - {} = {}".format(a, b, a-b))
    print("나누기를 진행합니다.")
    print("{} / {} = {}".format(a, b, a/b))
    print("곱하기를 진행합니다.")
    print("{} X {} = {}".format(a, b, a*b))

a = int(input("정수 입력 : "))
b = int(input("정수 입력 : "))

 

auto_oper(a,b)

def input_stu ():
    stu_list=[]
    print("프로그램을 시작합니다.")
    while True :
        print("1. 학생 추가\n2. 학생 삭제\n3. 프로그램 종료")
        input_num = int(input("실행할 프로그램을 선택해주세요(정수입력) : "))
        if input_num == 1 :
            input_name = input("학생의 이름을 입력해주세요 : ")
            stu_list.append(input_name)
            print("등록완료 되었습니다.")
        elif input_num == 2 :
            input_del = input("삭제할 학생의 이름을 입력해주세요. : ")
            if input_del in stu_list :
                stu_list.remove(input_del)
                print("삭제 완료되었습니다.")
            else :
                print("등록된 학생이 아닙니다.")
        elif input_num == 3 :
            print("학생 등록 프로그램을 종료합니다.")
            print("등록된 학생 : {}".format(stu_list))
            break
        else :
            print("잘못입력하셨습니다. 다시 입력하여 주십시오.")
            continue


# slicing

# 예제
# 에피노 레일에서 새로운 기차를 발명해서 이름을 지으려고합니다.
# 다음 조건에 맞춰 이름을 지어주세요.

# 조건 1 : EFFINO에서 앞에 3글자를 사용
# 슬라이싱 , index
# 조건 2 : EFFINO에서 F의 갯수 사용
# count
# 조건 3 : EFFINO의 총 글자 갯수를 사용
# len
# 조건 4 : 만들어진 글자에서 BUS를 붙힌 후에 BUS를 TRAIN으로 변경해주세요.
# replace
# 조건 5 : 만들어진 이름에서 TRAIN만 소문자로 변경해주세요.
# lower replace

# 출력문은 포맷을 사용해서 출력해주세요.
# "EFFINO레일의 새로운 기차 이름은 EFF26train입니다." 

# 조건1 
name = "EFFINO"
new_Name = name[:name.index('I')]
print(new_Name)

# 조건2
new_Name = new_Name + str(name.count("F"))
print(new_Name)

# 조건3
new_Name = new_Name + str(len(name))
print(new_Name)

# 조건4
new_Name = new_Name + "BUS"
print(new_Name)
new_Name = new_Name.replace("BUS", "TRAIN")
print(new_Name)

# 조건 5
new_Name = new_Name.replace("TRAIN", new_Name[5:].lower())
print(new_Name)

# 출력문
print("{}레일의 새로운 기차 이름은 {}입니다".format(name, new_Name))


# if for while
#예제

num_list = [1,5,3,19,7,0,40,15,41] 

# 1조건 리스트에 20,37,23을 추가하세요.
# 2조건 리스트를 정렬하세요.
# 3조건 리스트에서 홀수와 짝수를 서로 다른 리스트에 포함시키세요.
# 출력문 
# 리스트에서 홀수는 []입니다.
# 리스트에서 짝수는 []입니다.

# 1조건
num_list.extend([20,37,23])
print(num_list)
# num_list.append(20)
# num_list.append(37)
# num_list.append(23)
# num_list += [20,37,23]

# 조건2
num_list.sort()
print(num_list)

# 조건 3
i = 0
even_num = []
odd_num = []

while i < len(num_list):
    if num_list[i] % 2 == 1 :
        odd_num.append(num_list[i])
        i+=1
    elif num_list[i] == 0 :
        print("홀수도 짝수도 아닌 0입니다.")
        i+=1
    elif num_list[i] % 2 == 0 :
        even_num.append(num_list[i])
        i+=1 

# 출력문
print("리스트에서 홀수는" + str(odd_num) + "입니다.")
print("리스트에서 짝수는" + str(even_num) + "입니다.")


# 예제 2
# 다음과 같이 별을 찍으세요.

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********

for i in range(1,9):
    print("*"*(i))

    
# def

# 예제1
# 두개의 숫자를 입력받아 더하기,빼기,나누기,곱하기
# 를 출력하는 프로그램을 제작하세요.
# 첫 입력 : a
# 두번째 입력 : b 

# def num_oper (a,b) :
#     print("더하기를 진행합니다.")
#     print("{} + {} = {}".format(a, b, a+b))
#     print("빼기를 진행합니다.")
#     print("{} - {} = {}".format(a, b, a-b))
#     print("나누기를 진행합니다.")
#     print("{} / {} = {}".format(a, b, a/b))
#     print("곱하기를 진행합니다.")
#     print("{} * {} = {}".format(a, b, a*b))

# a = int(input("정수 입력 : "))
# b = int(input("정수 입력 : "))

# num_oper(a, b)


# 예제 2
# 학교의 학생의 이름을 추가하고 삭제하는 프로그램을 제작하세요.
# 조건 1 학생의 이름은 프로그램 종료 전까지 계속 추가할 수 잇어야한다.
# 조건 2 프로그램 종료 시 맨마지막에 추가한 모든 학생의 이름을 출력한다.
# 조건 3 다른 숫자를 입력하면 잘못입력하였다고 알려주고 다시 입력 받는다.
# 조건 4 삭제하려는 학생이 이름이 없을 시에는 등록되지 않았다고 알려주고 다시 처음부터
#        프로그램을 시작한다.
# 조건 5 프로그램 시작과 종료를 알려준다.

def stu_upd () :
    stu_list=[]
    print("학생 등록 프로그램을 시작합니다.")
    while True :
        print("1. 학생 등록\n2. 학생 삭제\n3. 종료")
        input_num = int(input("프로그램할 번호 입력 : "))
        if input_num == 1 :
            print("학생을 등록하겠습니다.")
            input_name = input("학생의 이름을 입력해주세요. : ")
            stu_list.append(input_name)
            print("등록이 완료되었습니다.")
        elif input_num == 2 :
            print("학생을 삭제하겠습니다.")
            input_name = input("학생의 이름을 입력해주세요. : ")
            if input_name in stu_list :
                print("학생 삭제를 완료 하였습니다.")
                stu_list.remove(input_name)
            else :
                print("잘못입력 하였습니다.")
        elif input_num == 3 :
            print("학생 등록 프로그램을 종료 하겠습니다.")
            print("등록된 학생 : {}".format(stu_list))
            break
        else :
            print("잘못입력하셨습니다. 다시 입력해주세요.")

stu_upd()


```



## 후기

위클리를 하면서 파이썬을 코딩테스트를 풀이하면서 공부를 해왔지만, 하나의 섹션을 코드로 표현해서 코딩테스트를 코드 리뷰하면서 어렵게 느꼈던 주석들이 이해 되는 강의였다. 인공지능 관련된 중요한 섹션으로는 데이터 관련으로 숫자, 문자, 부울 및 문자열, 데이터 유형이 있고, AI 알고리즘 데이터 구성과 저장 관련은 튜플 및 딕셔너리, AI 모델 교육 및 평가 관련은 변수가 있다고 생각한다. 이번 유데미 강의 위클리 역량 강화를 통해서 파이썬 언어에 대한 다른 측면에서 접근을 생각해 볼 수 있어서 좋았다.






  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
