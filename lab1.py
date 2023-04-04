# # import numpy as np
# # a= np.arange(15).reshape(3,5)
# # print(a)
# #####################
# import numpy as np
# a=np.array([1,2,3,4])
# print(a)
# print(a[1])
# print(type(a))
# b=np.array([(1,2,3),(4,5,6)])
# print(b)
# b=np.array([(1,2,3),(4,5,6)],dtype= complex)
# print(b)
# b=np.array([(1.2,2,3),(7,9,5)])
# print(b)
##################################
"""Calculus sympy"""
from sympy import *
x=symbols('r')
a=diff(cos(x),x)
print(a)


