def _p(m,n):
	return m + n
def _log(a):
	if type(a) is symbol:
		return a.index
	else:
		print(type(a))
		return 0
from functools import reduce
class poly:
	def __norm(self):
		for i in self.children:
	def __init__(self, *args):
		self.children = args
	def __repr__(self):
		ch = list(self.children)
		ch.sort(key=_log)
		return ','.join(map(lambda x: x.__repr__() , ch))
	def __mul__(self,o):
		if type(o) is symbol or type(o) is int:
			a = map(lambda x: x*o, self.children)
			return poly(*a)
		elif type(o) is poly:
			a = reduce(_p,[i*o for i in self.children])
			return a
	def __add__(self,o):
		if type(o) is symbol:
			b = None
			for i in self.children:
				if type(i) is symbol:
					if i.index == o.index:
						i.base = i.base + o.base
						b = self
				elif type(o) is poly:
					print(type(o))
			if b:
				return self
			else:
				self.children = tuple([*self.children,o])
			return self
		elif type(o) is poly:
			b = o
			for i in self.children:
				b = b + i
			return b
	def __pow__(self,o):
		if type(o) is int:
			if o > 1:
				a = self
				for i in range(o-1):
					a = a*a
			return a
class symbol:
	def copy(self):
		return symbol(self.type,self.base,self.index)
	def __init__(self,_type,base=1,index=1):
		self.type = _type
		self.base = base
		self.index = index
	def __pow__(self,o):
		if type(o) is int:
			a = self.copy()
			a.index = a.index * o
			return a
	def __mul__(self,o):
		if type(o) is symbol:
			s = symbol(self.type,o.base*self.base,o.index+self.index)
			return poly(s)
		elif type(o) is poly:
			return o*self
		elif type(o) is int:
			a = self.copy()
			a.base = a.base * o
			return a
	def __rmul__(self,o):
		return self*o
	def __add__(self,o):
		if type(o) is symbol:
			if self.index == o.index:
				return poly(symbol(self.type,self.base+o.base,self.index))
			else:
				return poly(self.copy(),o.copy())
		elif type(o) is poly:
			return o + self
	def __repr__(self):
		return f'({self.base} {self.type}^{self.index})'
x = symbol('x')
x = (x+x**2)*(x+x**2)
print(x,type(x))
