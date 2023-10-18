from sympy import *
import matplotlib 
from matplotlib import pyplot
import numpy as np
def taylor_polynomial(fx, x_not, n, x):
        if n == 0:
              x = symbols('x')
              return sympify(fx).subs({x: x_not})
        else:
            new_fx = fx

            x = symbols('x')
            for i in range(n):
                new_fx = Derivative(new_fx, x, evaluate=True)
            
            a = new_fx.subs({x: x_not})
            final_exp = ((x-x_not)**n)*a/factorial(n)
            return final_exp + taylor_polynomial(fx, x_not, n-1, x)   
fx = input("give polynomial")
n = int(input("give order of polynomial"))
x_not = int(input("at what point would you like to approximate"))
x = 'x'
a = taylor_polynomial(fx, x_not , n, x)
#print(a)
ord1 = taylor_polynomial(fx, x_not , 1, x)
ord2 = taylor_polynomial(fx, x_not , 2, x)
ord3 = taylor_polynomial(fx, x_not , 3, x)
b = sympify(a).subs({x: 0})
#print(b)
j = np.linspace(0.1,5.0,num = 100)
array1 = []
array2 = []
array3 = []
array4 = []
array5 = []

for i in np.linspace(0.01,5.0,num = 100):
    array1.append(sympify(a).subs({x: i}))
    array2.append(sympify(fx).subs({x: i}))
 
    array3.append(sympify(ord1).subs({x: i}))
    array4.append(sympify(ord2).subs({x: i}))
    array5.append(sympify(ord3).subs({x: i}))
    

#pyplot.plot(j, array1, color = 'c')
pyplot.plot(j, array2, color = 'c')
pyplot.plot(j, array3, color = 'b')
pyplot.plot(j, array4, color = 'g')
pyplot.plot(j, array5, color = 'y')
pyplot.show()

