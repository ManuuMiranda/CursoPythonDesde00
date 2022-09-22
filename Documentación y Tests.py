import doctest
from re import *
import math

def areatriangulo(base, altura):
    """
    Calcula el area de un triángulo dado
    >>> areatriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areatriangulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areatriangulo(9,3)
    'El área del triángulo es: 13.5'

    """

    return f'El área del triángulo es: {(base*altura)/2}'


doctest.testmod()

def comprueba_mail(user_mail):
    """
    La función comprueba_mail evalúa un mail recibido en busca de la @.
    Si tiene una @ es correcto, si tiene más o esta al final es incorrecto

    >>> comprueba_mail('manueh.miranda@gmail.com')
    True

    >>> comprueba_mail('manueh.mirandagmail.com@')
    False

    >>> comprueba_mail('manueh.mirandagmail.com')
    False

    >>> comprueba_mail('manueh.miranda@gmail@.com')
    False

    """
    arroba = user_mail.count('@')

    if arroba != 1 or user_mail.rfind('@') == len(user_mail)-1 or user_mail.find('@') == 0:
        return False
    else:
        return True


def raiz_cuadrada(lista_nums):
    """
    La función devuelve una lista con la raíz cuadrada de los elementos numéricos pasados por
    :param lista_nums: en una lista

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...    lista.append(i)
    >>> raiz_cuadrada(lista)
    [2.0, 3.0, 4.0]
    >>> lista = []
    >>> for i in [4, -9, 16]:
    ...    lista.append(i)
    >>> raiz_cuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    # Esto último es para que el test funcione aunque de un error, es como hacer una excepción rara
    return [math.sqrt(n)
            for n in lista_nums]  # Lista números será la lista que le pasaremos a la función


print(raiz_cuadrada([9, 16, 25, 36]))