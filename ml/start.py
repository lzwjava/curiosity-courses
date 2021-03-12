import numpy as np
import math
import matplotlib.pyplot as plt

x = np.random.rand(2)*100
y = np.random.rand(2)*100

a_max=1000
a_min=-1000
b_max=1000
b_min=-1000

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

for i in range(100):
    a = avg_a()
    b = avg_b()
    max_d = cal_d(a_max, b)
    min_d = cal_d(a_min, b)
    if max_d < min_d:
        a_min = a
    else:
        a_max = a
    # a = avg_a()
    # max_db = cal_db(a, b_max)
    # min_db = cal_db(a, b_min)
    # if max_db < min_db:
    #     b_min = b        
    # else:
    #     b_max = b

print(x)
print(y)
print('a = ', avg_a())
print('b = ', avg_b())
print('y[0]=', avg_a() * x[0] + avg_b())
print('y[1]=', avg_a() * x[1] + avg_b())