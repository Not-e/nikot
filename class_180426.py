import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9,9))
x = np.linspace(0,10,1000)
X = np.array([1.,2.,3.,4.,5.])
Y = np.array([4,4.5,6,8,8.5])

def f(p):
    k, b = p
    return Y - (k * X + b)

r = leastsq(f, [1,0])
k, b = r[0]
print("k=",k,"b=",b)

# plt.scatter(X,Y, s=100, alpha=1.0 , marker='o' , label=u'数据点')
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9,9))

x = np.linspace(0,10,1000)
X = np.array([1., 2., 3., 4., 5.])
Y = np.array([4, 4.5, 6, 8, 8.5])

def f(p):
    k, b = p
    return(Y-(k*X+b))

r = leastsq(f, [1,0])
k, b = r[0]
print("k=",k,"b=",b)

plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label=u'数据点')
y=k*x+b

ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')

plt.xlim(0, x.max() * 1.1)
plt.ylim(0, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()

