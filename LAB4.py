import random
import time as t
import matplotlib.pyplot as plt
t=t.time()
random.seed(t)
d=1000
inside=0
p=[]
q=[]
r=[]
s=[]
for i in range(d):
    x=2*random.random()-1
    y=2*random.random()-1
    p.append(x)
    q.append(y)
    if x*x+y*y<=1:
        r.append(x)
        s.append(y)
        inside=inside+1
print(4*inside/d)
plt.plot(p,q,"-")
plt.plot(r,s,"-")
