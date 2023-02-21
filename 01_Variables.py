
#                                               Variables


"""
    Las variables almacenan datos en la memoria de una computadora. Se recomienda el uso de variables mnemotécnicas en muchos lenguajes de programación. Una variable mnemotécnica es un nombre de variable que se puede recordar y asociar fácilmente. Una variable se refiere a una dirección de memoria en la que se almacenan los datos. Número al principio, carácter especial, guión no están permitidos al nombrar una variable. Una variable puede tener un nombre corto (como x, y, z), pero se recomienda enfáticamente un nombre más descriptivo (nombre, apellido, edad, país).


    Reglas de nombres de variables de Python:

        Un nombre de variable debe comenzar con una letra o el carácter de subrayado.
        Un nombre de variable no puede comenzar con un número.
        Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _).
        Los nombres de las variables distinguen entre mayúsculas y minúsculas (nombre, Nombre, PrimerNombre y NOMBRE) son variables diferentes).

"""

#Ejemplo de Variables nombradas bien:
 
firstname = 'Nombre'
lastname = 'Apellido'
age =  'Edad'
country = 'Pais'
city = 'Ciudad'
first_name = 'primer_nombre'
last_name = 'apellidos'
capital_city = 'Capital_ciudad'
_if = 'Lenguaje_reservado'
year2023 = 'Año_2022'
year_2023 = 'Año_2023'
current_year_2023 = 'Estamos_En_2023'
birth_year = 'Fecha_de_Cumpleaños'
#num1 = 'Numero1'
#num2 = 'Numero2'
#num3 = ''

#Ejemplo de como no nombrar una variable:

#first-name = ''
#first@name = ''
#first$name = ''
#num-1 = ''
#1num = ''

#Ejemplo de como se debe hacer y uso de la funcion len()

first_name = 'Santiago Arias'
First_name = 'Santiago'

print(first_name)
print(First_name)

print(len(first_name))
print("La cantidad de caracteres son: ", len(first_name))



last_name = 'Arias Aguirre'
Last_name = 'Arias Aguirre'

print(last_name)
print(Last_name)

print(len(last_name))
print("La cantidad de caracteres son: ", len(last_name))



country = 'Colombia'
Country = 'Colombia'

print(country)
print(Country)

print(len(country))
print("La cantidad de caracteres son: ", len(country))

print('-------------------------------------------------------------------------------------------------------')

#Declar varias variables en una sola linea

Nombre, Apellido, Pais, Edad, Casado = 30, 'Arias', 'Colombia', 20, False

print(Nombre, Apellido, Pais, Edad, Casado)

print(Nombre)
print(Apellido)
print(Pais)
print(Edad)
print(Casado)

print('-------------------------------------------------------------------------------------------------------')

#Ejemplo con nombre y edad + como pedir datos al usuario por consola:

nombre = input("¿Como te llamas: ")
edad = input("¿Cual es tu edad?: ")

num1 = int(input("Ingrese el valor a sumar: "))
num2 = int(input("Ingrese el valor a sumar: "))

num3 = num1 + num2

print("La suma es: ", num1 + num2)



print('-------------------------------------------------------------------------------------------------------')

# Conversion de datos
 
''' Pasar de int a float '''
num_ent = 10

num_float = float(num_ent) 
print(num_float)

print(int(num_float))

print("El valor convertido a decimal es: ", float(num_ent))

''' Pasar de float a int '''

gravedad = 9.81

intg = int(gravedad)
print(intg)

print(int(gravedad))

print("El valor convertido a entero es: ", int(gravedad))

''' Pasar de int a str '''

num_int = 11

num_str = str(num_int) #--> '11' --> eleven
print(num_str)

''' Pasar de str a int o float '''

str1 = '10'

print("El numero entero es: ", int(str1)) #--> '10' --> 10

print("El numero flotante es: ", float(str1))#--> '10' --> 10.0

''' Pasar de str a list '''

Mi_Nombre = 'Daniela'

list_Mi_Nombre = list(Mi_Nombre)
print(list_Mi_Nombre)

''' Ejercicios '''

# 1.

"""
#- Calcule el área de un círculo y asigne el valor a una variable llamada area_del_circulo.
#- Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circunferencia.
#- Tome el radio como entrada del usuario y calcule el área.
"""

#Area de un circulo

pi = 3.1416
radio = (int(input("Deme el valor del radio: ")))
flotradio = float(radio)

a = pi * flotradio**2

print("El valor del radio en decimal es: ", flotradio)
print("El area del circulo es: ", a)


# Circunferencia


radioc = (int(input("Deme el valor del radio: ")))

circunferencia = 2*pi*radioc

print("El valor de la circunferencia es: ", circunferencia)

#Pedir informacion al usuario


pi = 3.1416
radio = (int(input("Ingrese el valor de el radio: ")))

a = pi*radio**2

print("El area del circulo es: ", a)

#Encontrar el area de un cuadrado y triangulo


lado = int(input("Ingrese el valor de un lado: "))

ar = lado*2

print("El area del cuadrado es: ", ar)