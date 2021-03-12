import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.random import randint

x = randint(100)
y = randint(100)

a_max=100
a_min=0

def cal_d(da):
    y0 = x * da
    return abs(y0-y)

def avg_a():
    return (a_max + a_min) / 2

for i in range(14):
    a = avg_a()
    max_d = cal_d(a_max)
    min_d = cal_d(a_min)
    if max_d < min_d:
        a_min = a
    else:
        a_max = a    

print(x)
print(y)
print(avg_a())
print(avg_a()*x)
