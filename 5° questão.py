import numpy as np

# Função a ser integrada
def f(x):
    return np.cos(2 * x)
# Solução analítica
def solucao_analitica(a, b):
    return (1 / 2) * np.sin(4) - (1 / 4) * np.sin(2)
# Métodos de Riemann
def ponto_medio(f, a, b, n):
    h = (b - a) / n
    xi = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(xi))
def trapezios(f, a, b, n):
    h = (b - a) / n
    xi = np.linspace(a, b, n + 1)
    return h / 2 * (f(a) + 2 * np.sum(f(xi[1:-1])) + f(b))
def simpson(f, a, b, n):
    if n % 2 != 0:
        n += 1  # Se n é ímpar, torná-lo par
    h = (b - a) / n
    xi = np.linspace(a, b, n + 1)
    resultado_simpson = f(a) + f(b)
    for i in range(1, n, 2):
        resultado_simpson += 4 * f(xi[i])
    for i in range(2, n - 1, 2):
        resultado_simpson += 2 * f(xi[i])
    return h / 3 * resultado_simpson
# Definindo intervalo
a, b = 2, 5
# Valores de n
n_valores = [4, 10, 25, 100]
# Tabela 1: Comparando com a solução analítica
print("Tabela 1: Comparando com a solução analítica")
print("n | Solução Analítica | Ponto Médio | Trapézios | Simpson")
print("--|-------------------|-------------|-----------|--------")
for n in n_valores:
    ponto_medio_resultado = ponto_medio(f, a, b, n)
    trapezios_resultado = trapezios(f, a, b, n)
    simpson_resultado = simpson(f, a, b, n)
    analitico = solucao_analitica(a, b)
    print(f"{n} | {analitico:.6f} | {ponto_medio_resultado:.6f} | {trapezios_resultado:.6f} | {simpson_resultado:.6f}")
# Tabela 2: Comparando os erros absolutos
print("\nTabela 2: Comparando os erros absolutos")
print("n | Erro Ponto Médio | Erro Trapézios | Erro Simpson")
print("--|------------------|-----------------|--------------")
for n in n_valores:
    ponto_medio_resultado = ponto_medio(f, a, b, n)
    trapezios_resultado = trapezios(f, a, b, n)
    simpson_resultado = simpson(f, a, b, n)
    analitico = solucao_analitica(a, b)
    erro_pm = np.abs(analitico - ponto_medio_resultado)
    erro_trap = np.abs(analitico - trapezios_resultado)
    erro_simpson = np.abs(analitico - simpson_resultado)
    print(f"{n} | {erro_pm:.6f} | {erro_trap:.6f} | {erro_simpson:.6f}")







print('\nItem B:\n')
# Função a ser integrada
def g(x):
    return x * np.log(x)
# Solução analítica
def solucao_analitica_b(a, b):
    return b * (np.log(b) - 1) - a * (np.log(a) - 1)
# Métodos de Riemann
def ponto_medio_b(f, a, b, n):
    h = (b - a) / n
    xi = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(xi))
def trapezios_b(f, a, b, n):
    h = (b - a) / n
    xi = np.linspace(a, b, n + 1)
    return h / 2 * (f(a) + 2 * np.sum(f(xi[1:-1])) + f(b))
def simpson_b(f, a, b, n):
    if n % 2 != 0:
        n += 1  # Se n é ímpar, torná-lo par
    h = (b - a) / n
    xi = np.linspace(a, b, n + 1)
    resultado_simpson = f(a) + f(b)
    for i in range(1, n, 2):
        resultado_simpson += 4 * f(xi[i])
    for i in range(2, n - 1, 2):
        resultado_simpson += 2 * f(xi[i])
    return h / 3 * resultado_simpson


# Definindo intervalo
a, b = 1, 4
# Valores de n
n_valores_b = [4, 10, 25, 100]
# Tabela 1: Comparando com a solução analítica
print("Tabela 1: Comparando com a solução analítica")
print("n | Solução Analítica | Ponto Médio | Trapézios | Simpson")
print("--|-------------------|-------------|-----------|--------")
for n in n_valores_b:
    ponto_medio_resultado = ponto_medio_b(g, a, b, n)
    trapezios_resultado = trapezios_b(g, a, b, n)
    simpson_resultado = simpson_b(g, a, b, n)
    analitico_b = solucao_analitica_b(a, b)
    print(
        f"{n} | {analitico_b:.6f} | {ponto_medio_resultado:.6f} | {trapezios_resultado:.6f} | {simpson_resultado:.6f}")
# Tabela 2: Comparando os erros absolutos
print("\nTabela 2: Comparando os erros absolutos")
print("n | Erro Ponto Médio | Erro Trapézios | Erro Simpson")
print("--|------------------|-----------------|--------------")
for n in n_valores_b:
    ponto_medio_resultado = ponto_medio_b(g, a, b, n)
    trapezios_resultado = trapezios_b(g, a, b, n)
    simpson_resultado = simpson_b(g, a, b, n)
    analitico_b = solucao_analitica_b(a, b)
    erro_pm = np.abs(analitico_b - ponto_medio_resultado)
    erro_trap = np.abs(analitico_b - trapezios_resultado)
    erro_simpson = np.abs(analitico_b - simpson_resultado)
    print(f"{n} | {erro_pm:.6f} | {erro_trap:.6f} | {erro_simpson:.6f}")

