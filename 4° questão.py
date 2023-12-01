import numpy as np
import matplotlib.pyplot as plt
def funcao(x):
    return np.exp(x) + np.sin(x)**3
def derivada_exata(x):
    return np.exp(x) + 3 * np.sin(x)**2 * np.cos(x)
def derivada_numerica(x, h):
    return (funcao(x + h) - funcao(x - h)) / (2 * h)
# Valores de x
x_valores = np.linspace(-2, 2, 500)
y_valores = funcao(x_valores)
derivada_exata_valores = derivada_exata(x_valores)
derivada_numerica_h_01 = derivada_numerica(x_valores, 0.1)
derivada_numerica_h_001 = derivada_numerica(x_valores, 0.001)
# Plote
plt.figure(figsize=(12, 8))
# Plotar a função original
plt.subplot(3, 1, 1)
plt.plot(x_valores, y_valores, label='Função Original', color='blue')
plt.title('Função Original')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# Plotar a derivada exata
plt.subplot(3, 1, 2)
plt.plot(x_valores, derivada_exata_valores, label='Derivada Exata', linestyle='--', linewidth=2, color='green')
plt.title('Derivada Exata')
plt.xlabel('x')
plt.ylabel('y\'')
plt.legend()
# Plotar as derivadas numéricas
plt.subplot(3, 1, 3)
plt.plot(x_valores, derivada_numerica_h_01, label='Derivada Numérica (h=0.1)', linestyle='-.', linewidth=2, color='red')
plt.plot(x_valores, derivada_numerica_h_001, label='Derivada Numérica (h=0.001)', linestyle=':', linewidth=2, color='purple')
plt.title('Derivadas Numéricas')
plt.xlabel('x')
plt.ylabel('y\'')
plt.legend()

plt.tight_layout()
plt.show()
