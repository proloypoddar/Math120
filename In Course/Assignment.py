from sympy import*
import matplotlib.pyplot as plt
import numpy as np
x, a, b = symbols('x a b')
integrand = sin(a*x) * exp(-b*x)
func = lambdify(x, integrand.subs([(a, 1), (b, 1)]), 'numpy')
x_vals = np.linspace(-10, 10, 1000)
y_vals = func(x_vals)
plt.plot(x_vals, y_vals)
plt.show()
integrand = sin(a*x) * exp(-b*x)
integral = integrate(integrand, x)
integral = simplify(integral)
pprint( integral)