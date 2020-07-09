#newton_method_with_gradient_descent
import exemplos
from diff.autodiff import var,df

err = 0.01

f = lambda x: x**2 - 9
x = var(1)
lr = 0.01 	  # tamanho do passos

n = 1000 #numero máximo de iterações

for i in range(n):
	y = f(x.a)
	dy = df(f,x)
	x = var(x - dy*lr)
	if abs(dy) <= err:
		print("stop at it: {} x = {} : f(x) = {}".format(i+1,x,y))
		break
	if i == (n-1):
		print("não houve convergência>: it{}".format(n))


max_iter = 1000
#x = x - 1
x = x + 1
for iter in range(max_iter):
	y = f(x.a)
	dy = df(f,x)
	x = var(x - y/dy)
	if abs(y) <= err:
		print("stop at iter {}: x = {} f(x) = {}".format(iter,x,y))
		break
	if iter == max_iter:
		print("max_iter is complete: x = {}".format(x))
