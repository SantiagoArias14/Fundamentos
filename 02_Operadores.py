"""
Boolean:

    Un tipo de datos booleano representa uno de los dos valores: True o False . El uso de estos tipos de datos quedará claro una vez que comencemos a usar el operador de comparación. La primera letra T para Verdadero y F para Falso debe ser mayúscula.

"""

#Ejemplo

print(True) #Con la funcion type (Vemos el tipo de dato que hay en el print).
print(False)

"-----------------------------------------------------------------------------------------------------------------"

"""
Operadores de asignacion:

    Los operadores de asignación se utilizan para asignar valores a las variables. Tomemos "=" como ejemplo. 
    El signo igual en matemáticas muestra que dos valores son iguales, sin embargo, en Python significa que estamos almacenando un valor en una determinada variable y lo llamamos asignación o asignación de valor a una variable.

"""

"-----------------------------------------------------------------------------------------------------------------"

"""
Operadores aritmeticos:

# Suma (+) => a + b
# Resta(-) => a - b
# Multiplicación(*) => a * b
# División(/) => a / b
# Módulo (%) => a % b
# División de piso(//) => a // b
# Exponencial(**) => a ** b

"""

#Ejemplo:

print('La suma es: ', 1 + 2)

print('La resta es: ', 2 - 1)

print('La multiplicacion es: ', 2 * 3)

print ('La division es: ', 4 / 2)       
print('La division es: ', 6 / 2)     
print('La division es: ', 7 / 2)

print('Division de piso: ', 7 // 2) #Sirve para hacer una division y que nos de un aproximado en numero entero.
print ('Division de piso: ', 7 // 3)

print('Modulo: ', 20 % 8) 

print('Exponencial: ', 2 ** 3)


"-----------------------------------------------------------------------------------------------------------------"

# Ejemplo con numeros:

Num1 = 77
Num2 = 88

#Suma:
Sum = Num1 + Num2
print('La suma es: ', Sum)

#Resta:
diff = Num1 - Num2
print('La resta es: ', diff)

#Multiplicacion:
Multi = Num1 * Num2
print('La multiplicacion es: ', Multi)

#Division:
Div = Num1 / Num2
print('La division es: ', Div)

#Modulo:
Mod = Num1 % Num2
print('El modulo es: ', Mod)

#Division de piso:
DivF = Num1 // Num2
print('Resultado de piso es: ', DivF) 

#Exponenciacion:
Expo = Num1**Num2
print('Exponente es: ', Expo)

"-----------------------------------------------------------------------------------------------------------------"

# Calcular del area de un circulo, rectangulo y triangulo. Teniendo la siguiente informacion:

# Radio del circulo = 10

radio = 10

print('El area del circulo es: ', 3,1416*radio**2)


# Largo del rectangulo = 10 y el ancho = 20
# Calcular el peso de un objeto, teniendo en cuenta: Masa = 75 y la gravedad de la tierra.
# Calcular la densidad de un liquido teniendo en cuenta: Masa = 75 y el Volumen = 0.075.

"-----------------------------------------------------------------------------------------------------------------"

"""
Operadores de comparacion:

    En programación comparamos valores, usamos operadores de comparación para comparar dos valores. Comprobamos si un valor es mayor o menor o igual a otro valor.

"""

#Ejemplos:

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 3) # Si ambos operandos son iguales devuelve True.
print(3 != 3) # Si los operandos no son iguales, da como resultado True.

#Comparar cantidad de letras con funcion "len()" y boolean:

print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('Leche') != len('Carne'))
print(len('Leche') == len('Carne'))
print(len('tomate') == len('patata'))
print(len('python') > len('dragon'))

#Comparacion de boolean:

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True == False: ', False == True)

"-----------------------------------------------------------------------------------------------------------------"

"""
Operadores logicos:
    A diferencia de otros lenguajes de programación, Python usa palabras clave "and" , "or" y "not" para los operadores lógicos. Los operadores lógicos se utilizan para combinar sentencias condicionales

"""
# Ejemplo:

# and:
print(3 > 2 and 4 > 3) 
print(3 > 2 and 4 < 3)
print(3 < 2 and 4 < 3)
print('True and True: ', True and True)

# or:
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
print('True or False:', True or False)

# not:
print(not 3 > 2)
print(not True)
print(not False)
print(not not True)
print(not not False)

"-----------------------------------------------------------------------------------------------------------------"

# Ejercicios:                                                          Nota: Nombre = str('Santiago')

# 1. Declarar una variable que almacene su nombre.
# 2. Declarar una variable con su altura.
# 3. Escriba un codigo que solicite al usuario la base y la altura de un triangulo y calcule el area de este.
# 4. Escriba un codigo que solicite al usuario lado a, lado b y lado c de un triangulo y calcule el perimetro de este.
# 5. Calcule el area y perimetro de un rectangulo.
# 6. Calcule el radio de un circulo.

nombre = str('Valeria')
altura = float(1.80)


Base = int(input('Ingresar el valor de la base del triangulo: '))
Altura = int(input('Ingresar el valor de la altura del triangulo: '))

#Area

Area = Base * Altura / 2

print('El area del triangulo es: ', Area)


