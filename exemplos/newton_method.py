import exemplos
from diff.autodiff import var,df

err = 0.01

f = lambda x: x**2 - 9
x = var(1)



max_iter = 1000
for iter in range(max_iter):
    y = f(x.a)
    dy = df(f,x)
    x = var(x - y/dy)
    if abs(y) <= err:
        print("stop at iter {}: x = {} f(x) = {}".format(iter,x))
        break
    if iter == max_iter:
        print("max_iter is complete: x = {}".format(x))
