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

def restar_vector_de_vector(vector1, vector2):
    return [x - y for x, y in zip(vector1, vector2)]
