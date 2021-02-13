"""Único return vs múltiples return"""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Implementar la función operacion_basica, donde:
        - Si multiplicar es True: devolver la multiplicación entre a y b.
        - Si multiplicar es False: devolver la division entre a y b.
        - Si multiplicar es False y b es cero: devolver "Operación no válida".

    Restricciones:
        - Utilizar un único return
        - No utilizar AND ni OR
    """

    if multiplicar:
        result = a * b
    else:
        if b == 0:
            result = "Operación no válida"
        else:
            result = a / b
    return result


# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN


###############################################################################


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Re-Escribir utilizando tres returns"""

    if multiplicar:
        return a * b
    if b == 0:
        return "Operación no válida"
    return a / b


# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN
