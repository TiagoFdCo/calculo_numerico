'''
Bibliotecas uteis em python: 
* math
* sympy
* numpy   
* mpmath
* decimal
* fractions

//cls: comando de terminal que limpa o terminal
'''

#importando as bibliotecas
import math as m
import sympy as sp
import numpy as np
import fractions as frac
import decimal as dc
#Fractions
f = frac.Fraction(1, 3)
#print(f)
#print(float(f))

'''
Exercicios
1) Compare o erro absoluto e o erro relativo da uma aproximação de pi (use 3.143, 143, 14) em relação ao valor real de pi
utilize as bibliotecas decimal, math e numpy
'''

pi1 = 3.143
pi2 = m.pi #valor de pi pela bibliteca MATH
#print(pi2)

erro_absoluto = pi1 - pi2 #MINHA FORMULA
print("erro absoluto: ", erro_absoluto)

erro_absoluto2 = abs(pi1 - pi2) #FUNÇÃO ERRO ABS DO MATH
print("erro absoluto DO MATH: ", erro_absoluto)

#erro relativo
erro_relativo = erro_absoluto/pi1
erro_relativo2 = erro_absoluto2/pi1

print(erro_relativo)
#print(erro_relativo2)

#usando decimal
dc.getcontext().prec = 10

x = dc.Decimal(erro_absoluto) / dc.Decimal(pi1)
#print(x)

#usando FRACTIONS
fracao = frac.Fraction(erro_absoluto, pi1)
print(float(fracao))