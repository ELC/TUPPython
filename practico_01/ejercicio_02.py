"""Ejercicio 2: Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros,
introducción a la recursividad
"""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Devolver el máximo utilizando UNICAMENTE tres IFs y comparaciones encadenadas
    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons
    """
    if b < a > c:
        return a
    if a < b > c:
        return b
    if a < c > b:
        return c


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(24, 9, 18) == 24
# NO MODIFICAR - FIN


###############################################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    """Modificar la función para que tome 4 parámetros, utilizar el built-in max"""
    return max(a, b, c, d)


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_arbitrario(*args) -> float:
    """Modificar la función para que tome una cantidad arbitraria de parámetros
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    """
    return max(args)


# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_recursivo(*args) -> float:
    """CHALLENGE OPCIONAL: Re-Escribir la función de forma recursiva."""
    primero, *resto = args

    if resto == []:
        return primero

    return max(primero, maximo_recursivo(*resto))


# NO MODIFICAR - INICIO
assert maximo_recursivo(1, 10, 5, -5) == 10
assert maximo_recursivo(4, 9, 18, 6) == 18
assert maximo_recursivo(24, 9, 18, 20) == 24
assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
