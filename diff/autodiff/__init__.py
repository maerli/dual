## autodiff.py
from diff.dual import dual
def var(x):
	if type(x) is dual:
		return dual(x.a,1)
	return dual(x,1)
def const(n):
	if type(n) is dual:
		return dual(n.a,0)
	return dual(n,0)

def df(f,*args):
	y = f(*args)
	return y.b
