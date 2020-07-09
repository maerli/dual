#reversediff
from diff.revediff.reverse import Var

def _clear_children(*args):
	for x in args:
		if type(x) is Var:
			x.children = []
			x.grad_value = None
		

def var(x):
	if type(x) is Var:
		x.children = []
		x.grad_value = None
		return Var(x.value)
	return Var(x)

def df(f,*args):
	y = f(*args)
	y.grad_value = 1.0
	ans = [x.grad() for x in args if type(x) is Var]
	_clear_children(*args)
	if len(ans) == 1: 
		return ans[0]
	return tuple(ans)
def const(x):
	if type(x) is Var:
		pass
	return x

