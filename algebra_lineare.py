#!python
import math
import numpy as np
from matplotlib import pyplot as plt

#   Vettori
def vectorsum(A, B):
    """
    Restituisce la somma tra due vettori.
    """
    C = []
    if len(A) == len(B):
        for i in range(len(A)):
            C.append([A[i] + B[i]])
    else:
        print('Errore: impossibile sommare due vettori di dimensioni differenti.')
    return C
    
def vectorprod(A, B):
    """
    Restituisce il prodotto scalare tra due vettori.
    """
    lenA = len(A)
    lenB = len(B)
    #   Verifica le dimensioni dei vettori.
    if lenA == lenB:
        AB = 0
        for i in range(lenA):
            AB = AB + A[i] * B[i]
        return AB
    else:
        print('Errore: impossibile calcolare il prodotto tra vettori di dimensioni differenti.')
        return False

def scaltimesvec(a, A):
    """
    Restituisce il prodotto tra uno scalare e un vettore.
    """
    for i in range(len(A)):
        A[i] = a * A[i]
    return A

def vectornorm1(A):
    """
    Restituisce la norma vettoriale 1 di un dato vettore.
    """
    result = 0
    for i in range(len(A)):
        result = result + abs(A[i])
    return result

def euclidnorm(A):
    """
    Restituisce la norma euclidea (norma 2) di un dato vettore.
    """
    result = 0
    for i in range(1, len(A)):
        result = result + (A[i] ** 2)
    return math.sqrt(result)

def vecinfnorm(A):
    """
    Restituisce la norma infinito di un dato vettore.
    """
    max = 0
    for i in range(1, len(A)):
        if (abs(A[i]) > max):
            max = abs(A[i])
    return max

#   Matrici
def scaltimesmatrix(A, s):
    """
    Restituisce il prodotto di uno scalare per una matrice.
    """
    rows = len(A)
    cols = len(A[0])
    b = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            b[i][j] = s * A[i][j]
    return b

def matrixsum(A, B):
    """
    Restituisce la somma tra due matrici.
    """
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    if rowsA == rowsB and colsA == colsB:
        C = np.zeros((rowsA, colsA))
        for i in range(rowsA):
            for j in range(colsA):
                C[i][j] = A[i][j] + B[i][j]
        return C
    else:
        print('Errore: le matrici hanno dimensioni differenti.')
        return False

def matrixprod(A, B):
    """
    Restituisce il prodotto tra due matrici.
    """
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    if colsA == rowsB:
        C = np.zeros((rowsA, colsA))
        for i in range(rowsA):
            for j in range(colsB):
                temp = 0
                for k in range(colsA):
                    temp = temp + A[i][k] * B[k][j]
                C[i][j] = temp 
        return C
    else:
        print('Errore: il numero di colonne della prima matrice è diverso dal numero di righe della seconda.')
        return False

def matrixnorm1(A):
    """
    Restituisce la norma matriciale 1 di una data matrice.
    """
    rows = len(A)
    cols = len(A[0])
    max = 0
    if rows == cols:
        for j in range(cols):
            sum = 0
            for i in range(1, rows):
                sum = sum + abs(A[i][j])
            if sum > max:
                max = sum
    else:
        print('Errore: la matrice non è quadrata')
    return max

def matrixinfnorm(A):
    """
    Restituisce la norma matriciale infinito di una data matrice.
    """
    rows = len(A)
    cols = len(A[0])
    max = 0
    if rows == cols:
        for i in range(rows):
            sum = abs(A[i][0])
            for j in range(1, cols):
                sum = sum + abs(A[i][j])
            if sum > max:
                max = sum
    else:
        print('Errore: la matrice non è quadrata.')
    return max

def forwardsub(L, b):
    """
    Implementazione dell'algoritmo di sostituzione
    in avanti per la risoluzione di sistemi triangolari
    con matrice triangolare inferiore.
    """
    size = len(L)
    x = np.zeros(size)
    x[0] = b[0] / L[0][0]   #   Si calcola la prima equazione del sistema
    for i in range(1, size + 1, 1): #   Ciclo sulle righe
        S = 0
        for j in range(1, i, 1):    #   Ciclo sulle colonne
            S = S + L[i - 1][j - 1] * x[j - 1]
        x[i - 1] = (b[i - 1] - S) / L[i - 1][i - 1]
    return x

def backwardsub(U, b):
    """
    Implementazione dell'algoritmo di sostituzione all'indietro
    per la risoluzione di sistemi triangolari con
    matrice triangolare superiore.
    """
    size = len(U)
    x = np.zeros(size)
    for i in range(size - 1, -1, -1):   #   Ciclo sulle righe
        S = 0
        for j in range(i + 1, size):    #   Ciclo sulle colonne
            S = S + U[i][j] * x[j]
        x[i] = (b[i] - S) / U[i][i]
    return x

def gauss(A, b):
    """
    Trasforma un dato sistema in uno equivalente di tipo triangolare superiore.
    """
    size = len(A)
    for j in range(size):
        #   Eliminazione di Gauss
        for i in range(j + 1, size):
            m = -(A[i][j]/A[j][j])
            A[i][j] = 0
            for k in range(j + 1, size):
                A[i][k] = A[i][k] + m * A[j][k]
            b[i] = b[i] + m * b[j]

