# author: dqw_1519100068_0430（邓清文）
# 数值拟合，leastsq

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

def f(p):
    a,b,c = p
    return(Y-(a*X*X+b*X+c))

X = np.array([0., 1., 2., 3., -1.,-2.,-3.])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
x = np.linspace(-4,4,1000)
r = leastsq(f,[1,0,0])
a,b,c = r[0]
y=a*x*x+b*x+c
print("a=",a,"b=",b,"c=",c)

plt.figure(figsize=(8,8))
plt.scatter(X,Y, s=90, alpha=1.0, marker='o',label=u'数据点')
plt.plot(x, y, color='r',linewidth=5, linestyle=":",label=u'拟合曲线')

plt.xlabel(u'安培/A',fontproperties=font)
plt.ylabel(u'伏特/V',fontproperties=font)
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(-2, y.max() * 1.1)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.legend(loc='upper left',prop=font)
plt.savefig('y=ax^2+bx+c.jpeg')
plt.show()
