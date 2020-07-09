import exemplos
from diff.revediff import var,const,df
xs = [i/10 for i in range(11)]
ys = [2*x + 0.5 for x in xs]

loss = lambda x,y,a,b : (a*x + b - y)**2
err = lambda a,b : sum([loss(xs[i],ys[i],a,b) for i in range(len(xs))])

a = var(1)
b = var(0)
lr = 0.01
for k in range(100):
	tam = len(xs)
	da,db = df(err,a,b)
	a = a - lr*da
	b = b - lr*db
print(a,b)
