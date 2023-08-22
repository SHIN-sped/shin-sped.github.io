---
title: "[NIPA]AI+웹개발 취업캠프 SW심화 4주차 5회"
excerpt: "위클리 학습일지"

categories:
  - Categories2
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories2/post-name-here-6/

toc: true
toc_sticky: true

date: 2023-08-11
last_modified_at: 2023-08-11
---

## 🦥 Python FLASK로 웹사이트 만들기 1/2

## PPTX 정리

## Install and Setup

```Python
# 1) python 3.9
# 2) powershell 관리자 모드 실행 -  Set-ExecutionPolicy RemoteSigned - Y
# 3) python -m venv mynewflaskenv
# 4) .\mynewflaskenv\Scripts\activate
# 5) pip install -r requirements.txt
# 6) python
# 7) import flask
```





## Python Level One

정수(int) 다음과 같은 정수는    3 300 200

부동 소수점(float) 소수점이 있는 숫자: 2.3 4.6 100.0

문자열(str) 순서대로 나열된 문자 시퀀스:   "hello" '새미' "2000" "楽しい"

목록(list) 정렬된 객체 시퀀스  [10,"hello",200.3]

딕셔너리(dict) 정렬되지 않은 키:값 쌍: {"mykey" : "value" , "name" : "Frankie"}

튜플(tuple) 정렬된 불변 객체 시퀀스: (10,"hello",200.3)

Set(set) 고유한 객체의 정렬되지 않은 컬렉션:  {"a","b"}

부울(bool) 참 또는 거짓을 나타내는 논리 값

