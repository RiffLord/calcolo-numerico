#!python
import math
import numpy as np
from fractions import Fraction
from matplotlib import pyplot as plt

def bisezionisucc(fun, a, b, tol):
    #   Verifica delle condizioni di presenza della radice in [a, b]
    fa = fun(a)
    fb = fun(b)

    # Grafico della funzione
    x = np.linspace(a, b)
    y = np.array([fun(i) for i in x])
    plt.plot(x, y, 'b-')
    
    if fa * fb > 0:
        print('Errore: radice in [%f, %f] non garantita.' % (a, b))
    else:
        n = math.ceil((math.log(b - a) - math.log(tol)) / math.log(2))
        for k in range(n + 1):
            c = (a + b) / 2
            fc = fun(c)
            ast = Fraction(a).limit_denominator(100)
            bst = Fraction(b).limit_denominator(100)
            cst = Fraction(c).limit_denominator(100)
            print('[a, b]=[%5s, %5s] f(a)=%f f(b)=%f c=%s f(c)=%f' % (ast, bst, fa, fb, cst, fc))
            if abs(fc) < 1.0e-14:
                break
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            #   Grafico dei punti
            plt.plot(c, 0, 'r+')
            txt = '$c_{%d}$' % k
            plt.text(c, -0.8, txt, fontsize=10)

    plt.show()
    return c

def newton(fun, df, x0, tol, itmax):
    #   Calcolo dei punti iniziali
    fx0 = fun(x0)
    dfx0 = df(x0)
    it = 0          #    Contatore delle iterazioni
    stop = False
    plt.plot(x0, 0, 'r+')
    #   Iterazione
    while not stop and it < itmax:
        x1 = x0 - float(fx0 / dfx0)
        fx1 = fun(x1)
        #   Grafico della tangente in x0
        plt.plot(x0, fx0, 'r.')
        plt.plot(np.array([x0, x0]), np.array([0, fx0]), 'k:', linewidth=0.4)
        plt.plot(np.array([x0, x1]), np.array([fx0, 0]), 'k-', linewidth=0.4)
        plt.plot(x1, 0, 'r+')
        #   Criteri di arresto
        stop = (abs(x1-x0) < tol) and abs(fx1) < tol
        it = it + 1
        if not stop:
            x0 = x1
            fx0 = fx1
            dfx0 = df(x0)
    #   Verifica della convergenza
    if not stop:
        print('Errore: il metodo non converge in %d iterazioni con tolleranza %f' % (it, tol))
    return x1

if __name__ == '__main__':
    def funzione(x):
        y = math.cos(x) + 2 * math.sin(x)
        return y
    print('Radice di cos(x) + 2 * sin(x): %15.12f' % bisezionisucc(funzione, 0, 5, 1.0e-3))

    def f(x):
        y = pow(x, 3) - 4
        return y

    #   Derivata di f(x)
    def df(x):
        y = 3 * pow(x, 2)
        return y

    x = np.linspace(-1.5, 2.5)
    y = np.array([f(i) for i in x])

    #   Grafico della funzione
    graph = plt.figure()
    graph.add_subplot(111)
    plt.plot(x, y, 'b-')

    # Calcolo della radice
    z = newton(f, df, 2.0, 1.0e-10, 22)
    print('Radice di f(x): %f' % z)
    plt.show()

            
