import numpy as np




# 1.Calcule la pendiente, la intersección x y la intersección y de y = 2x -2

"""
La ecuación de la línea recta y = mx + b se puede expresar como y = pendiente * x + intersección_y. En la ecuación y = 2x - 2, la pendiente es 2 y la intersección y es -2. Para encontrar la intersección x, podemos despejar x de la ecuación, lo que resulta en x = (y + 2) / 2.
"""

pendiente = 2
interseccion_y = -2

# Calcula la intersección x para y = 0
interseccion_x = -interseccion_y / pendiente

print("La pendiente es:", pendiente)
print("La intersección x es:", interseccion_x)
print("La intersección y es:", interseccion_y)


# 2.Escriba un script que solicite al usuario que ingrese el número de años. Calcular el número de segundos que puede vivir una persona. Supongamos que una persona puede vivir cien años.

# Solicitar al usuario que ingrese el número de años
num_años = int(input("Ingrese el número de años que desea calcular: "))

# Calcular el número de segundos que puede vivir una persona
segundos_por_años = 365 * 24 * 60 * 60
segundos_de_vida = num_años * segundos_por_años
segundos_maximos_de_vida = 100 * segundos_por_años
segundos_restantes_de_vida = segundos_maximos_de_vida - segundos_de_vida

# Imprimir el resultado
print("Una persona puede vivir", segundos_de_vida, "segundos en", num_años, "años.")
print("Suponiendo que una persona puede vivir cien años, le quedan", segundos_restantes_de_vida, "segundos de vida.")

# 3. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?

# Solicitar al usuario las horas y la tarifa por hora
horas = float(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

# Calcular el salario
salario = horas * tarifa

# Imprimir el salario
print("El salario de la persona es: ", salario)