```python
## Number
# Addition
2+1

# Subtraction
2-1

# Multiplication
2*2


# Division
3/2

# Powers
2**3

# Can also do roots this way
4**0.5

# Order of Operations followed in Python
2 + 10 * 10 + 3

# Can use parenthesis to specify orders
(2+10) * (10+3)

# Let's create an object called "a" and assign it the number 5
a = 5

# Now if I call a in my Python script, Python will treat it as the number 5.

# Adding the objects
a+a

# What happens on reassignment? Will Python let us write it over?

# Reassignment
a = 10

# Check
a

# Use A to redefine A
a = a + a

# Check
a

# Use object names to keep better track of what's going on in your code!
puppies = 6

weight = 2

total_weight = puppies*weight

# Show my total_weight
total_weight


## Strings
# Single word
'hello'

# Entire phrase
'This is also a string'

# We can also use double quote
"String built with double quotes"


# Be careful with quotes!
' I'm using single quotes, but will create an error'

# We can use a print statement to print a string.

print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')
len('Hello World')
# Assign s as a string
s = 'Hello World'

#Check
s

# Print the object
print(s)

# Show first element (in this case a letter)
s[0]

# Next element
s[1]

# Next Element
s[2]

# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]


# Note that there is no change to the original s
s

# Grab everything UP TO the 3rd index
s[:3]

#Everything
s[:]


# We can also use negative indexing to go backwards.
# Last letter (one index behind 0 so it loops back around)
s[-1]

# Grab everything but the last letter
s[:-1]

# Grab everything, but go in steps size of 1
s[::1]

# Grab everything, but go in step sizes of 2
s[::2]

# We can use this to print a string backwards
s[::-1]

s

# Let's try to change the first letter to 'x'
s[0] = 'x'



# Something we can do is concatenate strings!
s

# Concatenate strings!
s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

# We can use the multiplication symbol to create repetition!

letter = 'z'

letter*10

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')

print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))


# That is the basics of string formatting!
# Often we'll use the simpler form with f-string literals (MUST USE PY 3.6 FOR THIS)
username = "Jose"
color = "Blue"
print(f"The name is {username} and color is {color}")



## Lists
# Assign a list to an variable named my_list
my_list = [1,2,3]

my_list = ['A string',23,100.232,'o']
len(my_list)
# remind ourselves of how this works:
my_list = ['one','two','three',4,5]

# Grab element at index 0
my_list[0]

# Grab index 1 and everything past it
my_list[1:]

# Grab everything UP TO index 3
my_list[:3]

# We can also use + to concatenate lists, just like we did for strings.

my_list + ['new item']

# Note: This doesn't actually change the original list!

my_list


# Reassign
my_list = my_list + ['add new item permanently']

my_list

# We can also use the * for a duplication method similar to strings:

# Make the list double
my_list * 2

# Again doubling not permanent
my_list

# Create a new list
mylist = [1,2,3]


# Use the .append() method to permanently add an item to the end of a list:

# Append
mylist.append('append me!')

# Show
print(mylist)

# Pop off the 0 indexed item
mylist.pop(0)

# Show
mylist

# Assign the popped element, remember default popped index is -1
popped_item = mylist.pop()

print(popped_item)

# Show remaining list
print(mylist)


# It should also be noted that lists indexing will return an error if there is
# no element at that index. For example:
mylist[100]

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

# Show
matrix


# Grab first item in matrix object
matrix[0]

# Grab first item of the first item in the matrix object
matrix[0][0]



## Dictionaries
my_dict = {'key1':'value1','key2':'value2'}
my_dict['key2']
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
#Lets call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

#Can then even call methods on that value
my_dict['key3'][0].upper()

# We can effect the values of a key as well. For instance:
my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

#Check
my_dict['key1']

# Set the object equal to itself minus 123
my_dict['key1'] -= 123
my_dict['key1']

print(my_dict)
# We can also create keys by assignment. For instance if we started off with an
# empty dictionary, we could continually add to it:

# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

#Show
print(d)

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# Wow! Thats a quite the inception of dictionaries!
# Let's see how we can grab that value:

# Keep calling the keys
d['key1']['nestkey']['subnestkey']

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
print(d.keys())

# Method to grab all values
print(d.values())

# Method to return tuples of all items  (we'll learn about tuples soon)
print(d.items())



## Tuples_Sets Booleans
# Can create a tuple with mixed types
t = (1,2,3)

# Check len just like a list
len(t)

# Can also mix object types
t = ('one',2)

# Show
t

# Use indexing just like we did in lists
t[0]

# Slicing just like a list
t[-1]

# Use .index to enter a value and return the index
t.index('one')

# Use .count to count the number of times a value appears
t.count('one')

t[0]= 'change'

# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

t.append('nope')
x = set()

# We add to sets with the add() method
x.add(1)

#Show
x

# Add a different element
x.add(2)

#Show
x

# Try to add the same element
x.add(1)

#Show
x

# Create a list with repeats
mylist = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(mylist)

# Set object to be a boolean
a = True

#Show
a

# Output is boolean
1 > 2

# None placeholder
b = None



## Comparison-Logical_Operator
# Greater than
1 > 2
# Less than
1 < 2
# Greater than or Equal to
1 >= 1
# Less than or Equal to
1 <= 4
# Equality
1 == 1
1 == "1"
'hi' == 'bye'
# Inequality
1 != 2

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)




# If-elif-else
if 문 구문
if some_condition:
        			# 일부 코드 실행

if/else 문 구문
if some_condition:
        			# 일부 코드 실행
else:
        			# 다른 작업을 수행

if/else 문 구문
if some_condition:
        			# 일부 코드 실행
elif some_other_condition:
        			# 다른 것을 수행
else:
        			# 다른 작업을 수행

# Now let's show some examples of if, elif, and else statements:

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# If Else - Make sure to line up the else with the if statement to "connect" them

if 1 < 2:
    print('first')
else:
    print('last')

    
if 1 > 2:
    print('first')
else:
    print('last')


# To add more conditions (like else if) you just use a single phrase "elif"

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')    
    
    
## Loops
for 루프 구문
my_iterable = [1,2,3]
for item_name in my_iterable: 
        			print(item_name)
>> 1
>> 2
>> 3

#While 루프
While 루프는 특정 조건이 True로 유지되는 동안 코드 블록을 계속 실행합니다.
예를 들어, 수영장이 가득 차 있지 않은 동안 수영장에 물을 계속 채웁니다.
또는 개들이 여전히 배고픈 동안 개에게 계속 먹이를 주세요.

while 루프의 구문
while some_boolean_condition:         				#do something

원하는 경우 다른 조건과 결합할 수 있습니다.
while some_boolean_condition:         				#무언가 수행
else:
	#다른 무언가를 하세요

seq = [1,2,3,4,5]

for item in seq:
    print(item)
    
# Perform an action for every element but doesn't actually involve the elements
for item in seq:
    print('Yep')


# You can call the loop variable whatever you want:
for jelly in seq:
    print(jelly+jelly)

## For Loop with a Dictionary
ages = {"Sam":3,"Frank":4,"Dan":29}

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print("\n")
    
    
mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)
    
    

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# Note that its a generator:
range(5)

list(range(5))

for i in range(5):
    print(i)

# Start and ending
range(1,10)

# Third argument for step-size
range(0,10,2)


## Functions
def name_of_function():
	'''
     문서 문자열은 함수를 설명합니다.
     '''
        				print("Hello")

>> name_of_function()
>> Hello


def name_of_function(name):
	'''
     문서 문자열은 함수를 설명합니다.
     '''
        				print("Hello"+name)

>> name_of_function("Jose")
>> Hello Jose

일반적으로 함수의 결과를 출력하는 대신 반환 키워드를 사용하여 함수의 결과를 다시 전송합니다.
반환을 사용하면 함수의 출력을 새 변수에 할당할 수 있습니다.

def add_function(num1,num2):
        				return num1+num2

>> result = add_function(1,2)
>> 
>> print(result)
>> 3


def lowercase_function_name(argument1,argument2,argument3='default value'):
    '''
    This is the DocString of the function. It is where you can write a helpful
    description for anyone who will use your function.
    '''
    # After the docstring you write code that does stuff.

    
    
# Example 1
def report_person():
    print("Reporting Person")


# If you call the function without parenthesis it won't run, instead it will just report back what the object is:

print(report_person)


# Use parenthesis to run the function:
report_person()


# Example 2
# ** Passing in arguments/parameters **
def report(name):
    print("Reporting {}".format(name))




# Notice the error
report()
report('Bond')



# Example 3
# ** Default arguments can be used to set a default value. **



def report(name='Jason'):
    print('Reporting {}'.format(name))


report()
report('Kay')

def add(n1,n2):
    print(n1+n2)
add(2,3)
result = add(2,3)
print(result)
print(type(result))



def add(n1,n2):
    return n1+n2
add(2,3)
result = add(2,3)
print(result)



def secret_check(mystring):
    return 'secret' in mystring


# In[39]:

secret_check('This is a secret.')


# In[40]:

secret_check('SECRET')


# We can fix this with .lower()

# In[41]:

def secret_check(mystring):
    return 'secret' in mystring.lower()


# In[43]:

secret_check('SECRET!')


def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output


# Let's see what **''.join(output)** does:



''.join(['a','b','c'])




'--'.join(['a','b','c'])




'-x-'.join(['a','b','c'])




code_maker('Edward')




code_maker('John')


# OTHER USEFUL Operators
print(max(2,3))

mylist = ['a','b','c']

for x in mylist:
    print(x)

for x in enumerate(mylist):
    print(x)

for i, letter in enumerate(mylist):
    print(i)
    print(letter)

    
# Function Tasks
# Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):

    return (n1 + n2) == 10




check_ten(10,0)




check_ten(5,5)




check_ten(2,7)


# Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    if (n1+n2) == 10:
        return True
    else:
        return n1+n2




check_ten_sum(10,0)



check_ten_sum(2,7)

# Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    # Code Here
    return mystring[0].upper()


first_upper('hello')




first_upper('agent')
    
# Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.


def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]



last_two('hello')


last_two('hi')


last_two('a')
  
  
# Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.



def seq_check(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False



seq_check([1,2,3])



seq_check([7,7,7,1,2,3,7,7,7])



seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3])

# Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    return abs(len(s1)-len(s2))



compare_len('aa','aa')


compare_len('a','bb')


compare_len('bb','a')

# Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.


def sum_or_max(mylist):
    length = len(mylist)

    if length % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)



sum_or_max([1,2,3])



sum_or_max([0,1,2,3])

  
##  Exercise
# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
s[0]
# 's'
s[3]
# 'ask'
s[2:]
# 'las'
s[1:4]
# 'k'
s[-1]
#or
s[4]
# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
mylist[2][2] = "goodbye"

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
d1['simple_key']


d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']


d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1][0]


# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist)


# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {} and he is {} years old".format(age,name))
```



