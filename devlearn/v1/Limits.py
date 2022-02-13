import sympy as smp
from sympy import *

# declare symbols
x = smp.symbols('x')

# build function
f = sqrt(3 - 5*x + x**2 + x**3)/(x-1)

# obtain left-hand limit
L = smp.limit(f, x, 1, dir="-")

# obtain right-hand limit
R = smp.limit(f, x, 1, dir="+")

print("Left-hand limit = {}\nRight-hand limit = {}".format(L, R))

# plot the data
p1 = plot(f, (x, 0.5, .999), show=False)
p2 = plot(f, (x, 1.5, 1.0001), show=False)
p1.append(p2[0])
p1.show()