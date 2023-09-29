import pygame
from pygame.locals import *

from rt import Raytracer

from figuras import *
from lights import *
from materials import *

width = 500
height = 500
pygame.init() 

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE )
screen.set_alpha(None)


raytracer = Raytracer(screen)

raytracer.envMap = pygame.image.load("environmentMap2.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)

earthTexture = pygame.image.load("earthTextureMap.jpg")
ballTexture = pygame.image.load("basketballTextureMap.jpg")
marbleTexture = pygame.image.load("marbleTextureMap.jpg")
gemTexture = pygame.image.load("gemTexture.png")
pokeballTexture = pygame.image.load("pokeballTexture.jpg")

#OPAQUE
earth = Material(texture = earthTexture,spec = 32, ks = 0.1, matType = OPAQUE )
ball = Material(texture = pokeballTexture,spec = 64, ks = 0.2, matType = OPAQUE )

#REFLECTIVE
marble = Material(texture = marbleTexture,spec = 64, ks = 0.1, matType=REFLECTIVE )
blueMirror = Material(diffuse = (0.4,0.4,0.9), spec = 32, ks = 0.15, matType = REFLECTIVE)
#TRANSPARENT
gem = Material(texture = gemTexture, diffuse = (0.7,0.8,0.9), spec = 128, ks = 0.2, ior= 2.417, matType = TRANSPARENT)
diamond = Material(diffuse = (0.9,0.9,0.9), spec = 128, ks = 0.2, ior= 2.417, matType = TRANSPARENT)

#Opaque
raytracer.scene.append(Sphere(position=(-3,2,-8), radius = 1, material=ball))
raytracer.scene.append(Sphere(position=(-3,-1,-8), radius = 1, material=earth))

#REFLECTIVOS
raytracer.scene.append(Sphere(position=(0,2,-8), radius = 1, material=marble))
raytracer.scene.append(Sphere(position=(0,-1,-8), radius = 1, material=blueMirror))

#TRANSPARENT
raytracer.scene.append(Sphere(position=(3,2,-8), radius = 1, material=gem))
raytracer.scene.append(Sphere(position=(3,-1,-8), radius = 1, material=diamond))


brick = Material(diffuse = (1,0.4,0.4), spec = 8, ks = 0.01)
grass = Material(diffuse = (0.4,1,0.4), spec =32, ks = 0.1) 
water = Material(diffuse = (0.4,0.4,1), spec = 256, ks = 0.2 )


mirror = Material(diffuse = (0.9,0.9,0.9), spec = 64, ks = 0.2, matType = REFLECTIVE)
glass = Material(diffuse= (0.9,0.9,0.9),spec = 64, ks = 0.15, ior = 1.5, matType=TRANSPARENT)
water = Material(diffuse = (0.4,0.4,1.0), spec = 128, ks = 0.2, ior= 1.33, matType = TRANSPARENT)

#Luces
raytracer.lights.append(AmbientLight(intensity=0.1))  
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.9))  
#raytracer.lights.append(PointLight(point=(1.5, 0, -5), intensity=1, color=(1, 0, 1)))   

raytracer.rtClear()
raytracer.rtRender()

print("\nrender time", pygame.time.get_ticks()/1000, "secs")
isRunning = True
while isRunning:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
rect = pygame.Rect(0,0,width,height)   
sub = screen.subsurface(rect)
pygame.image.save(sub, "screenshot.jpg")   
    
    #raytracer.rtClear()#Borra lo que esta
    #raytracer.rtRender()# Vuelve a  dibujar
    #pygame.display.flip()

pygame.quit()