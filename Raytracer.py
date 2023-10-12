import pygame
from pygame.locals import *

from rt import Raytracer

from figuras import *
from lights import *
from materials import *

width = 500
height =500
pygame.init() 

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE  )
screen.set_alpha(None)


raytracer = Raytracer(screen)

raytracer.envMap = pygame.image.load("environmentMap.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)
pyramid = pygame.image.load("pyramidTexture.jpg")
diamondCube =pygame.image.load("diamond_block.png")
goldCube =pygame.image.load("gold_block.png")

blueMirror = Material(diffuse = (0.4,0.4,0.9), spec = 32, ks = 0.15, matType = REFLECTIVE)
#TRANSPARENT MATS
diamond = Material(diffuse = (0.9,0.9,0.9), spec = 128, ks = 0.2, ior= 2.417, matType = TRANSPARENT)
brick = Material(diffuse = (1,0.4,0.4), spec = 8, ks = 0.01)
grass = Material(diffuse = (0.4,1,0.4), spec =32, ks = 0.1) 
water = Material(diffuse = (0.4,0.4,1), spec = 256, ks = 0.2 )


mirror = Material(diffuse = (0.9,0.9,0.9), spec = 64, ks = 0.2, matType = REFLECTIVE)
glass = Material(diffuse= (0.9,0.9,0.9),spec = 64, ks = 0.15, ior = 1.5, matType=TRANSPARENT)
water = Material(diffuse = (0.4,0.4,1.0), spec = 128, ks = 0.2, ior= 1.33, matType = TRANSPARENT)
goldMinecraft = Material(texture = goldCube,spec = 24, ks = 0.1, matType=OPAQUE)
diamondMinecraft = Material(texture = goldCube,spec = 24, ks = 0.1, matType=OPAQUE)

pyramid_materialO= Material(texture=pyramid, spec=32, ks=0.1, matType=OPAQUE)
pyramid_materialT = Material(texture=pyramid, spec=32, ks=0.1, matType=TRANSPARENT)
pyramid_materialR = Material(texture=pyramid, spec=32, ks=0.1, matType=REFLECTIVE)

# Crear una piramide
piramide1 = Pyramid(position=(1.5, -1, -4), size=2.5, material=pyramid_materialR)
piramide2 = Pyramid(position=(-1.5, -1, -4), size=1.8, material=pyramid_materialT)
piramide3 = Pyramid(position=(0, -1, -4.2), size=1.2, material=mirror)
piramide4 = Pyramid(position=(1, -1, -2), size=0.5, material=pyramid_materialO)  
piramide5 = Pyramid(position=(-1, -1, -2), size=0.5, material=pyramid_materialO)  
piramide6 = Pyramid(position=(0, -1, -2), size=0.5, material=pyramid_materialO)  

Cubo = AABB(position=(0,1 , -2), size=(0.2, 0.2, 0.2), material=goldMinecraft)
Cubo2 = AABB(position=(-1.5,-1 , -6), size=(0.2, 0.2, 0.2), material=diamondMinecraft)


# Agregar la piramida la escena
raytracer.scene.append(piramide1)
raytracer.scene.append(piramide2)
raytracer.scene.append(piramide3)
raytracer.scene.append(piramide4)
raytracer.scene.append(piramide5)
raytracer.scene.append(piramide6)
raytracer.scene.append(Cubo)
raytracer.scene.append(Cubo2)


#Luces
#raytracer.lights.append(AmbientLight(intensity=0.1))  
#raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.9))  
#raytracer.lights.append(PointLight(point=(1.5, 0, -5), intensity=1, color=(1, 0, 1)))   
# Luces
ambient_light = AmbientLight(intensity=0.3, color=(1, 0.8, 0.6))  # Luz ambiental suave
directional_light = DirectionalLight(direction=(1, -1, -1), intensity=1.0, color=(1, 0.9, 0.8))  # Luz direccional principal
point_light = PointLight(point=(2, 2, 2), intensity=1.0, color=(1, 1, 1))  # Luz puntual (ajusta la posición según sea necesario)

# Agregar las luces a la escena
raytracer.lights.append(ambient_light)
raytracer.lights.append(directional_light)
raytracer.lights.append(point_light)

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