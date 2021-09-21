#!python
#   Funzioni che calcolano gli errori
def approx(x, delta):
    """
    Calcola l'approssimazione di x dato x stesso e una perturbazione.
    """
    return x + delta

def delta(x, approx):
    """
    Restituisce la perturbazione di un valore data la sua approssimazione
    e il valore teorico.
    """
    return approx - x

def abserr(x, approx):
    """
    Calcola l'errore assoluto dato un valore x e la sua approssimazione.
    """
    return abs(x - approx)

def relerr(x, approx):
    """
    Calcola l'errore relativo dato un valore x e la sua approssimazione.
    """
    if x == 0:
        print("Errore: impossibile calcolare l'errore per x = 0")
    else:
        return abs(x - approx) / abs(x)

#   Funzioni che calcolano i fattori di amplificazione degli errori su alcune operazioni base
def sumamplx(x, y):
    """
    Calcola il fattore di amplificazione dell'errore relativo di x, er(x).
    """
    if x + y == 0:
        print("Errore: impossibile calcolare il fattore per x + y = 0")
    else:
        return abs(x) / abs(x + y)

def sumamply(x, y):
    """
    Calcola il fattore di amplificazione dell'errore relativo di y, er(y).
    """
    if x + y == 0:
        print("Errore: impossibile calcolare il fattore per x + y = 0")
    else:
        return abs(y) / abs(x + y)

def prodampl(x, xapprox, y, yapprox):
    """
    Calcola il fattore di amplificazione dell'errore relativo del prodotto tra due numeri.
    """
    return relerr(x, xapprox) * relerr(y, yapprox)

#   Funzione che calcola il prodotto tra due numeri in due modi diversi,
#   confrontando i risultati per misurarne l'errore
def prodsum(a, N):
    """
    Calcola l'errore assoluto tra il prodotto tra due numeri calcolato
    mediante l'operatore * e mediante un procedimento iterativo.
    """
    P = a * N
    S = 0
    for n in range(N):
        S = S + a
    print('prodotto: %30.40f' % P)
    print('somma:    %30.40f' % S)
    print('Errore:   %e' % abserr(P, S))

#   Funzione che calcola il condizionamento della somma tra due numeri
def sumcond(x, xapprox, y, yapprox):
    """
    Controlla se la somma tra x e y sia ben condizionata o meno.
    """
    S = x + y
    St = xapprox + yapprox
    Esum = relerr(S, St)
    print('Somma:                        %f' % S)
    print('Errore relativo della somma:  %f' % Esum)
    print('Approssimazione della somma:  %f' % St)
    cond = (sumamplx(x, y) * relerr(x, xapprox)) + (sumamply(x, y) * relerr(y, yapprox))
    print('Condizionamento del problema: %f' % cond)    
    #   Per valori minori o uguali ad uno,
    #   gli errori relativi sugli addendi
    #   non vengono amplificati.
    if cond <= 1:
        print('Il problema è ben condizionato.')
    else:
        print('Il problema è mal condizionato.')
        
if __name__ == '__main__':
    #   Esecuzione delle funzioni di calcolo dell'errore
    x = 2.34
    deltax = -0.2 
    print('Dato teorico:          %f' % x)
    print('Perturbazione:         %f' % deltax)
    print('Approssimazione:       %f' % approx(x, deltax))
    print()

    x = 2.34
    deltax = -0.2
    xapprox = approx(x, deltax)
    print('Dato teorico:          %f' % x)
    print('Approssimazione:       %f' % approx(x, deltax))
    print('Perturbazione:         %f' % delta(x, xapprox))
    print()

    x = 1000000
    xapprox = 1000000.5
    print('Dato teorico:    %f' % x)
    print('Approssimazione: %f' % xapprox)
    print('Errore assoluto: %f' % abserr(x, xapprox))
    print()
    x = 2
    xapprox = 2.1
    print('Dato teorico:    %f' % x)
    print('Approssimazione: %f' % xapprox)
    print('Errore assoluto: %f' % abserr(x, xapprox))
    print()

    x = 1000000
    xapprox = 1000000.5
    print('Dato teorico:    %f' % x)
    print('Approssimazione: %f' % xapprox)
    print('Errore relativo: %.7f' % relerr(x, xapprox))
    print()
    x = 2
    xapprox = 2.1
    print('Dato teorico:    %f' % x)
    print('Approssimazione: %f' % xapprox)
    print('Errore relativo: %f' % relerr(x, xapprox))
    print()
    
    #   Esecuzione delle funzioni di calcolo dei fattori di amplificazione degli errori
    x = 2.34562
    y = -2.34563    
    print('|x| / |x - y| = %f' % sumamplx(x, y))
    print()  
    print('|y| / |x - y| = %f' % sumamply(x, y))
    print()
    
    print('er(x) * er(y) = %f' % prodampl(2, 2.1, 3, 2.9))
    print()

    x = 2
    y = 3.14
    # Perturbazione dei dati
    xt = 2.12
    yt = 2.99
    sumcond(x, xt, y, yt)
    print()
    #   Esecuzione con dati vicini tra loro ma di segno opposto
    sumcond(2, 2.1, -1.9, -2.05)
    print()
    
    #   Test della funzione di confronto tra metodi di prodotto
    prodsum(0.12, 10000000)
    print()
