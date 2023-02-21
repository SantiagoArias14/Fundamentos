# Encuentra una distancia euclidiana entre (2, 3) y (10, 8).
"""
La distancia euclidiana es la distancia entre 2 puntos
"""
import numpy as np

punto1 = np.array([2, 3])
punto2 = np.array([10, 8])

distancia = np.linalg.norm(punto2 - punto1)

print("La distancia euclidiana entre", punto1, "y", punto2, "es: ", distancia)
