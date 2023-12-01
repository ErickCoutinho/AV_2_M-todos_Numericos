import numpy as np
import matplotlib.pyplot as plt

# Pontos
pontos = np.array([(1, 3.25), (1.5, 3.5), (2, 3.75), (2.5, 4), (3, 4.25), (3.5, 4.5)])

# Separar os pontos em coordenadas x e y
x = pontos[:, 0]
y = pontos[:, 1]

# Realizar a regressão linear
coeficientes = np.polyfit(x, y, 1)  # O argumento "1" indica uma regressão linear (reta)
reta_regressao = np.poly1d(coeficientes)
print('Equação da reta:', reta_regressao)
x_valores_reta = np.linspace(min(x), max(x), 100)
y_valores_reta = reta_regressao(x_valores_reta)
# Plotar os pontos e a reta de regressão
plt.scatter(x, y, label='Pontos dados')
plt.plot(x_valores_reta, y_valores_reta, label='Reta de regressão', color='green')
plt.title('Reta de Regressão Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
