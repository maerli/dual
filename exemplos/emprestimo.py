import exemplos
from diff.autodiff import var,df,const

err = 0.01

f = lambda pv,i,n:  pv*(i/(1 - (1/(1 + i)**n))) - 289.62
pv = var(10)
i = const(4.20297/100)
n = const(6)

max_iter = 1000
for iter in range(max_iter):
    y = f(pv.a,i.a,n.a)
    dy = df(f,pv,i,n)
    pv = var(pv - y/dy)
    if abs(y) <= err:
        print(pv,iter)
        break
    if iter == max_iter:
        print("max_iter is complete: x = {}".format(pv))
