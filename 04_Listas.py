### Listas ###

'''
Una lista es una forma de estructura de datos, como su nombre lo indica esta nos permitira crear listas de datos de cualquier tipo y con ella realizar varias operaciones, desde las mas sencillas, hasta las mas complejas. Se podria tomar una lista como un "Array" o "Arreglo", ya que guardan cierto parentezco, no son lo mismo porque la lista trae operaciones un poco mas complejas. Sin embargo una lista acaba teniendo arrays pero la lista trae operadores como "Reverse", "Ordenaciones", Entre otras.
'''

#Definir y Crear una lista:
'''
Se llama la funcion "list()" para indicar que lo que queremos guardar en la variable es de tipo lista. 
Se puede guardar cualquier tipo de informacion en una lista, no hace falta seguir un mismo tipo de dato, una lista puede tener valores: numericos, de texto, decimales, entre otros.
'''

# Maneras de crear una lista

mi_lista = list(['Maria Fernanda', 18, 'Juanes', 20]) # Constructor
mi_lista2 = ['Perro', 'Gato', 'Pajaro']

print(mi_lista)
print(len(mi_lista))

print(mi_lista2)

print('----------------------------------------------------------------------------------------------------------')

#Guardar informacion en la lista:
mi_lista = ['Santy', 17, 1.75, 'Valeria', 17, 1.65, 'Santiago Arias', 21, 1.80, True, False]

print(mi_lista)
print('Cuantos valores tiene nuestra lista:', len(mi_lista))
print('Que tipo de datos es: ', type(mi_lista))

print('----------------------------------------------------------------------------------------------------------')

#Acceder a la informacion de la lista

print('El nombre de la primera persona en la lista es: ', mi_lista[0])
print('Que numero hay en esta posicion: ', mi_lista[-10])
print('¿Cuantas personas hay con la misma edad?: ', mi_lista.count(17)) # Imprimame cuantas veces hay repetido un valor.

#Que no se debe de hacer para acceder a toda la lista
#nombre, edad, altura, boolean_ = mi_lista[0], mi_lista[1]
#print(nombre)

print('----------------------------------------------------------------------------------------------------------')

#Concatenar listas

print('Resultado despues de concatenar listas: ', mi_lista + mi_lista2)

print('----------------------------------------------------------------------------------------------------------')


# Como agregar nuevos valores a nuestra lista

mi_lista.append(17) # Agrega informacion nueva a nuestra lista
print('Agregar un nuevo resultado a la lista: ', mi_lista)

mi_lista2.insert(0, 'Leon') # Insertar informacion en cierta posicion
print(mi_lista2)

# Eliminar elementos de una lista

mi_lista.remove(17) # Remover el valor de la lista madre
print('La lista queda asi despues de remover el valor 17: ', mi_lista)

milista3 = mi_lista2.pop(0)
print(milista3)
print(mi_lista2)


# Copiar una lista

milista4 = [12, 120, 100, 400, 1, 10, 0]
mi_nueva_lista = mi_lista.copy()

mi_lista.clear() # Vaciar una lista
print(mi_lista)

print(mi_nueva_lista)


print(milista4)
print(milista4[0:2])


milista4.sort() # Organizar los valores de una lista de menor a mayor
print(milista4)

milista4.reverse() # Organizar la lista de mayor a menor
print(milista4)

print('----------------------------------------------------------------------------------------------------------')

# Corregir un elemento en una lista

mi_lista2[0] = 'Daniel'
print(mi_lista2)

mi_lista2.sort()
print(mi_lista2)

mi_lista2.reverse()
print(mi_lista2)

'''
Nota: No se pueden organizar listas que contengan numeros y textos
'''

print('----------------------------------------------------------------------------------------------------------')

# Sublistas

print(milista4[0:2])
