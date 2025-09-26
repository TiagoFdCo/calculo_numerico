import numpy as np

'''
MÉTODO DA BISSEÇÃO 
'''
def f(x):
    return pow(x, 3) - x - 2 #TESTE

def numero_minimo_iteracoes(a, b): #equação para o número mínimo de iterações necessárias
    n = int(np.ceil((np.log2((b - a)/10**-5)))) 
    return n

def bissecao(a, b): #método da bisseção 
    resultado = None

    for i in range(numero_minimo_iteracoes(a, b)): #faz uma repetição do processo quantas vezes forem o mínimo de iterações necessárias
        fa  = f(a) 
        fb = f(b)

        if (fa * fb < 0): #verifica se os sinais são opostos 
            c = (a + b)/2 #tira a média entre os valores do intevalo
            funcao_media = f(c) #calcula o valor da função na média c
            if funcao_media == 0:
                print(f"{c} é a raiz exata da função!")
                break
            if fa * funcao_media < 0:
                b = c
            else:
                a = c

            resultado = c

    print(resultado)
    return "processo concluído"
            #print(c) #printa cada aproximação por iteração 
#função main
bissecao(1, 2)