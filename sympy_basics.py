import sympy as smp
from IPython.display import display
from pprint import pprint, PrettyPrinter

smp.init_printing(use_latex="mathjax", use_unicode=True)
# smp.init_session()

x = smp.symbols('x')
z = x**2 + 4*x + 3
print(smp.pretty(smp.solve(z,x)))

