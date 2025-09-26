'''
para o método RK4, segue-se os seguintes passos:
1)achar f(x0, y0), dada a função
2)achar k1, usando a equação dada
3)calcular k2, k3 e k4
4)aplica-se os 'ks' em y1
5)repete-se quantas vezes for necessário (seguindo o passo dado)

ENTRADAS:
-função(?)
-passo
-y(0), sendo que y(0) = x0
-y final, para poder determinar o passo

*resolva a EDO:  y' = -y + x -2, com, y(0) = 2, h= 0.1, para y(0.3) usando o método de runge kutta de 4ª ordem
'''

import sympy as sp
from sympy import *

#determinando as funções e variáveis
x, y, h = sp.symbols('x,y,h')
f = Function('f')
k2f = Function('k2f')
k3f = Function('k3f')
k4f = Function('k4f')
k1 = Function('k1')

def rk4(f, y_n, x0, yf, h):
  numeroIteracoes = int((yf - x0)/h)
  #no loop, a varivável i vai começar de zero e ir até numeroIteracoes

  for i in range(numeroIteracoes + 1):
  #primeira iteração:
    k1 = h * f.subs(x, x0).subs(y, y_n)
    k2f = h * f.subs(x, x0 + h/2).subs(y, y_n + k1/2)
    k3f = h * f.subs(x, x0 + h/2).subs(y, y_n + k2f/2)
    k4f = h * f.subs(x, x0 + h).subs(y, y_n + k3f)

    y_n += ((k1 + 2*k2f + 2*k3f + k4f)/6)

    x0 += h
  return y_n

  #Digite a função:
f = -y + x - 2
#Digite o valor de x0:
x0 = 0
#Digite o valor de y0:
y_n = 2
#Digite o passo:
h = 0.1
#Digite o valor de y final:
yf = 0.3

print(round((rk4(f, y_n, x0, yf, h)), 5))