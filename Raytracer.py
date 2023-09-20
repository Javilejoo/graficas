import pygame
from pygame.locals import *

from rt import Raytracer
from figuras import *
from lights import *
from materials import *

width = 256
height = 256
pygame.init() 

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25,0.25,0.25)

""" brick = Material(diffuse = (1,0.4,0.4), spec = 8, ks = 0.01)
grass = Material(diffuse = (0.4,1,0.4), spec =32, ks = 0.1) 
water = Material(diffuse = (0.4,0.4,1), spec = 256, ks = 0.2 ) """
snow = Material(diffuse= (1,1,1), spec= 0.2, ks = 0.1)
rock = Material(diffuse=(0,0,0), spec = 3, ks = 0.1)
carot = Material(diffuse=(1,0.5,0), spec = 0.5, ks = 0.3)
eyes = Material(diffuse= (0.9,0.9,0.9), spec= 0.4, ks = 0.1)

#Cuerpo
raytracer.scene.append(Sphere(position = (0,-2,-9), radius=2, material = snow))
raytracer.scene.append(Sphere(position = (0,-1.5,-7.2), radius=0.3, material = rock))

#mitad
raytracer.scene.append(Sphere(position = (0,1,-9), radius=1.5, material = snow))
raytracer.scene.append(Sphere(position = (0,0,-8), radius=0.3, material = rock))
raytracer.scene.append(Sphere(position = (0,1.5,-7.7), radius=0.3, material = rock))

#Cabeza
raytracer.scene.append(Sphere(position = (0,3.4,-9), radius=1, material = snow))
raytracer.scene.append(Sphere(position = (0,2.9,-7.7), radius=0.3, material = carot))
raytracer.scene.append(Sphere(position = (-0.4,3.2,-7.7), radius=0.25, material = eyes))
raytracer.scene.append(Sphere(position = (0.4,3.2,-7.7), radius=0.25, material = eyes))
raytracer.scene.append(Sphere(position = (-0.4,3.2,-7.5), radius=0.1, material = rock))
raytracer.scene.append(Sphere(position = (0.4,3.2,-7.5), radius=0.1, material = rock))
raytracer.scene.append(Sphere(position = (0,2.2,-7.7), radius=0.1, material = rock))
raytracer.scene.append(Sphere(position = (0.5,2.4,-7.7), radius=0.1, material = rock))
raytracer.scene.append(Sphere(position = (-0.5,2.4,-7.7), radius=0.1, material = rock))

#Luces
raytracer.lights.append(AmbientLight(intensity=0.2, color=(1, 1, 1)))  
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.8, color=(1, 1, 1)))  
raytracer.lights.append(PointLight(point=(0, 0, -5), intensity=0.5, color=(1, 1, 1)))  

isRunning = True
while isRunning:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False      
    
    raytracer.rtClear()#Borra lo que esta
    raytracer.rtRender()# Vuelve a  dibujar
    pygame.display.flip()

pygame.quit()