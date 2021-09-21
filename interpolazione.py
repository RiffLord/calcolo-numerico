#!python
import numpy as np
from matplotlib import pyplot as plt

def differenzedivise(x, y):
    degree = len(x) - 1     #   Grado del polinomio
    #   Formula di Newton alle differenze divise
    d = np.copy(y)
    for j in range(1, degree + 1):
        for i in range(degree, j - 1, -1):
            d[i] = (d[i] - d[i - 1]) / (x[i] - x[i - j])
    return d

def polinomionewton(x, nodes, diff):
    degree = len(nodes) - 1 #   Grado del polinomio
    #   Calcolo del polinomio di Newton in x
    point = diff[degree]
    for i in range(degree - 1, -1, -1):
        point = diff[i] + (x - nodes[i]) * point
    return point

def rettaregressione(x0, xm, m, a, b):
    """
    Calcola e visualizza un polinomio ax + b
    mediante la retta di regressione lineare.
    """
    #   Nodi
    x = np.linspace(x0, xm, m + 1)
    #   Perturbazione casuale dei valori
    y = (b + a * x) + (np.random.rand(m + 1) - 0.5)
    #   Calcolo della retta di regressione lineare
    #       Creazione di una matrice 2 * 2 popolata da zeri
    A = np.zeros((2, 2))
    #       Creazione di un vettore di dimensione 2 popolato da zeri
    d = np.zeros(2)
    #       La matrice viene popolata con i valori appropriati
    A[0, 0] = m + 1
    A[0, 1] = np.sum(x)
    A[1, 0] = A[0, 1]
    A[1, 1] = np.sum(x ** 2)
    #       Il vettore viene popolato con i valori dei termini noti
    d[0] = np.sum(y)
    d[1] = np.sum(x * y)
    
    #   Risoluzione del sistema
    c = np.linalg.solve(A, d)
    #   Valori del grafico della retta ricostruita
    xg = np.linspace(x0, xm, m)
    yg = c[0] + c[1] * xg

    #   Visualizzazione del grafico
    plt.figure(1)
    plt.plot(xg, a * xg + b, label='b + ax')
    plt.plot(xg, yg, label='c0 + c1x')
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.legend(loc='upper left')
    plt.show()

def vandermonde():
    datarange = 17
    realerr = np.zeros(datarange)
    esterr = np.zeros(datarange)
    for n in range(1, datarange):
        #   Costruzione della matrice di Vandermonde
        A = [[i ** j for j in range(n)] for i in range(n)]
        
        #   Costruzione di un problema di test
        x_solution = [1 for i in range(n)]
        b = np.dot(A, x_solution)

        #   Risoluzione del sistema lineare
        x = np.linalg.solve(A, b)
        err = x - x_solution
        realerr[n] = np.linalg.norm(err)
        #   Numero di condizione moltiplicato per la precisione di macchina
        esterr[n] = np.linalg.cond(A) * np.finfo(float).eps
    #   Visualizzazione degli errori
    plt.semilogy(range(datarange), realerr, label='Error')
    plt.semilogy(range(datarange), esterr, label='Estimate')
    plt.xlabel('n')
    plt.legend(loc=4)
    plt.show()

if __name__ == '__main__':
    xnodes = [0, 1, 2, 3]
    ynodes = [2, -1, 0, 1]
    print('Nodi in x:         ', xnodes)
    print('Nodi in y:         ', ynodes)
    print('Risultato:         ', differenzedivise(xnodes, ynodes))
    print()
    
    x1 = 2
    x2 = 3
    x3 = 5
    p1 = polinomionewton(x1, xnodes, differenzedivise(xnodes, ynodes))
    p2 = polinomionewton(x2, xnodes, differenzedivise(xnodes, ynodes))
    p3 = polinomionewton(x3, xnodes, differenzedivise(xnodes, ynodes))
    print('Polinomio in %d: %d' % (x1, p1))
    print('Polinomio in %d: %d' % (x2, p2))
    print('Polinomio in %d: %d' % (x3, p3))
    print()
    
    #   Test della Retta di regressione lineare
    x0 = 0
    xm = 4
    m = 200
    a = 2
    b = -1
    rettaregressione(x0, xm, m, a, b)
    
    vandermonde()  
