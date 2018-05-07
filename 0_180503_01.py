#author: dqw_1519100068(邓清文）
#work_7

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = -x + 0.75
    return y

# x = np.linspace(0,2,1000)
# y = f(x)
# z = x * 0
# plt.plot(x,y,"r")
# plt.plot(x,z,"b--")
# plt.show()

a,b,e = 0.1,3,0.001
k = 0
while(True):
    if f(a)*f(b)>0:
        print("Reset the line")
        break
    elif f(a)*f(b) == 0:
        if f(a) == 0:
            print(a,k)
        else:
            print(b,k)
        break
    else:
        m = (a+b)/2
        if abs(a-b)<=e:
            print(m,k)
            break
        elif f(m)*f(b)<=0:
            a=m
        else:
            b=m
        k += 1
        continue