변수 할당방금 숫자로 작업하는 방법을 살펴봤는데, 이 숫자들은 무엇을 나타낼까요?나중에 코드에서 쉽게 참조할 수 있도록 이러한 데이터 유형에 변수 이름을 할당하면 좋을 것입니다

예를 들어 my_dogs = 2

변수 이름 규칙이름은 숫자로 시작할 수 없습니다.이름에 공백이 없어야 하며 대신 _를 사용

문자열strings문자열은 작은따옴표 또는 큰따옴표 구문을 사용하는 문자 시퀀스

이러한 작업은 [ ] 대괄호와 숫자 인덱스를 사용하여 가져오려는 항목의 위치를 나타냅니다.

문자 : h e l l o  					   인덱스 : 0 1 2 3 4

이 작업은 [ ] 대괄호와 숫자 인덱스를 사용하여 잡으려는 항목의 위치를 나타냅니다.

문자 : h e l l o  					   Index : 0 1 2 3 4           역방향 인덱스:    0 -4 -3 -2 -1



슬라이스 문자열에 변수를 '삽입'하고 싶을 때가 있습니다. 

예를 들어 my_name = "Jose"print("Hello " + my_name)



목록(list)는 인덱싱 및 슬라이싱을 지원

딕셔너리는 객체를 저장하기 위한 정렬되지 않은 매핑입니다. 앞서 목록이 정렬된 순서로 객체를 저장하는 방법을 살펴보았는데, 딕셔너리는 대신 키-값 쌍

