import exemplos
from diff.autodiff import var,const,df

f = lambda x: x**2 -3*x + 1

## gradiente descent para encontrar df(x) = 0

x = var(0) # chute inicial
lr = 0.01 	  # tamanho do passos
err = 0.001   # |df(x) - df(xi)|

n = 1000 #numero máximo de iterações

for i in range(n):
	dy = df(f,x) # return dy
	x = var(x - dy*lr)
	  # ajustando os passos
	if abs(dy) <= err: # verificando se
		print("stop at it: {} x = {}".format(i+1,x))
		break
	if i == (n-1):
		print("não houve convergência>: it{}".format(n))
