import math
PI = math.pi

def exp(x):
	if type(x) == dual:
		return dual(math.exp(x.a),x.b*math.exp(x.a))
	return math.exp(x)
def cos(x):
	if type(x) is dual:
		a,b = x.get()
		return dual(math.cos(a),-b*math.sin(a))
	return math.cos(a)
def sin(x):
	if type(x) is dual:
		a,b = x.get()
		return dual(math.sin(a),b*math.cos(a))
	return math.sin(x)
def log(x):
	if type(x) is dual:
		a,b = x.get()
		return dual(math.log(a),b/a)
	return math.log(x)
def log10(x):
	if type(x) is dual:
		a,b = x.get()
		return dual(math.log10(a),b/(log(10)*a))
	return math.log10(x)
def helper(a,b):
	return (a.a,a.b,b.a,b.b)
class dual:
	def __init__(self,a,b):
		"""
		cria um container para a representção de um número dual
		a + b\epsilon
		"""
		self.a = a
		self.b = b
	def __add__(self,o):
		if type(o) is dual:
			return dual(self.a+o.a,self.b+o.b)
		else:
			return dual(self.a+o,self.b)
	def __radd__(self,o):
		return self + o
	def __sub__(self,o):
		return self + (-o)
	def __rsub__(self,o):
		return -self + o
	def __truediv__(self,o):
		if type(o) is dual:
			a,b,c,d = helper(self,o)
			return dual(a/c,(b*c - a*d)/c**2)
		else:
			a = self.a
			b = self.b
			return dual(a/o,b/o)
	def __rtruediv__(self,o):
		c = self.a
		d = self.b
		return dual(o/c,-o*d/c**2)
	def __pow__(self,o):
		if type(o) is dual:
			a,b,c,d = helper(self,o)
			return dual(a**c,(a**c)*(d*math.log(a)+c*b/a))
		else:
			# c = o, d =0
			#fx = a,f'x= b, gx=c,g'x=d
			a = self.a
			b = self.b
			return dual(a**o,(a**(o - 1))*o*b)
	def __rpow__(self,o):
		return dual(o,0)**self
	def __exp__(self):
		return 1
	def __neg__(self):
		return self*(-1)
	def __pos__(self):
		return self
	def __mul__(self,o):
		if type(o) is dual:
			a,b,c,d = helper(self,o)
			return dual(a*c,a*d+b*c)
		else:
			a1 = self.a
			b1 = self.b
			return dual(a1*o,b1*o)
	def __rmul__(self,o):
		return self*o
	def __matmul__(self,o):
		a,b,c,d = helper(self,o)
		return dual(a*c,b*d)
	def __repr__(self):
		return "dual(%s,%s)"%(self.a,self.b)
	def get(self):
		return (self.a,self.b)
	def const(self):
		self.b = 0
	def var(self):
		self.b = 1