딕셔너리는 중괄호와 콜론을 사용하여 키와 관련 값을 나타냅니다.                 {'key1':'value1','key2':'value2'}

딕셔너리:  키 이름으로 검색된 개체.순서가 지정되지 않으며 정렬할 수 없습니다.

목록(list)는  위치별로 검색된 개체입니다.정렬된 시퀀스는 색인화하거나 분할할 수 있습니다.

튜플은 리스트와 매우 유사합니다. 그러나 한 가지 중요한 차이점이 있는데, 바로 불변성입니다.요소가 튜플 안에 있으면 다시 할당할 수 없습니다.튜플은 괄호를 사용합니다: (1,2,3)

집합은 고유한 요소의 정렬되지 않은 컬렉션입니다.즉, 동일한 객체의 대표자는 하나만 있을 수 있습니다.



## Python Level Two

범위(Scope)는 변수를 보거나 액세스할 수 있는 위치를 결정하는 개념

객체 지향 프로그래밍(OOP)을 사용하면 프로그래머가 메서드와 속성을 가진 자신만의 객체, 문자열, 목록, 딕셔너리 또는 기타 객체를 정의한 후 .method_name() 구문을 사용하여 해당 객체에서 메서드를 호출



메서드는 객체 자체뿐만 아니라 객체에 대한 정보를 사용하여 결과를 반환하거나 현재 객체를 변경하는 함수 역할

예를 들어 목록에 추가하거나 튜플에서 요소의 발생 횟수를 계산하는 것



OOP를 사용하면 사용자가 직접 개체 , OOP를 사용하면 반복 가능하고 체계화된 코드



데코레이터를 사용하면 함수를 "장식"할 수 있습니다. 이 문맥에서 이 단어가 의미하는 바에 대해 논의



**if __name__ == "__main__":** - 모듈에서 임포트할 때 모듈 함수가 임포트로 사용되는지 아니면 해당 모듈의 원본 .py 파일을 사용하는지

```Python
## Modules and Packages
def func_in_mymodule():
    print("I am a function inside of the mymodule.py file!")

## Name and Main
def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    

import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")    
# file one.py
    def func():
        print("func() in one.py")

    print("top-level in one.py")

    if __name__ == "__main__":
        print("one.py is being run directly")
    else:
        print("one.py is being imported into another module")

and then:

    # file two.py
    import one

    print("top-level in two.py")
    one.func()

    if __name__ == "__main__":
        print("two.py is being run directly")
    else:
        print("two.py is being imported into another module")

Now, if you invoke the interpreter as

    python one.py

The output will be

    top-level in one.py

one.py is being run directly
If you run two.py instead:

    python two.py

You get

  top-level in one.py
  one.py is being imported into another module
  top-level in two.py
  func() in one.py
  two.py is being run directly
  
Thus, when module one gets loaded, its __name__ equals "one" instead of __main__.

## Scope
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

print(x)
print(printer())
print(x)


# x is local here:
f = lambda x:x**2



name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print(f'Because of global x is: {x}')
    x = 2
    print(f'Ran func(), changed global x to {x}')

print(f'Before calling func(), x is: {x}')
func()
print(f'Value of x (outside of func()) is: {x}')


## Object Oriented Programming
class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # 일부 작업 수행
    	print(self.param1)
        
mylist = [1,2,3]
mylist.count(2)
print(type(1))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({'key1':100}))
# Create a new object type called Sample
class Sample():
    pass

# Instance of Sample
x = Sample()

print(type(x))

class Dog():
    def __init__(self,breed):
        self.breed = breed

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')


class Dog():

    # Class Object Attribute
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','Sam')

sam.name

class Circle():

    # This is a Class Object Attribute
    # Notice how it is not under __init__
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(2)
print('Radius is: ')
print(c.getRadius())
print('Area is: ')
print(c.area())

class Animal():
    def __init__(self):
        print("Animal created")

    def report(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Dog created")

    def report(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.report()
d.eat()
d.bark()


class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        # Notice how this is return, NOT print()
        return f"Title:{self.title} , author:{self.author}, pages:{self.pages}"

    def __len__(self):
        return self.pages


book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))


## OOP_project
class Account:
    pass


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.balance




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)



# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.



class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.balance




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# Decorators
def simple_func():
   # 더 많은 일을 하고 싶어요!
#: # 간단한 작업 수행
무언가를 반환



def func():
    return 1

func()


s = 'Global Variable'

def func():
    print(locals())

print(globals())

print(globals().keys())

globals()['s']

func()

def hello(name='Jose'):
    return 'Hello '+name

hello()


greet = hello

greet
# Call it
greet()


del hello

hello()

greet()


def hello(name='Jose'):
    print 'The hello() function has been executed'

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()
# Uh oh!
welcome()


def hello(name='Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()

x
print(x())


def hello():
    return 'Hi Jose!'

def other(func):
    print 'Other code would go here'
    print func()

other(hello)


def new_decorator(func):

    def wrap_func():
        print "Code would be here, before executing the func"

        func()

        print "Code here will execute after the func()"

    return wrap_func

def func_needs_decorator():
    print "This function is in need of a Decorator"

func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()



@new_decorator
def func_needs_decorator():
    print "This function is in need of a Decorator"

func_needs_decorator()


```





