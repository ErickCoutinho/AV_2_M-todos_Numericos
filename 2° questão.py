import numpy as np
import matplotlib.pyplot as plt

#pontos
x1 = np.array([1,2])
x2 = np.array([2,0.4])
x3 = np.array([3,3])
x4 = np.array([4,3.5])
#arrays
x = np.array([x1[0], x2[0], x3[0], x4[0]])
y = np.array([x1[1], x2[1], x3[1], x4[1]])

grau_polinomio = len(x) - 1
# Ajuste do polinômio aos pontos
coeficientes = np.polyfit(x, y, grau_polinomio)
# Criar o polinômio a partir dos coeficientes
polinomio = np.poly1d(coeficientes)
print(f'O polinomia que interpola os pontos é:{polinomio}')
print('Os números "3" e "2" no print representam os graus dos termos do polinômio.')
print('Polinômio: \n-1.05x^3 + 8.4x^2 - 19.45x + 14.1 ')

# Avaliar o polinômio em pontos específicos para plotagem
x_valores = np.linspace(min(x), max(x), 100)
y_valores = polinomio(x_valores)

# Plotar os pontos e o polinômio interpolado
plt.scatter(x, y, label='Pontos dados')
plt.plot(x_valores, y_valores, label='Polinômio interpolado', color='green')
plt.title('Interpolação Polinomial')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
