#!python
import math

def normalize(x):
    """
    Restituisce il dato in input in forma normalizzata.
    """
    exp = 0
    while abs(x) < 0.1 or abs(x) >= 1:
    	if abs(x) >= 1:
    		x = x / 10
    		exp = exp + 1
    	elif abs(x) < 0.1:
    		x = x * 10
    		exp = exp - 1
    return (x, exp)

#   Funzioni che calcolano i valori fondamentali dei sistemi floating-point
def epsilon():
    """
    Restituisce il roundoff di un numero in virgola mobile.
    """
    U = 1.0
    while 1 + U > 1:
        Utemp = U
        U = U / 2
    U = Utemp
    return U

def precision(eps=epsilon(), base=2):
    """
    Restituisce il numero di cifre della mantissa
    (di un sistema binario con il bit nascosto).
    """
    return 1 - (math.log(eps) / math.log(base))

def digits(prec=precision(), base=2):
    """
    Restituisce un'approssimazione del numero di
    cifre significative per rappresentare un numero.
    """
    return prec * math.log10(base)

def deshift(bits=64):
    """
    Restituisce gli estremi effettivi (senza shifting)
    dell'intervallo degli esponenti ammissibile
    per una data precisione di un sistema in virgola mobile.
    """
    if bits == 8:
        c = 4
    elif bits == 16:
        c = 5
    elif bits == 32:
        c = 8
    elif bits == 64:
        c = 11
    elif bits == 128:
        c = 15
    else:
        print("Error: %d-bit precision doesn't exist" % bits)
        return (0, 0)
    #   Si sottrae 1 perchè gli estremi dell'intervallo
    #   sono solitamente riservati per scopi speciali.
    M = pow(2, c) - 1
    #   Calcola gli estremi effettivi dell'intervallo degli esponenti
    return (-((M - 1) / 2) + 1, (M - 1) / 2)

def realmin(m=deshift()[0]):
    """
    Calcola il più piccolo numero di macchina rappresentabile al calcolatore.
    """
    return pow(2, m)

def realmax(prec=epsilon(), M=deshift()[1]):
    """
    Calcola il più grande numero di macchina rappresentabile al calcolatore.
    """
    return (2 - pow(2, -prec)) * pow(2, M)

if __name__ == '__main__':
    x = 57968.43
    print('normalize:          %f = %f * 10^%d' % (x, normalize(x)[0], normalize(x)[1]))
    x = -0.00036549100
    print('normalize:          %f = %f * 10^%d' % (x, normalize(x)[0], normalize(x)[1]))
    x = 0.463
    print('normalize:          %f = %f * 10^%d' % (x, normalize(x)[0], normalize(x)[1]))
    print()
    
    print('calling numpy.finfo(numpy.float).eps')
    import numpy as np
    print('                         %.52f' % np.finfo(float).eps)
    print('epsilon machine:         %.52f' % epsilon())
    print('1 + epsilon =            %.52f' % (1 + epsilon()))
    print('1 + (epsilon - 0.5999) = %.52f' % (1 + (epsilon() - 0.5999)))
    print()
    
    print('precision:    %d' % precision())
    print()
    
    print('significant digits: %.2f' % digits())
    print()
    
    print('exp64bit:           [%d, %d]' % deshift())
    print()
    
    print('realmin:            %.500f' % realmin())
    print()
    #   Provocherà una situazione di underflow
    print('realmin - 1:        %.500f' % (realmin() - 1))
    print()
    
    print('realmax:            %.4f' % realmax())
    print()
    print('realmax + 1 = %.4f' % (realmax() + 1))