## HTML and CSS Crash Course

* **HTML 기초**
* **HTML 태그 지정** - 사이트의 주요 구성 요소는 HTML 요소로 정의, HTML 요소에는 .html 파일 내에 해당 태그
* **HTML 목록** - 정보 목록을 표시하고 싶을 때, Facebook에 친구 목록 추가Google 검색 결과 나열HTML에는 <ul> 및 <ol>
* **HTML Div 및 span** - CSS와 부트스트랩 4에 대해 설명할 때 사이트의 특정 섹션에만 스타일을 적용, Div와 span을 사용하면 HTML의 일부를 분할
* **HTML 속성** - 태그에는 직접 조작할 수 있는 속성, 링크를 추가하거나 소스 이미지를 추가하는 등의 작업을 수행





## Flask Basicks

* **가상 환경** - 가상 환경을 사용하여 종속성을 관리

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def index():
      return '<h1>Hello Puppy!</h1>'

  if __name__ == '__main__':
      app.run()
  ```

  ​

* **기본 경로** - @app.route() 데코레이터에 있습니다.데코레이터에 전달된 문자열 매개변수는 함수에 연결할 URL 확장자(일명 보기)를 결정

* **동적 경로** - 상황에 따라 URL 경로 확장을 동적으로 설정, 경로 <변수>의 변수, 함수에 전달된 매개변수

* **디버그 모드**

* **요청 컨텍스트 기본 사항** - WSGI(웹 서버 게이트웨이 인터페이스)는 웹 서버가 Python 프로그래밍 언어로 작성된 웹 애플리케이션 또는 프레임워크에 요청을 전달하기 위한 간단한 호출 규칙, Flask 애플리케이션이 요청을 처리할 때, WSGI 서버로부터 받은 환경을 기반으로 요청 객체를 생성

  ​

## Templates with Flask

* 파이썬 문자열을 통해 수동으로 HTML을 반환했습니다.현실적으로 HTML 템플릿(페이지용으로 이미 생성한 HTML 파일)을 렌더링하기 위해 뷰 함수를 연결

* 플라스크에서 render_템플릿 함수를 가져와서 보기 함수에서 .html 파일을 반환하면 템플릿을 렌더링

* 렌더링_템플릿 함수를 사용하면 Flask 웹 앱으로 HTML 파일을 직접 렌더링

* Jinja 템플릿을 사용하면 Python 코드에서 HTML 파일로 변수를 직접 삽입, **{{ 일부_변수}}**

* Jinja 템플릿을 사용하면 {{ variable }} 구문을 사용하여 변수를 전달할 수 있습니다.또한 템플릿에서 루프 및 if 문과 같은 제어 흐름 구문도 사용할 수 있습니다.여기에는 {% %} 구문이 사용

* 템플릿 변수를 사용하여 HTML에 목록 변수를 전달했다고 가정해 보겠습니다.전체 목록을 한 번에 표시하는 대신 파이썬 목록의 각 항목을 글머리 기호로 구분된 HTML 목록

  ```python
   {% for item in mylist %}
   {{ item }}

   {% endfor %}

  ```

  ​

* HTML 템플릿에 직접 링크하는 뷰 함수를 만들 수 있다는 것을 알고 있습니다.하지만 여전히 모든 페이지에 대해 HTML 템플릿을 만들어야 한다는 뜻

* **템플릿 상속** - 사이트의 재사용 가능한 측면이 포함된 base.html 템플릿 파일을 설정, 그런 다음 {% extend "base.html" %} 및 {% block %} 문을 사용하여 이러한 재사용 가능한 측면을 다른 페이지로 확장

  ```python
  base.html
  {%block contents%}

  {% endblock %}

  home.html
  {%extends "base.html"%}

  {%block content%}



  {% endblock %}



  {{ variable | filter }}
  For example:
  {{ name }}
  jose
  {{ name | capitalize }}
  Jose

  ```

  ​



## Forms with Flask

* 플라스크 파이썬 스크립트에서 flask_wtf 및 wtforms 패키지를 사용하여 양식을 빠르게 만드는 방법
* 보안을 위한 비밀 키 구성, WTForm 클래스 만들기, 양식의 각 부분에 대한 필드 만들기, 보기 함수 설정, 메소드 추가 = ['GET','POST'], 폼 클래스의 인스턴스 생성, 양식 제출 처리
* 가능한 모든 HTML 양식 필드에는 가져올 수 있는 해당 wtforms 클래스가 있습니다.wtforms에는 쉽게 삽입할 수 있는 유효성 검사기도 있습니다.유효성 검사기는 필드를 채우도록 요구하는 등 양식 데이터에 대한 검사를 수행



## SQL Databases with Flask

* Flask로 양식을 통해 사용자 정보를 수집하는 방법을 이해했습니다.이러한 이해를 바탕으로 Flask 애플리케이션을 데이터베이스에 연결하여 사용자 정보를 저장
* SQL 데이터베이스로 작업할 때는 다음과 같은 SQL 문을 배워야 합니다.SELECT \* FROM Puppies
* SQLite는 Flask와 함께 제공되는 간단한 SQL 데이터베이스 엔진
* SQLite는 그 이름과는 달리 실제로 기본적인 애플리케이션(하루 10만 건의 조회 수)을 위해 꽤 잘 확장할 수 있습니다.Python, Flask, SQL을 함께 연결하려면 ORM(객체 관계형 매퍼)이 필요
* ORM을 사용하면 데이터베이스에서 생성, 편집, 업데이트 및 삭제할 때 SQL 구문 대신 Python을 직접 사용할 수 있습니다.Python에서 가장 일반적인 ORM은 SQL Alchemy
* Flask-SQLAlchemy는 Flask와 SQLAlchemy를 쉽게 연결할 수 있는 확장 프로그램
* Flask 앱에서 SQLite 데이터베이스 설정, Flask 앱에서 모델 생성, 모델에 대한 기본 CRUD 수행
* 플라스크 앱 생성, SQLAlchemy를 위한 Flask 앱 구성, 애플리케이션을 SQLAlchemy 클래스 호출에 전달
* 모델에 대한 플라스크 폼을 만드는 것과 유사 - 모델 클래스 생성, db.Model에서 상속, 선택적으로 테이블 이름 제공, 테이블 열을 속성으로 추가, .init__ 및 __repr__에 대한 메서드를 추가
* CRUD를 수행하는 기본 예제를 살펴보겠습니다.C - 생성 R - 읽기 U - 업데이트 D - 삭제
* **플라스크 마이그레이션** - Flask-SQLAlchemy를 사용하여 CRUD를 수행, 데이터베이스 테이블에 대한 모델을 만들 때 때때로 새 열을 추가하는 등 모델을 조정, 데이터베이스 테이블을 업데이트하기 위해 이러한 변경 사항을 마이그레이션
* 관계 - 대규모 프로젝트의 경우 종종 여러 개의 모델이 있을 수 있습니다.이러한 모델은 서로 관계를 가질 수 있습니다(예: 강아지용 모델과 소유자용 모델).
* 모델 관계를 이해하려면 테이블의 기본 키와 외래 키를 검토해야 합니다.기본, 키고유 식별자, 열, 외래 키,다른 테이블의 기본 키



## Large Flask Applications - 실습





## User Authentication - 실습





## Social-Network-Project - 실습





## REST APIs - 실습








  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
