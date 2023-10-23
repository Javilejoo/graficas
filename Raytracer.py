import pygame
from pygame.locals import *

from rt import Raytracer

from figuras import *
from lights import *
from materials import *

width = 500
height =500
pygame.init() 

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE )
screen.set_alpha(None)


raytracer = Raytracer(screen)

raytracer.envMap = pygame.image.load("environmentmap.jpeg")
solTexture = pygame.image.load("sol.jpg")
mercurioTexture = pygame.image.load("mercurio.jpg")
venusTexture = pygame.image.load("venus.jpg")
jupiterTexture = pygame.image.load("jupiter.jpg")
saturnoTexture = pygame.image.load("saturno.jpg")
uranoTexture = pygame.image.load("urano.jpg")
piramideTexture = pygame.image.load("pyramidTexture.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)



brick = Material(diffuse = (1,0.4,0.4), spec = 8, ks = 0.01)
grass = Material(diffuse = (0.4,1,0.4), spec =32, ks = 0.1) 
glass = Material(diffuse= (0.9,0.9,0.9),spec = 64, ks = 0.15, ior = 1.5, matType=TRANSPARENT)
water = Material(diffuse = (0.4,0.4,1.0), spec = 128, ks = 0.2, ior= 1.33, matType = TRANSPARENT)  

sol_material = Material(texture=solTexture,diffuse=(1.0, 0.8, 0.2), spec=100, ks=0.4, matType=OPAQUE)
mercurio_material = Material(texture=mercurioTexture,diffuse=(0.7, 0.7, 0.7), spec=80, ks=0.3, matType=OPAQUE)
venus_material = Material(texture=venusTexture, diffuse=(0.8, 0.2, 0.1), spec=60, ks=0.2, matType=REFLECTIVE)
jupiter_material = Material(texture=jupiterTexture, diffuse=(0.7, 0.5, 0.3), spec=40, ks=0.2, matType=OPAQUE)
saturno_material = Material(texture=saturnoTexture, diffuse=(0.9, 0.7, 0.4), spec=30, ks=0.1, matType=OPAQUE)
urano_material = Material(texture=uranoTexture, diffuse=(0.4, 0.6, 0.8), spec=32, ks=0.15, matType=REFLECTIVE)
piramide_material = Material(texture=piramideTexture, spec=60, ks=0.2, matType=OPAQUE)


#Planetas
# Crea las esferas para los planetas
raytracer.scene.append(Sphere(position=(0, 3, -12), radius=2, material=sol_material))  # El Sol
raytracer.scene.append(Sphere(position=(1, 3, -10), radius=0.38, material=mercurio_material))  # Mercurio
raytracer.scene.append(Sphere(position=(4.3, 0, -10), radius=0.65, material=venus_material))  # Venus
raytracer.scene.append(Sphere(position=(5, 5, -13), radius=1.99, material=jupiter_material))  # Júpiter
raytracer.scene.append(Sphere(position=(-7, 2, -17), radius=1.90, material=saturno_material))   # Saturno
raytracer.scene.append(Sphere(position=(-7, 6, -25), radius=1.90, material=urano_material)) # Urano


#Piramides
raytracer.scene.append(Pyramid(position=(0, -1, -4), size=2, material=glass))
raytracer.scene.append(Pyramid(position=(-1.7, -1, -4), size=1.5, material=piramide_material))
raytracer.scene.append( Pyramid(position=(1.7, -1, -4), size=1, material=piramide_material))  
#cilindros
raytracer.scene.append( Cylinder(position = (0,-1,-2),radius=0.2, height=0.2, material=water))
raytracer.scene.append( Cylinder(position = (1,-1,-2),radius=0.2, height=0.3, material=brick))
raytracer.scene.append( Cylinder(position = (-1,-1,-2),radius=0.2, height=0.3, material=grass))


# Luces
ambient_light = AmbientLight(intensity=0.7, color=(1, 0.8, 0.8))  # Luz ambiental suave
directional_light = DirectionalLight(direction=(1, 1, -3), intensity=1.0, color=(1, 1, 1))  # Luz direccional principal
#directional_light = DirectionalLight(direction=(-1, 1, -2), intensity=1.0, color=(0.6, 0.2, 0.4)) 
point_light = PointLight(point=(-1, 1, -1), intensity=1.0, color=(0.5,0.5,0.5))  # Luz puntual 
point_light = PointLight(point=(1.7, -1, -2), intensity=0.6, color=(0.7,0.2,0.8))  # Luz puntual 
# Agregar las luces a la escena
raytracer.lights.append(ambient_light)
raytracer.lights.append(directional_light)
raytracer.lights.append(point_light)

raytracer.rtClear()
raytracer.rtRender()

print("\nrenderTime", pygame.time.get_ticks()/1000, "secs")
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

pygame.quit()