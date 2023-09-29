
import mathLib as ml
from math import tan, pi, atan2, acos

class Intercept(object):
  def __init__(self,distance, point, normal,texcoords, obj):
    self.distance = distance
    self.point = point
    self.normal = normal
    self.texcoords = texcoords
    self.obj = obj

class Shape(object):
  def __init__(self, position, material):
    self.position = position
    self.material = material

  def ray_intersect(self, orig, dir):
    return None
  

class Sphere(Shape):
  def __init__(self, position, radius, material):
    self.radius = radius
    super().__init__(position,material)
  
  def ray_intersect(self, orig, dir):
    L = ml.restar_vector_de_vector(self.position, orig)
    lengthL = ml.norma_linalg(L)
    tca = ml.producto_punto(L, dir)
    d = (lengthL**2 - tca**2)**0.5

    if d > self.radius:
      return None
    
    thc = (self.radius**2 - d**2)**0.5

    t0 = tca - thc
    t1 = tca + thc

    if t0 < 0:
      t0 = t1
    
    if t0 < 0:
      return None
    
    P = ml.sumar_vectores(orig, ml.multiplicar_vector_por_escalar(dir, t0))
    normal = ml.restar_vector_de_vector(P,self.position)
    normal_norm = ml.norma_linalg(normal)
    if normal_norm != 0:
      normal = ml.multiplicar_vector_por_escalar(normal, 1 / normal_norm)

    u = (atan2(normal[2], normal[0]) / (2 * pi)) + 0.5
    v = acos(normal[1]) / pi
    return Intercept(distance = t0,
                     point = P,
                     normal = normal,
                     texcoords=(u,v),
                     obj = self)