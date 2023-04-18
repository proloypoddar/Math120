# # from sympy import*
# # x=symbols("x")
# # y=Function("y")
# # yp=diff(y(x),x)
# # enq=yp+(y(x)**2/x**2)
# # sol=dsolve(enq,y(x),ics={y(1):1/2})
# # pprint(sol)
# # ######################
# from sympy import*
# t=symbols("t")
# y=Function("y")
# a=symbols("a")
# ytp=diff(y(t),t)
# eq=ytp-(2*a*t-2*y(t)*t)
# pprint(dsolve(eq,ics={y(0):"0"}))
