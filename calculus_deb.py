
import numpy as np

# MATRIZ INVERSA

A = np.array([[1,4,3],[-1,-2,0],[2,2,3]])
print("A: \n", np.linalg.inv(A) , "\n")

B = np.array([[1,1,1],[0,1,1],[0,0,1]])
print("B: \n", np.linalg.inv(B), "\n")

C = np.array([[2,0,5],[0,3,0],[ 1,0,3]])
print("C: \n", np.linalg.inv(C), "\n")

D = np.array([[-1,-3,-3],[0,6,1],[3,8,3]])
print("D: \n", np.linalg.inv(D), "\n")

E = np.array([[1,0,1],[-1,1,1],[-1,-2,-3]])
print("E: \n", np.linalg.inv(E), "\n")

# No Octave
# Obs: nas funções do octave mais do que apenas resolver ele passa por uma serie de funções que garante que
#  a resposta esta distribuida da melhor forma matematicamente escolhendo o melhor método de resolução para a matriz em questão.
# Cria matriz: A=[123;234;108];
# Inversa: inv(A)
# Resolve sistema:  x = A\b
# Decomposição: rref([A b]) -> concatenar as matrizes

# Transpor A.T
# Dimensões A.shape
# Mudar dimensões v = np.array([1, 2, 3]).reshape(3, 1) == [[1], [2], [3]]
#   também pode usar sem definir o novo reshape e ele faz automatico v = np.array([1, 2, 3]).reshape(-1, 1)
# Criar array zerado np.zeros((3, 2)) == [[0., 0.], [0., 0.], [0., 0.]]
# Criar array de numeros UM np.ones((2, 3)) == [[1, 1, 1], [1, 1, 1]]
# Criar array de numeros randomicos np.random.rand(3, 2)
# identity_matrix = np.eye(3) or shifted_identity = np.eye(4, k=1)

# Multiplica matrizes  A * B ou A @ v

# Sistema de Equações lineares
# Ax = b // numero de colunas deve ser o numero de linhas das matrizes calculadas ex: (3x3) * (3x1) = (3x1)
# vetor A do tamanho das linhas e vetor B das colunas
# duas retas no plano cartesiano, na intersecção temos a solução única

# Sistemas de equações lineares np.linalg.solve(A, b)

# { 4x + 3y - 5z = 2
# -2x - -4y + 5z = 5
# 8x + 8y = -3 }
#
# A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])
# y = np.array([2, 5, -3])
# x = np.linalg.solve(A, y)

# Decomposição LU
# from scipy.linalg import lu
# P, L, U = lu(A)

# adição soma os sistemas multiplicando por -x uma das equações
# substituição faz uma distributiva em uma unica função para ter apenas uma variavel e depois com o valor de um deles retorna.
# igualação

# Métodos de resolução de Sistemas de Equações Lineares
# algébrico:  matriz inversa regra de cramer / escalonamento Gauss / Gauss-Jordan
# numerico:  Jacobi / Gauss-Seidel / Decomposição LU

A = np.array([[2, 9], [3, 4]])
y = np.array([5, 7])
x = np.linalg.solve(A, y)
print("\n Solved equation", x)
print("Inversa: \n", np.linalg.inv(A), "\n")
print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

# esse não tem solução
A = np.array([[1, 3, -4], [2, 6, -8]])
y = np.array([1,1])
#x = np.linalg.solve(A, y)
#print("\n Solved equation", x)
#print("Inversa: \n", np.linalg.inv(A), "\n")

