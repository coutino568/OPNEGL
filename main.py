from OpenGL.GL import *

#pip installPyGLM

import glm

from buffer import Buffer
import pygame
from model import Model
from gl import Renderer
from math import cos,sin,tan,radians
from shader import *



width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )

rend= Renderer(screen)

clock = pygame.time.Clock()

rend.setShaders(vertex_shader, fragment_shader)


#primero van los vertices, despues las uvs/texcords y despues las normales
triangle =[-0.5,-0.5,0,   0.0,0.0,        1.0,0.0,0.0,
           0,1,0.1,0   ,  0.0,0.99,      0.0,1.0,0.0,
           0.5,-0.5,0 ,   0.99,0.0,       0.0 ,0.0,1.0]

triangleModel =Model(triangle,"witchkingcentered.obj","metal.jpg")
triangleModel.position.z = -10
triangleModel.scale = glm.vec3(2,2,2)
rend.scene.append(triangleModel)
# rend = Renderer(screen)





isRunning =True

while isRunning:
    
    keys = pygame.key.get_pressed()
    deltatime= clock.tick(60)/1000
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False
    # if keys[K_UP]:
    #     if rend.ClearColor[0]<1:
    #         rend.ClearColor[0]+=deltatime
    # elif keys[K_DOWN]:
    #     if rend.ClearColor[0]>0:
    #         rend.ClearColor[0]-=deltatime
    
    
    
    
    
    
    rend.target.y = rend.camPosition.y
    
    rend.camPosition.x = rend.target.x + sin(radians(rend.angle))* rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle))* rend.camDistance
    
    
    
    rend.update()
    triangleModel.rotation.y += 45*deltatime
    # print(triangleModel.rotation.y)
    rend.render()
    
    rend.elapsedTime+= deltatime
    pygame.display.flip()
 

pygame.quit()


