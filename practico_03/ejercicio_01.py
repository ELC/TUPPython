# Implementar la clase Rectangulo que contiene una base y una altura, y el
# método area.

from typing import Optional


class Rectangulo:
    def __init__(self,
                 base: Optional[float] = None,
                 altura: Optional[float] = None) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> Optional[float]:
        return self.base * self.altura


# NO MODIFICAR - INICIO

# Test Constructor
rec = Rectangulo(10, 10)
assert rec.base == 10
assert rec.altura == 10
assert rec.area() == 100

# Test Valores por defecto
rec = Rectangulo()
rec.base = 10
rec.altura = 10
assert rec.base == 10
assert rec.altura == 10
assert rec.area() == 100

# Test variables de clase
assert Rectangulo(10, 10).area() == 100
assert Rectangulo(10, 0).area() == 0
assert Rectangulo(0, 10).area() == 0

# NO MODIFICAR - FIN
