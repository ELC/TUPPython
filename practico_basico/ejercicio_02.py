"""Lógica Simple y Cortocircuito"""


"""
Determinar el valor booleano de la siguiente sentencia:
"""

sentencia_01 = False and True or True

#Comentar la linea con el resultado incorrecto
resultado_01 = True
#resultado_01 = False

assert sentencia_01 == resultado_01


"""
Determinar el valor booleano de la siguiente sentencia:
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado - 3, 2)

sentencia_02 = not area_cuadrado < 5

#Comentar la linea con el resultado incorrecto
#resultado_02 = True
resultado_02 = False

assert sentencia_02 == resultado_02


"""
Determinar el valor booleano de la siguiente sentencia:
"""

sentencia_03 = 49 % 7 == 0 and not 50 % 7 == 0

#Comentar la linea con el resultado incorrecto
resultado_03 = True
#resultado_03 = False

assert sentencia_03 == resultado_03


"""
Determinar el valor de la siguiente sentencia:
"""

sentencia_04 = False or not True or 80 or "90" or 100

#Comentar las lineas con resultado incorrecto
#resultado_04 = True
#resultado_04 = False
resultado_04 = 80
#resultado_04 = "90"
#resultado_04 = 100

assert sentencia_04 == resultado_04


"""
Determinar el valor de la siguiente sentencia:
"""

sentencia_04 = 80 and False and "90" and 100

#Comentar las lineas con resultado incorrecto
#resultado_04 = True
resultado_04 = False
#resultado_04 = 80
#resultado_04 = "90"

assert sentencia_04 == resultado_04