def rref(A, tol=1.0e-12):
    ''' input: a matrix (2D array)
       output: rref form of the matrix, and a tuple of pivot columns
    '''
    m, n = A.shape
    i, j = 0, 0
    jb = [] # list of pivot columns

    while i < m and j < n:
        # Find value and index of largest element in the remainder of column j
        k = np.argmax(np.abs(A[i:m, j])) + i
        p = np.abs(A[k, j])
        if p <= tol:
            # The column is negligible, zero it out
            A[i:m, j] = 0.0
            j += 1
        else:
            # Remember the column index
            jb.append(j)
            if i != k:
                # Swap the i-th and k-th rows
                A[[i, k], j:n] = A[[k, i], j:n]
            # Divide the pivot row i by the pivot element A[i, j]
            A[i, j:n] = A[i, j:n] / A[i, j]
            # Subtract multiples of the pivot row from all the other rows
            for k in range(m):
                if k != i:
                    A[k, j:n] -= A[k, j] * A[i, j:n]
            i += 1
            j += 1
    # Finished
    return A, tuple(jb)

print("\nRref:", str(rref(A)))


A = np.array([[3, -4], [6, -10]])
y = np.array([5, 2])
x = np.linalg.solve(A, y)
print("\n Solved equation", x )
print("\nInversa:", np.linalg.inv(A), "\n")
print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")
print("\nRref:", str(rref(A)))

A = np.array([[3, -4], [6, -8]])
y = np.array([5, 2])

try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
    print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")


A = np.array([[3, 2, -9], [-9, -5, 2], [6,7,3]])
y = np.array([-65, 16, 5])

print("\nEXERCICIO 4: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")
  print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 4: -------}")

A = np.array([[ 5, -3], [7, -2]])
y = np.array([21, 36])

print("\nEXERCICIO 5: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")
  print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 5: -------}")

s34 = np.sqrt(34)
s35 = np.sqrt(35)
s42 = np.sqrt(42)
A = np.array([[1/s35, -(3/s34), 1/s42], [3/s35, 0, -(4/s42)], [-(5/s35),5/s34, -(5/s42)]])
y = np.array([0, 0, 1])

print("\nEXERCICIO 6: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")
  print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 6: -------}")

A = np.array([[0, 1], [5, 1], [10, 1]])
y = np.array([2, 6, 11])

print("\nEXERCICIO 7: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")
  print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 7: -------}")

A = np.array([[1, 1], [1,2], [1, 5]])
y = np.array([1, 3, 10])

print("\nEXERCICIO 8: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
    print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")
except:
  print("An exception occurred tryig to use INVERSA - INF")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 8: -------}")

A = np.array([[1,1],[1,2],[1,5]])
y = np.array([1, 3, 9])

print("\nEXERCICIO 9: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
    print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

except:
  print("An exception occurred tryig to use INVERSA - INF")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 9: -------}")

A = np.array([[5, 3, 3], [3, 3, 4]])
y = np.array([40, 30])

print("\nEXERCICIO 10: -------{")
try:
  x = np.linalg.solve(A, y)
  print("\n Solved equation", x)
except:
  print("An exception occurred tryig to use SOLVE - INF")

try:
    print("\nInversa:", np.linalg.inv(A), "\n")
    print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

except:
  print("An exception occurred tryig to use INVERSA - INF")

try:
    print("\nRref:", str(rref(A)))
except:
    print("An exception occured trying to use RREF")
print("\nEXERCICIO 10: -------}")

# Existência da unicidade de soluções
# o posto de uma matriz (rank) é um conceito que mede o número de linhas ou colunas
# linearmente independentes em uma matriz.
# O conjunto Ax = b com m equações e n variáveis tem soluções se

# matrix MxN
# n == numero de colunas
# menos linhas do que colunas == infinitas soluções

# Soluçã única = inversa ou divisão a esquerda
# Infinotas = divisão a esquerda, rref
# nenhuma solução = divisão a esquerda retorna a solução de mínimos quadrados

# unica = n
# infinitas < n

from numpy.linalg import matrix_rank

matrix = np.eye(4)

def solve_equations(matrix , y):
    rank = matrix_rank(matrix)
    rows, columns = matrix.shape

    if rows == rank:
        print("Esta é uma matriz com solução única")
        print("\nInversa:", np.linalg.inv(matrix) , "\n")
        print("Resultado Inversa: \n", np.linalg.inv(A) * y, "\n")

    else:
        print("\nRref:", str(rref(matrix)))

