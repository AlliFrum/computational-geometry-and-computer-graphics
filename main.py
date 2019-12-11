import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify
from sympy.solvers import solve
import re
def init_graph():
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

x = np.arange(-10, 10, 0.1)
y = np.cos(x)
# for i in range(len(y)):
#     y[i] = round(y[i], 2)

f = open('file_data.txt', 'w')

for i in range(len(x)):
    f.write(str(x[i]) + " " + str(y[i]) + "\n")

f.close

f = open('file_data.txt', 'r')
lines = f.readlines()
x = []
y = []

for line in lines:
    spl = re.split("\s", line)
    x.append(float(spl[0]))
    y.append(float(spl[1]))

print(x)
print(y)

init_graph()

line = plt.plot(x, y, lw=2)

plt.ylabel('f(x)=cos(x)')
plt.ylim(0, 1)
plt.yticks(np.arange(-3, 3, 1))
plt.xticks(np.arange(-11, 11, 1))

plt.savefig('figure.png')
plt.show()

f.close()
