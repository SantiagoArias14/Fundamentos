### Strings ###

'''
El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. Todos los datos entre comillas simples, dobles o triples son cadenas. Existen diferentes métodos de cadena y funciones integradas 
para manejar tipos de datos de cadena. Para verificar la longitud de una cadena, use el método len().
Ejemplos:

'''

#Definir una variable string
My_Cadena = 'Hola, Esto es un curso de Python'
print(len(My_Cadena))

print('----------------------------------------------------------------------------------------------------------')

# Definir 2 cadenas y comparar cual es mas grande
My_Cadena2 = 'Mi nombre es: Santiago Arias'
My_Cadena3 = 'Mi nombre es: Maria Fernanda'

print(len(My_Cadena2) > len(My_Cadena3))

# Comparar si son iguales de grandes
print(len(My_Cadena2) == len(My_Cadena3))

#Comparar si My_Cadena2 es menor que My_Cadena3
print(len(My_Cadena2) < len(My_Cadena3))

"""
Nota: Tambien podemos hacer operaciones con operadores logicos y cadenas, estos ejemplos no son las unicas opciones que existen.

"""

print('----------------------------------------------------------------------------------------------------------')

# Definir una variable de texto con multineas
My_Multilinea = '''Esto es un ejemplo con las cadenas en multilinea, se pueden hacer con comillas simples o comillas dobles, se deben de poner 3 veces cada una, la diferencia de las comillas dobles, es que las triples nos dejan alvergar mas informacion o texto en este caso.'''

print(My_Multilinea)

print('----------------------------------------------------------------------------------------------------------')

#Concatenar informacion de una cadena

print(My_Cadena +". "+ My_Cadena2)
print(My_Cadena + ', ' + My_Cadena3 + ' y tengo 18 años')

# Concatenar cadenas ya creadas con nuevas cadenas hechas en el print()

print(My_Cadena + ", " + My_Cadena2 + ", Sean bievenidos todos, gracias por participar." + " Hoy veremos Strings")

print('----------------------------------------------------------------------------------------------------------')

# Secuencias de escape en cadenas

'''
En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

'''

#Salto de Linea: \n
My_SaltoLinea = '''Esto es un ejemplo con el salto de linea, \nse pueden hacer con comillas simples o comillas dobles, se deben de poner 3 veces cada una, la diferencia de las comillas dobles, es que las triples nos dejan alvergar mas informacion o texto en este caso.'''

print(My_SaltoLinea)

print('----------------------------------------------------------------------------------------------------------')

#Tabulador de 8 espacios: \t
My_Tabulador = '''Esto es un ejemplo del tabulador, \tse pueden hacer con comillas simples o comillas dobles, se deben de poner 3 veces cada una, la diferencia de las comillas dobles, es que las triples nos dejan alvergar mas informacion o texto en este caso.'''

print(My_Tabulador)

print('----------------------------------------------------------------------------------------------------------')

# Barra invertida: \\
My_BarraInvertida = 'Esto es un ejemplo de la barra invertida, \\se pueden hacer con comillas simples o comillas dobles, se deben de poner 3 veces cada una, la diferencia de las comillas dobles, es que las triples nos dejan alvergar mas informacion o texto en este caso.'

print(My_BarraInvertida)

print('----------------------------------------------------------------------------------------------------------')

# Formatar de un String

# %s -> Valores de texto -> Value String
# %d -> Valores enteros 
# %f -> Valores flotantes

name, surname, age, weight = 'Santiago', 'Arias', 20, 76.5

print("Mi nombre es: "+name+ " " +surname+ " y mi edad es:", age, "años", weight, "kilos") 

print("Mi nombre es: %s %s y mi edad es %d años y peso %f kilos" %(name, surname, age, weight))
print('Yo tengo %d años y me llamo %s %s' %(age, name, surname))

print("Mi nombre es: {} {}. Mi edad es {} años y peso {} kilos".format(name, surname, age, weight))
print('Yo tengo {} años y me llamo {} {}'.format(age, name, surname))

#Inferir informacion

print(f"Mi nombre es: {name} {surname}. Mi edad es {age} años y peso {weight} kilos")
print(f"Yo tengo {age} y me llamo: {name} {surname}")

('----------------------------------------------------------------------------------------------------------')

# Descomprimir caracteres

Lenguaje = 'JavaScript'
a,b,c,d,e,f,g,h,i,j = Lenguaje

print(a,b,c,d,e,f,g,h,i,j)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

('----------------------------------------------------------------------------------------------------------')

# Dividir caracteres de una cadena

# Imprimir desde una posicion a otra
div_Lenguaje = Lenguaje [0:4]
print(div_Lenguaje)

# Imprimir desde una posicion
div_Lenguaje = Lenguaje [0:]
print(div_Lenguaje)

# Imprimir una posicion negativa
div_Lenguaje = Lenguaje [-1]
print(div_Lenguaje)

# Darle reversa a la cadena
reverse_Lenguaje = Lenguaje [::-1]
print(reverse_Lenguaje)

# Evitar caracteres
evit_Lenguaje = Lenguaje [0:5:2]
print(evit_Lenguaje)

print('----------------------------------------------------------------------------------------------------------')

# Metodos para Cadenas

print(Lenguaje.capitalize()) # Esto imprime el valor de la cadena en mayuscula
print(Lenguaje.upper()) # Imprime la variable de cadena en mayuscula
print(Lenguaje.count("J")) # Imprime cuantos valores hay repetidos en la variable
print(Lenguaje.isnumeric()) # Imprime si la variable es un numero o no
print('numero'.isnumeric()) 
print(Lenguaje.lower()) # Imprime la variable en minusculas
