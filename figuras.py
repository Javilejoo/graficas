import mathLib as ml
import numpy as np
from math import pi, atan2, acos

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

class Plane(Shape):
  def __init__(self, position, normal, material):
    self.normal = normal / np.linalg.norm(normal)
    super().__init__(position, material)

  def ray_intersect(self, orig, dir):
    # Distancia = ((planePos - origRay) o normal) / (dirRay o normal)
    denom = np.dot(dir, self.normal)
    if abs(denom) <= 0.0001:
      return None
    num = np.dot(np.subtract(self.position,orig), self.normal)
    t = num / denom

    if t < 0:
      return None
      
    # P = O + D * t0
    P = np.add(orig, t * np.array(dir))
      
    return Intercept(distance = t,
                     point = P,
                     normal = self.normal,
                     texcoords= None,
                     obj = self)
  
class Disk(Plane):
  def __init__(self, position, normal,radius,material):
    self.radius = radius
    super().__init__(position , normal, material)

  def ray_intersect(self, orig, dir):
    planeInterect = super().ray_intersect(orig, dir)

    if planeInterect is None:
      return None
    
    contactDistance = np.subtract(planeInterect.point, self.position) #vector quiero magnitud
    contactDistance = np.linalg.norm(contactDistance)

    if contactDistance > self.radius:
      return None
    
    return Intercept(distance = planeInterect.distance,
                     point = planeInterect.point,
                     normal = self.normal,
                     texcoords= None,
                     obj = self)
  

      
