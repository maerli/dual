#teste.py
import exemplos
from diff.revediff import df,var,const,new_df
f = lambda x,y: x/(x**2 + y**2)
x = var(1)
y = const(1)

fxy,dx = new_df(f)(x,y)
print(fxy,dx)
