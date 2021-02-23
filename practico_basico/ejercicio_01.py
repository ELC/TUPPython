"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5
area_cuadrado = lado_cuadrado * lado_cuadrado  # Completar

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia
"""

lado_cuadrado = 5
area_cuadrado = lado_cuadrado ** 2  # Completar

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)  # Completar

assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar
Restricción: Usar el operador de división entera
"""

precio = 3.74
presupuesto_disponible = 10
cantidad_a_comprar = presupuesto_disponible // precio  # Completar

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7
Restricción: Usar el operador módulo
"""

numero_incalculable = 2 ** 54 - 1
es_divisible_por_siete = numero_incalculable % 7 == 0  # Completar

assert es_divisible_por_siete
