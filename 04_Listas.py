### Listas ###

'''
Una lista es una forma de estructura de datos, como su nombre lo indica esto nos permitira crear listas de datos de cualquier tipo y con ella realizar varias operaciones, desde las mas sencillas, hasta las mas complejas. Se podria tomar una lista como un "Array" o "Arreglo", ya que guardan cierto parentesco, no son lo mismo porque la lista trae operaciones un poco mas complejas. Sin embargo una lista acaba teniendo arrays pero la lista trae operadores como "Reverse", "Ordenaciones", Entre otras.
'''

#Definir y Crear una lista:
'''
Se llama la funcion "list()" para indicar que lo que queremos guardar en la variable es de tipo lista. 
Se puede guardar cualquier tipo de informacion en una lista, no hace falta seguir un mismo tipo de dato, una lista puede tener valores: numericos, de texto, decimales, entre otros.
'''

mi_lista = list(['Maria Fernanda', 18, 'Juanes', 20]) 
mi_lista2 = ['Perro', 'Gato', 'Pajaro']

print(mi_lista)
print(len(mi_lista))

print(mi_lista2)

print('----------------------------------------------------------------------------------------------------------')

#Guardar informacion en la lista:
mi_lista = ['Santy', 17, 1.75, 'Valeria', 17, 1.65, 'Santiago Arias', 21, 1.80, True, False]

print(mi_lista)
print(len(mi_lista))
print(type(mi_lista))

print('----------------------------------------------------------------------------------------------------------')

#Acceder a la informacion de la lista

print('El nombre de la primera persona en la lista es: ', mi_lista[0])
print(mi_lista[-10])
print('¿Cuantas personas hay con la misma edad?: ', mi_lista.count(17)) # Imprimame cuantas veces hay repetido un valor.

#Que no se debe de hacer para acceder a toda la lista
#nombre, edad, altura, boolean_ = mi_lista[0], mi_lista[1]
#print(nombre)

print('----------------------------------------------------------------------------------------------------------')

#Concatenar listas

print(mi_lista + mi_lista2)
