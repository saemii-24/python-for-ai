# from math import sqrt, pi
import math
from random import randint, choice
from datetime import datetime

print(math.sqrt(16))

number = randint(1, 10)
print(number)

fruit = choice(['apple', 'banana', 'cherry'])
print(fruit)

print(datetime.now())

def check_weather(temp):
    if temp > 30:
        return '30도가 넘어요'
    else: 
        return '30도 이하에요'
    
print(check_weather(25))

def greet(person1, person2):
    print(f'hello, {person1} and {person2}!')

greet('Alice', 'Bob')



discount = 0.1

def apply_discount(price):
    if price > 100:
        return price * (1 - discount)
    else:
        return price

print(apply_discount(150))

def array_func():
    arr = [1, 2, 3, 4, 5]
    one = arr[0]
    last = arr[-1]
    return one, last

first, last = array_func()
print(first, last)