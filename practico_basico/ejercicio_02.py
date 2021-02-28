"""Lógica Simple y Cortocircuito"""

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True
"""

esta_lloviendo = True
estan_regando = True

# COMPLETAR - INICIO
piso_mojado = esta_lloviendo or estan_regando
# COMPLETAR - FIN

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.

Restricción: Usar NOT
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
area_mayor_a_cinco = not area_cuadrado < 5
# COMPLETAR - FIN

assert area_mayor_a_cinco  


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
resultado = numero_1 % 7 == 0 and not 50 % 7 == 0
# COMPLETAR - FIN

assert resultado  


"""
Construir una expresión lógica que use TODAS las sentencias y cuyo resultado sea
el mismo valor de la sentencia 3.

Restricción: sólo usar OR y NOT
"""

sentencia_01 = False
sentencia_02 = True
sentencia_03 = 80
sentencia_04 = "90"
sentencia_05 = 100

# COMPLETAR - INICIO
resultado = sentencia_01 or not True or 80 or "90" and 100
# COMPLETAR - FIN

assert resultado == 80  

