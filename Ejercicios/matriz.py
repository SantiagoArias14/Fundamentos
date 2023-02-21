import numpy as np 


# Definir las dos matrices a sumar
MatrizA = [[-3, 4, 5], [0, 1, -8], [7, 10, -6]]
MatrizB = [[1/3, 0, -1], [0, -6, 3/5], [1, 1, 1]]

# Sumar las dos matrices utilizando la función np.add(), para la resta es np.substract()

resultado = np.add(MatrizA, MatrizB)
resultadorest = np.subtract(MatrizA, MatrizB)

# Imprimir la matriz resultado
print(resultado)
print(resultadorest)



