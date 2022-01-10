import sympy  as sp 
from sympy import randMatrix
A=randMatrix(2,4,0,1)
sp.pprint(A)
sp.pprint(A.rref())