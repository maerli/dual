import exemplos
from math import sqrt
from diff.revediff import var,df,const,new_df
def f(x,y):
	n = (x**2 + y**2)
	d = n*(n**0.5)
	return (x/d,-y/(d))
lis = [(1, 0), (0, 1), (-1, 0), (0, -1), (2, 0), (0, 2), (-2, 0) , (0, -2)]
for x,y in lis:
	_x,_y = f(x,y)
	print(f'({x},{y}) = ({_x},{_y})')
