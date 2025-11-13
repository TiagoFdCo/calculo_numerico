import matplotlib.pyplot as plt #Biblioteca para plotar os gráficos 
import numpy as np #Biblioteca com as funções matemáticas em Python
from scipy.optimize import linprog as lp #Biblioteca que possui funções de resolução de sistemas lineares

'''
Definição do problema de maximização
T = 15x + 10y
Como o linprog minimiza, então multiplicamos por -1
'''
c = [-15, -10] #Fazendo o vetor com os coeficientes da equação a ser otimizada

#Vetor com as restrições
A = [
    [2, 1.5],
    [1.2, 0.8],
    [1, 0]
]
b = [180, 120, 40]

#Limites das variáveis (x, y > 0)
x_bounds = (0, None)
y_bounds = (0, None)

'''
Resolução do problema
'''
res = lp(c, A_ub = A, b_ub = b, bounds = [x_bounds, y_bounds], method = 'highs') #Função que resolve o sistema linear baseado nos fatores declarados acima
x_opt, y_opt = res.x #função que acha os valores ótimos de x e y
t_max = -res.fun #função que retorna o valor máximo
t_max2 = 15*x_opt + 10*y_opt #método manual para achar o valor máximo

print(f"Solução ótima: x = {x_opt:.2f}, y = {y_opt:.2f}")
print(f"valor máximo de T = {t_max:.2f}")

#Geração do gráfico
x1 = np.linspace(0, 200, 400)

#Cada restrição resolvida para y
r1 = (180 - 2 * x1) /1.5
r2 = (120 - 1.2 * x1) / 0.8
r3 = 40 - 0 * x1

#Região viável(mínimo de todas as restrições)
x2_region = np.minimum(r1, r2) #ver isso aqui
x2_region[x1 > 40] = np.nan
x2_region[x2_region < 0] = np.nan

#Plotagem

plt.figure(figsize=(8,6))
plt.plot(x1, r1, label=r'$2x + 1.5y \leq 180$ (tempo total)')
plt.plot(x1, r2, label=r'$1.2x + 0.8y \leq 120$ (memória)')
plt.plot(x1, r3, label=r'$x \leq 40$ (licenças GPU)')

# Preenche a região viável
plt.fill_between(x1, 0, x2_region, color='lightgreen', alpha=0.4, label='Região viável')

# Ponto ótimo
plt.plot(x_opt, y_opt, 'ro', label=f'Otimo (x={x_opt:.1f}, y={y_opt:.1f})')

# Curva de nível da função objetivo
T_line = ((t_max - 15*x1) / 10)
plt.plot(x1, T_line, '--', color='red', label=f'Z = {t_max:.1f}')

plt.xlim(0, 160)
plt.ylim(0, 160)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Solução Gráfica da Programação Linear\nMaximização de T = 15x + 10y')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()