"""Any y Sets."""

from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricción: Utilizar bucles anidados.
    """
    for elem in lista_1:
        for elem_ in lista_2:
            if elem == elem_:
                return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN."""
    for elem in lista_1:
        if elem in lista_2:
            return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando sin bucles, el operador in y la funcion any.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return any(elem in lista_2 for elem in lista_1)


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).
    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """
    return len(set(lista_1) & set(lista_2)) != 0


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
