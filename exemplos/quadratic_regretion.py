import exemplos
from diff.revediff import var,const,df
xs = [i/10 for i in range(11)]
ys = [x**2 + 0.7*x + 0.1 for x in xs]

loss = lambda x,y,a,b,c : (a*x**2 + b*x + c - y)**2
err = lambda a,b,c : sum([loss(xs[i],ys[i],a,b,c) for i in range(len(xs))])

a = var(1)
b = var(0)
c = var(1)

lr = 0.01
for k in range(10000):
	tam = len(xs)
	da,db,dc = df(err,a,b,c)
	a = a - lr*da
	b = b - lr*db
	c = c - lr*dc
print(a,b,c)
