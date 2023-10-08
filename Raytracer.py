import pygame
from pygame.locals import *

from rt import Raytracer

from figuras import *
from lights import *
from materials import *

width = 100
height = 100
pygame.init() 

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE  )
screen.set_alpha(None)


raytracer = Raytracer(screen)

raytracer.envMap = pygame.image.load("environmentMap.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)




diamondCube =pygame.image.load("diamond_block.png")
ironCube =pygame.image.load("iron_block.png")
glowstoneCube =pygame.image.load("glowstone.png")
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



# Materiales para las paredes
ceiling_material = Material(diffuse=(1.0, 0.9, 0.2), spec=64, ks=0.2)  # Amarillo brillante
floor_material = Material(diffuse=(0.95, 0.8, 0.7), spec=64, ks=0.2)    # Rosa pastel
back_wall_material = Material(diffuse=(0.4, 0.7, 0.95), spec=64, ks=0.2)  # Azul brillante
left_wall_material = Material(diffuse=(1.0, 0.4, 0.6), spec=64, ks=0.2)  # Rojo brillante
right_wall_material = Material(diffuse=(0.6, 1.0, 0.5), spec=64, ks=0.2)  # Verde brillante
diamondMinecraft = Material(texture = diamondCube,spec = 24, ks = 0.1, matType=OPAQUE)
ironMinecraft = Material(texture = ironCube,spec = 24, ks = 0.1, matType=OPAQUE)
goldMinecraft = Material(texture = goldCube,spec = 24, ks = 0.1, matType=OPAQUE)
glowstoneMinecraft = Material(texture = glowstoneCube,spec = 24, ks = 0.1, matType=REFLECTIVE)


# Crear los planos que forman las paredes del cuarto con los materiales respectivos
ceiling = Plane(position=(0, 5, 0), normal=(0, 1, 0.2), material=ceiling_material)
floor = Plane(position=(0, -2, 0), normal=(0, 1, -0.2), material=floor_material)
back_wall = Plane(position=(0, 0, 5), normal=(0, 0, 1), material=back_wall_material)
left_wall = Plane(position=(-4, 0, 0), normal=(1, 0, -0.2), material=left_wall_material)
right_wall = Plane(position=(4, 0, 0), normal=(1, 0, 0.2), material=right_wall_material)


Diskk = Disk(position=(-2, 0, -5), normal=(1, 0, 0.2), radius=1, material=mirror)
Diskk1 = Disk(position=(2, 0, -5), normal=(1, 0, -0.2), radius=1, material=mirror)
Diskk2 = Disk(position=(0, 0, -7), normal=(0, 0, 1), radius=1, material=mirror)
Diskk3 = Disk(position=(0, 4, 0), normal=(0, -1, 0), radius=1, material=mirror)
Cubo1 = AABB(position=(1, -1, -4), size=(1, 1, 1), material=ironMinecraft)
Cubo2 = AABB(position=(-1, -1, -4), size=(1, 1, 1), material=diamondMinecraft)
Cubo3 = AABB(position=(1, 0, -4.5), size=(1, 1, 1), material=goldMinecraft)
Cubo4 = AABB(position=(0, -1, -6), size=(1, 1, 1), material=glowstoneMinecraft)
# Agregar los planos a la escena
raytracer.scene.append(ceiling)
raytracer.scene.append(floor)
raytracer.scene.append(back_wall)
raytracer.scene.append(left_wall)
raytracer.scene.append(right_wall)

raytracer.scene.append(Diskk)
raytracer.scene.append(Diskk1)
raytracer.scene.append(Diskk2)
raytracer.scene.append(Diskk3)
raytracer.scene.append(Cubo1)
raytracer.scene.append(Cubo2)
raytracer.scene.append(Cubo3)
raytracer.scene.append(Cubo4)



#Luces
#raytracer.lights.append(AmbientLight(intensity=0.1))  
#raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.9))  
#raytracer.lights.append(PointLight(point=(1.5, 0, -5), intensity=1, color=(1, 0, 1)))   
# Luces
ambient_light = AmbientLight(intensity=0.2, color=(1, 1, 1))  # Luz ambiental suave
directional_light = DirectionalLight(direction=(1, -1, -1), intensity=0.6, color=(1, 1, 1))  # Luz direccional principal
point_light = PointLight(point=(2, 2, 2), intensity=1.0, color=(1, 1, 1))  # Luz puntual (ajusta la posición según sea necesario)

# Agregar las luces a la escena
raytracer.lights.append(ambient_light)
raytracer.lights.append(directional_light)

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