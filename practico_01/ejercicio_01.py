"""Ejercicio 1: Bloque IF, operadores lógicos, función max y operador ternario"""


def maximo(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor sin utilizar la función max"""
    if a > b:
        return a
    return b


# NO MODIFICAR - INICIO
assert maximo(10, 5) == 10
assert maximo(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir la función utilizando el built-in max
    Referencia: https://docs.python.org/3/library/functions.html#max
    """
    return max(a, b)


# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """CHALLENGE OPCIONAL: Re-escribir la función utilizando el operador ternario
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    """
    return b if a > b else a


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