def gausspivot(A, b):
    """
    Trasforma un dato sistema in uno equivalente di tipo triangolare superiore.
    """
    size = len(A)
    for j in range(size):    #   Ciclo sulle colonne
        #   Ricerca della riga pivot
        Amax = abs(A[j][j])
        imax = j
        for i in range(j + 1, size):
            if abs(A[i][j]) > Amax:
                Amax = abs(A[i][j])
                imax = i
        #   Scambio di riga j con imax
        if imax > j:
            for k in range(j, size):
                Atemp = A[j][k]
                A[j][k] = A[imax][k]
                A[imax][k] = Atemp
            btemp = b[j]
            b[j] = b[imax]
            b[imax] = btemp
        #   Eliminazione di Gauss
        for i in range(j + 1, size):
            m = -(A[i][j] / A[j][j])
            A[i][j] = 0
            for k in range(j + 1, size):
                A[i][k] = A[i][k] + m * A[j][k]
            b[i] = b[i] + m * b[j]

def determ(A):
    """
    Restituisce il determinante di una matrice, sfruttando l'algoritmo di Gauss.
    """
    #   Verifica che la matrice sia quadrata
    rows = len(A)
    cols = len(A[0])
    if rows == cols:
        #   Trasforma la matrice in una matrice triangolare equivalente
        gauss(A, np.zeros(cols))
        #   Il determinante di una matrice triangolare
        #   equivale al prodotto degli elementi
        #   sulla diagonale principale
        det = A[0][0]
        for i in range(1, rows):
            det = det * A[i][i]
        return det
    else:
        print('Errore: la matrice non è quadrata.')
        return False

if __name__ == '__main__':
    # Esecuzione delle funzioni sui vettori con dati di prova
    A = [0, 1, 2, 3, 4, 5]
    B = [5, 4, 3, 2, 1, 0]
    print('A:     ', A)
    print('B:     ', B)
    print('A + B = ', vectorsum(A, B))
    print()

    print('A:     ', A)
    print('B:     ', B)
    print('A * B = %d' % vectorprod(A, B))
    print()
    
    C = [0, 1, 2, 3]
    D = [0, 1]
    print('C:      ', C)
    print('D:      ', D)
    print('C * D =  %d' % vectorprod(C, D))
    print()

    print('A:      ', A)
    print('4 * A = ', scaltimesvec(4, A))
    print()

    print('A: ', A)
    print('Vector Norm 1: %d' % vectornorm1(A))
    print()

    print('A: ', A)
    print('Norma euclidea: %f' % euclidnorm(A))
    print()
    
    print('A: ', A)
    print('Norma infinito: %d' % vecinfnorm(A))
    print()

    #   Esecuzione delle funzioni sulle matrici con dati di prova   
    E = [[0, 1, 2], [2, 1, 0], [1, 0, 2]]
    print('E:      ', E)
    print('E * 3 = ', scaltimesmatrix(E, 3))
    print()
    
    F = [[2, 1, 0], [0, 1, 2], [2, 0, 1]]
    print('E:      ', E)
    print('F:      ', F)
    print('E + F = ', matrixsum(E, F))
    print()
    
    G = [[0, 1], [1, 0]]
    print('E:      ', E)
    print('G:      ', G)
    print('E + G = ', matrixsum(E, G))
    print()
    
    print('E:      ', E)
    print('F:      ', F)
    print('E * F = ', matrixprod(E, F))
    print()
    
    print('E:      ', E)
    print('G:      ', G)
    print('E * G = ', matrixprod(E, G))
    print()

    print('A:                 ', [[1, 5, 8], [2, 7, 4], [4, 3, 2]])
    print('Norma matriciale 1: %d' % matrixnorm1([[1, 5, 8], [2, 7, 4], [4, 3, 2]]))
    print()

    print('B:                 ', [[0, 1, 2], [2, 1, 0]])
    print(matrixnorm1([[0, 1, 2], [2, 1, 0]]))
    print()

    print('A:                        ', [[1, 5, 8], [2, 7, 4], [4, 3, 2]])
    print('Norma matriciale infinito: %d' % matrixinfnorm([[1, 5, 8], [2, 7, 4], [4, 3, 2]]))
    print()

    print('B:                        ', [[0, 1, 2], [2, 1, 0]])
    print(matrixinfnorm([[0, 1, 2], [2, 1, 0]]))
    print()

    print('L:                        ', [[2, 0, 0], [4, 10, 0], [16, 8, 10]])
    print('b:                        ', [6, 3, 2])
    print('Sostituzione in avanti:')
    print('Vettore delle incognite:')
    print(forwardsub([[2, 0, 0], [4, 10, 0], [16, 8, 10]], [6, 3, 2]))
    print()

    print('U:                        ', [[6, 5, 1], [0, 1, 7], [0, 0, 2]])
    print('b:                        ', [3, 2, 1])
    print("Sostituzione all'indietro:")
    print('Vettore delle incognite:')
    print(backwardsub([[6, 5, 1], [0, 1, 7], [0, 0, 2]], [3, 2, 1]))
    print()

    H = [[1, 2, 2], [-2, 1, 4], [4, 3, -6]]
    b = [1, 3, 0]
    print('H:                                          ', H)
    print('b:                                          ', b)
    print('Metodo di eliminazione di Gauss')
    gauss(H, b)
    print('H:                                          ', H)
    print('b:                                          ', b)
    print() 
    print("Sostituzione all'indietro")
    print(backwardsub(H, b))
    print()    
    
    H = [[1, 2, 2], [-2, 1, 4], [4, 3, -6]]
    b = [1, 3, 0]
    print('H:                                          ', H)
    print('b:                                          ', b)
    print('Metodo di eliminazione di Gauss con pivot')
    gausspivot(H, b)
    print('H:                                          ', H)
    print('b:                                          ', b)
    print() 
    print("Sostituzione all'indietro")
    print(backwardsub(H, b))
    print()

    H = [[1, 2, 2], [-2, 1, 4], [4, 3, -6]]
    print('H:                                          ', H)
    print('Determinante di H:                          ', determ(H))
    print()

    B = [[0, 1], [2, 3], [4, 5]]
    print('B:                                          ', B)
    print('Determinante di B:                          ', determ(B))
    print()
