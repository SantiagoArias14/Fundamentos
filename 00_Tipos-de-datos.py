#                                      ¿Como podemos hacer comentarios en el codigo?

# Podemos hacer comentarios de una linea con "#"

"""
Comentarios de varias lineas. Se utilizan 3 comillas dobles seguidas.
"""

'''
Esto sigue siendo un comentario de varias lineas. Se utilizan 3 comillas sencillas seguidas.                        

"editor.wordWrap": "wordWrapColumn",
"editor.wrappingIndent": "same",
"editor.wordWrapColumn": 100,
'''                                                                                                                                                                                     


#                                           Tipos de datos en Python


# Int = Enteros
# Str = Cadena o Texto
# Float = Decimales
# Bool = booleanos "True" y "False"


#Numeros Enteros:

'''
Los numeros enteros son aquellos que son negativos o positivos y no tienen decimales.
Ejemplo:
-3, -2, -1, 0, 1, 2, 3.
'''

#Ejemplo Practicos:
en = -12 #Guardamos el valor en la variable
en2 = 13
en3 = 20.59

#Imprimir que valor y que tipo de dato son la variable 'en' y la variable 'en2':
print("El valor de la variable 'en' es: ", en)
print(type(en))

print("El valor de la variable 'en2' es: ", en2)
print(type(en2))

#Sumar e imprimir que tipo de dato es la variable ent3:
ent3 = en + en2 + en3

print("El valor de la suma es: ", ent3)
print(type(ent3))

print("El valor de la suma es: ", en + en2 + en3)
print(type(en+en2+en3))

#Convertir un decimal a un entero
en4 = en + en2 + en3
fl4 = 111.111

x = int(en4) #Int lo multiplica en base 10 para volverlo un valor entero.
print("El valor despues de convertir un valor decimal a un entero es: ", x)

v = int(fl4)
print("El valor despues de convertir un valor decimal a un entero es: ", v)

'-----------------------------------------------------------------------------------------------------------------'

#Numero Float:
'''
Son aquellos numeros que tienen valores decimales.
Ejemplo:
-3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 
'''

#Ejemplo practico:
fl1 = 43.89
fl2 = 14.99

#Imprimir que valor y que tipo de dato son las variables fl1 y fl2:
print("El valor de la variable 'fl1' es: ", fl1)
print(type(fl1))

print("El valor de la variable 'fl2' es: ", fl2)
print(type(fl2))

#Sumar las variables y decir de que tipo son:
fl3 = fl1 + fl2

print("El valor de la suma es: ", fl3)
print(type(fl3))

print("El valor de la suma es: ", fl1 + fl2)
print(type(fl1+fl2))

"""
#Nota: Recordar que existen otros operadores, tales como;

#> Resta : "-".
#> Suma : "+".
#> Division : "/".
#> Multiplicacion : "*".
#> Exponencial : "**".
#> Modulo : "%".
"""

'-----------------------------------------------------------------------------------------------------------------'

#Datos String:
'''
Es todo aquello que represente texto, nombre, apellido, entre otros.
Ejemplo:
'Santiago', 'Arias', 'Manzana', 'Gato', '20'.
'''

#Ejemplo Practico:

cadena1 = 'Hola Mundo'

'Esto es una cadena de texto'
'12334' #Sigue siendo una cadena aunque tenga numeros, ya que esta encerrado por comilas.

print("Esto es una cadena o string")

#Que tipo de dato es:
print("Que hay dentro de la cadena: ", cadena1)
print(type('Tipo de dato')) 

'-----------------------------------------------------------------------------------------------------------------'

#Datos Boolean:
'''
Son valores que representan valores Verdaderos o Falsos. Siempre se escriben con mayusculas 
"True" o "False"
'''

#Ejemplos Practicos:

print(bool(20>22)) # 20 es mayor que 22
print(20>22)

print(bool(22<=22)) # 22 es menor o igual a 22
print(22<=22)

print(bool(30==9)) # 30 es igual a 9 "=" "=="
print(30==9)

#Que tipo de dato es:

print(type(True))


#Ejemplo con operadores logicos:

#and: El resultado es True solamente si 'a' es True y 'b' es True de lo contrario el resultado es False.
#or: El resultado es True si 'a' es True o 'b' es True de lo contrario el resultado es False.
#not: El resultado es True si 'a' es False de lo contrario el resultado es False.

a = 50
b = 70
c = 90

#Ejercicio con and:

d = a < b and b > a and c > b and b < c and (c == a)
print("El resultado es :", d)

#Ejercicio con or:

e = c == c or b >= c and a > c or a > b or c < a
print("El resultado es :", e)

#Ejercicio con not:

f = not (a < b) # Lo que es falso lo convierte en verdadero y lo que es verdadero lo vuelve falso
print(" El resultado es: ", f)

'-----------------------------------------------------------------------------------------------------------------'

"""
#Ejercicios para realizar:

#1. Realizar las siguientes operaciones con 2 numeros o mas.

#- Suma (+)
#- Sustracción(-)
#- Multiplicación(*)
#- Módulo(%)
#- División(/)

#2. Imprimir strings que tengan su nombre, apellido, años, donde vive y donde estudia. 

#3. Comprobar que tipo de datos son los siguientes:
#- 10
#- 9.8
#- 3.14
#- 3 < 1 == 4 < 2 >= 0 <= 10 
#- 'Python en Vs para Data Analitica'
"""

# Modulo

# Variables a Utilizar

Mdl1, Mdl2, Mdl3 = 2000, 1000, 10000


# Operaciones

Rmdl = Mdl1 % Mdl2 % Mdl3

#Prints

print("El modulo es: ", Rmdl)

