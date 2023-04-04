from sympy import*
x=symbols("x")
y=(cos(x)-1)/x
limit=limit(y,x,oo)
print("Ans is: ",limit)