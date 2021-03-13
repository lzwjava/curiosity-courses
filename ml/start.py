import numpy as np
import math
import matplotlib.pyplot as plt

x = np.random.rand(2)*100
y = np.random.rand(2)*100

a_max=100
a_min=-100
b_max=100
b_min=-100

def cal_d(da, b):
    y0 = x[0] * da + b
    y1 = x[1] * da + b
    d = abs(y0-y[0]) + abs(y1-y[1])
    return d

def cal_db(a, db):
    y0 = x[0] * a + db
    y1 = x[1] * a + db
    d = abs(y0-y[0]) + abs(y1-y[1])
    return d

def avg_a():
    return (a_max + a_min) / 2

def avg_b():
    return (b_max + b_min) / 2

min_dist = 1000000
min_a = 0
min_b = 0

for i in range(10000):
    a = np.random.randint((a_max - a_min)*10)/10 + a_min
    b = np.random.randint((b_max - b_min)*10)/10 + b_min
    y0 = a * x[0] + b
    y1 = a * x[1] + b
    dist = abs(y0 - y[0]) + abs(y1- y[1])
    if (dist < min_dist):
        min_a = a
        min_b = b
        min_dist = dist

print(x)
print(y)
print('a = ', min_a)
print('b = ', min_b)
print('y[0]=', min_a * x[0] + min_b)
print('y[1]=', min_a * x[1] + min_b)