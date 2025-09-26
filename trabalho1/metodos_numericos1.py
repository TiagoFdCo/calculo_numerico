# Importa bibliotecas essenciais
import numpy as np              # Para cálculos numéricos e funções matemáticas
import matplotlib.pyplot as plt # Para gerar gráficos
import pandas as pd             # Para criar e manipular tabelas (DataFrames)

# ==============================
# MÉTODO DA BISSEÇÃO
# ==============================

def f(x):
    # Função alvo: f(x) = x^3 - x - 2
    # Recebe um valor x e retorna o valor da função
    return x**3 - x - 2

def numero_minimo_iteracoes(a, b, tol=1e-5):
    # Calcula o número mínimo de iterações necessárias para atingir uma tolerância desejada
    # Fórmula derivada do método da bisseção: n >= log2((b-a)/tol)
    n = int(np.ceil(np.log2((b - a)/tol)))  # np.ceil arredonda para cima
    return n  # Retorna o número mínimo de iterações

def bissecao(a, b, tol=1e-5):
    # Função que implementa o método da bisseção
    resultado = None  # Inicializa variável para armazenar a raiz aproximada
    dados = []        # Lista para armazenar as iterações e aproximações

    for i in range(numero_minimo_iteracoes(a, b, tol)): 
        # Loop para realizar o número mínimo de iterações
        fa = f(a)  # Calcula f(a)
        fb = f(b)  # Calcula f(b)

        if fa * fb < 0:  # Verifica se os sinais são opostos
            c = (a + b)/2  # Calcula ponto médio do intervalo
            fc = f(c)      # Calcula f(c)
            if fc == 0:    # Se f(c) for exatamente zero, encontramos a raiz
                resultado = c
                dados.append({"iteração": i, "aproximação": resultado})
                break
            if fa * fc < 0: # Ajusta o intervalo dependendo do sinal de f(c)
                b = c
            else:
                a = c
            resultado = c
            # Salva a iteração e a aproximação
            dados.append({"iteração": i, "aproximação": resultado})

    # Cria um DataFrame do pandas com as iterações
    df = pd.DataFrame(dados)
    # Calcula erro absoluto em relação à última aproximação da raiz
    df["erro"] = abs(df["aproximação"] - df["aproximação"].iloc[-1])

    # ----- CONFIGURAÇÃO DA FIGURA COM GRID -----
    fig = plt.figure(figsize=(18, 10))  # Tamanho da figura
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 2])  # Grade de 2x2, primeira linha menor

    # 1. Tabela como imagem
    ax_table = fig.add_subplot(gs[0, :])  # Ocupa primeira linha inteira
    ax_table.axis('tight')                 # Ajusta layout da tabela
    ax_table.axis('off')                   # Desliga os eixos
    tabela = ax_table.table(cellText=np.round(df.values, 6),  # Conteúdo da tabela
                            colLabels=df.columns,             # Cabeçalhos
                            cellLoc='center',                # Centraliza conteúdo
                            loc='center')                    # Centraliza tabela
    # Ajusta a coluna de iteração para mostrar números inteiros
    for i in range(len(df)):
        tabela[i + 1, 0].get_text().set_text(f"{int(df.iloc[i,0])}")

    # Dados da função para gráfico
    x = np.linspace(min(df["aproximação"]) - 0.5, max(df["aproximação"]) + 0.5, 200)  # 200 pontos
    y = f(x)  # Calcula f(x) para cada ponto

    # 2. Gráfico Aproximação vs Iteração
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.plot(df["iteração"], df["aproximação"], marker="o")  # Plota pontos da aproximação
    ax1.set_title("Aproximação vs Iteração")
    ax1.set_xlabel("Iteração")
    ax1.set_ylabel("Aproximação")
    ax1.grid(True)  # Adiciona grade

    # 3. Gráfico Erro vs Iteração (logarítmico)
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.semilogy(df["iteração"], df["erro"], marker="o")  # Escala log no eixo y
    ax2.set_title("Erro vs Iteração (log)")
    ax2.set_xlabel("Iteração")
    ax2.set_ylabel("Erro")
    ax2.grid(True, which="both")

    plt.tight_layout()  # Ajusta espaços
    plt.show()          # Exibe figura

    # 4. Gráfico da função e iterações
    plt.figure(figsize=(8,5))
    plt.plot(x, y, label="f(x)")  # Plota curva da função
    plt.axhline(0, color="black", linewidth=1)  # Linha y=0
    plt.scatter(df["aproximação"], [f(val) for val in df["aproximação"]],
                color="red", marker="x", label="Iterações")  # Pontos das iterações
    plt.title("Função e Iterações - Bisseção")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return df  # Retorna o DataFrame com resultados

# ==============================
# MÉTODO DA FALSA POSIÇÃO
# ==============================

MAX_ITER = 100  # Máximo de iterações

def falsaPosicao(a, b, tol=1e-5, max_iter=MAX_ITER):
    if f(a) * f(b) > 0:  # Verifica sinais opostos
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")

    dados = []  # Lista para armazenar dados
    xr_ant = None  # Valor anterior de xr para calcular erro

    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        xr = (a * fb - b * fa) / (fb - fa)  # Fórmula da falsa posição
        fxr = f(xr)
        erro = abs(xr - xr_ant) if xr_ant is not None else np.nan
        xr_ant = xr

        dados.append({"iteração": i, "aproximação": xr, "erro": erro})

        if abs(fxr) < tol:  # Critério de parada
            break

        if fa * fxr < 0:
            b = xr
        else:
            a = xr

    df = pd.DataFrame(dados)

    # Tabela como imagem
    fig, ax = plt.subplots(figsize=(12, len(df)*0.5 + 1))
    ax.axis('off')
    ax.axis('tight')
    table = ax.table(cellText=np.round(df.values,6),
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1,1.5)
    plt.title("📊 Tabela de Iterações do Método da Falsa Posição", fontsize=14)
    plt.show()

    # Gráfico Aproximação vs Iteração
    plt.figure(figsize=(10,5))
    plt.plot(df["iteração"], df["aproximação"], marker="o", color="b")
    plt.axhline(y=df["aproximação"].iloc[-1], color="r", linestyle="--",
                label=f"Raiz ≈ {df['aproximação'].iloc[-1]:.6f}")
    plt.title("Convergência do Método da Falsa Posição")
    plt.xlabel("Iteração")
    plt.ylabel("Aproximação da Raiz")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Gráfico Erro vs Iteração
    plt.figure(figsize=(10,5))
    plt.plot(df["iteração"], df["erro"], marker="o", color="orange")
    plt.yscale("log")
    plt.title("Erro Absoluto por Iteração")
    plt.xlabel("Iteração")
    plt.ylabel("Erro |xr - xr_ant|")
    plt.grid(True)
    plt.show()

    return df  # Retorna o DataFrame com resultados

# ==============================
# EXECUÇÃO E COMPARAÇÃO
# ==============================

df_bissecao = bissecao(1, 2)      # Executa bisseção no intervalo [1,2]
df_falsa = falsaPosicao(1, 2)    # Executa falsa posição no mesmo intervalo

# Gráfico comparativo das aproximações
plt.figure(figsize=(10,5))
plt.plot(df_bissecao["iteração"], df_bissecao["aproximação"], marker="o", label="Bisseção")
plt.plot(df_falsa["iteração"], df_falsa["aproximação"], marker="x", label="Falsa Posição")
plt.title("Comparação da Evolução das Aproximações")
plt.xlabel("Iteração")
plt.ylabel("Aproximação da Raiz")
plt.grid(True)
plt.legend()
plt.show()
