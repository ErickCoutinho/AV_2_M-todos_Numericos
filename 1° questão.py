import numpy as np
A = np.array([[1, 2, -1, 0],
              [2, -1, 0, 0],
              [0, -1, 2, -1],
              [0, 0, -1, 2]])
b = np.array([[1],
             [1],
             [1],
             [1,]])
x0 = np.zeros_like(b)
autovalores = np.linalg.eigvals(A)
print("Autovalores da matriz A:", autovalores)

print('A solução exata é:\n',np.linalg.inv(A)@b)
def jacobi(A, b, x0, tol, N):
    # Preliminares
    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')
    n = np.shape(A)[0]
    x = np.zeros(n)
    it = 0

    # Iterações
    while it < N:
        it += 1
        # Iteração de Jacobi
        for i in np.arange(n):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i + 1, n))):
                x[i] -= A[i, j] * x0[j]
            x[i] /= A[i, i]
        # Tolerância
        if np.linalg.norm(x - x0, np.inf) < tol:
            return x
        # Prepara nova iteração
        x0 = np.copy(x)
    raise NameError('Número máximo de iterações excedido.')

result = jacobi(A,b,x0, 0.0001,5000)
print(result)


def gauss_seidel(A, b, x0, tol, N):
    # preliminares
    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')

    n = np.shape(A)[0]
    x = np.copy(x0)
    it = 0
    # iteracoes
    while (it < N):
        it = it + 1
        # iteracao de Jacobi
        for i in np.arange(n):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i + 1, n))):
                x[i] -= A[i, j] * x[j]
            x[i] /= A[i, i]
            print(x[i], A[i, i])
            # tolerancia
        if (np.linalg.norm(x - x0, np.inf) < tol):
            return x
            # prepara nova iteracao
        x0 = np.copy(x)
    raise NameError('num.max.deiteracoes excedido.')

result_2 = gauss_seidel(A, b, x0, 0.0001, 5000)
print(result_2)



