from dual import dual
from random import random
num = 10
xs = [x/num for x in range(num)]
ys = [(2*x + 1 ) for x in xs]

f = lambda x,a,b : a*x + b
loss = lambda a,b,x,y: (y - f(x,a,b))**2

a = dual(1,1)
b = dual(0,0)
lr = 0.01
def regretion():
	while True:
		fa,dfa = (sum([ loss(a,b,xs[i],ys[i]) for i in range(num)])/num).get()
		a.a -= lr*dfa
		a.const()
		b.var()
		
		fb,dfb = (sum([ loss(a,b,xs[i],ys[i]) for i in range(num)])/num).get()
		b.a -= lr*dfb
		a.var()
		b.const()
		
		if fa < 0.001:
			print(a,b)
			print(f(1,a,b))
			break
regretion()
