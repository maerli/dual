#teste.py
from autodiff import df,var
f = lambda x: x**2 + 1
x = var(3)
y = 1
dy = df(f,x)
print(dy)
