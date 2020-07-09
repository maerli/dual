import exemplos
from diff.revediff import var,const,df
import numpy as np
f = lambda x: 2*x + 1
xi = var(1)
x = np.array([xi,xi+1,xi+2])
dx = df(f,x)
print(f(x))
