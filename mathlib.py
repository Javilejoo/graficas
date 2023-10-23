import math

def normalizar(vector):
    normal = math.sqrt(sum([x * x for x in vector]))
    return [x / normal for x in vector]

def producto_punto(vector1, vector2):
    return sum([x * y for x, y in zip(vector1, vector2)])

def restar_vectores(vector1, vector2):
    return [x - y for x, y in zip(vector1, vector2)]

def norma_linalg(vector):
    return math.sqrt(sum([x * x for x in vector]))

def sumar_vectores(vector1, vector2):
    return [x + y for x, y in zip(vector1, vector2)]

def multiplicar_vector_por_escalar(vector, escalar):
    return [x * escalar for x in vector]

def multiplicar_vectores(vector1, vector2):
    return [x * y for x, y in zip(vector1, vector2)]

def producto_vectorial(vector1, vector2):
    x = vector1[1] * vector2[2] - vector1[2] * vector2[1]
    y = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    return [x, y, z]






