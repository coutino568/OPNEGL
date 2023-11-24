from OpenGL.GL import *

#pip installPyGLM

import glm

from buffer import Buffer
import pygame
from pygame.locals import *
from model import Model
from gl import Renderer
from math import cos,sin,tan,radians
from shader import *



width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
pygame.display.set_caption('OPEN GL RENDERER')
rend= Renderer(screen)

clock = pygame.time.Clock()


shaders= [fragment_shader_toon,fragment_shader,fragment_shader_black_and_white , fragment_shader_normal]
shaderindex=0
rend.setShaders(vertex_shader, fragment_shader_toon)



triangleModel =Model("witchkingcentered.obj","metal.jpg")
triangleModel.position.z = -20
triangleModel.scale = glm.vec3(2,2,2)
rend.scene.append(triangleModel)
# rend = Renderer(screen)

timesinceshaderchange =0



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
                
                
    if keys[K_w]:
        rend.camPosition.z -= 5*deltatime
               
    elif keys[K_s]:
        
        rend.camPosition.z += 5*deltatime
        
    if keys[K_d]:
        rend.camPosition.x -= 5*deltatime
               
    elif keys[K_a]:
        
        rend.camPosition.x += 5*deltatime
        
        
        
    elif keys[K_f]:
        ##Solo para evitar que se cambie demasiado rapido de shader
        if timesinceshaderchange > 1:
            shaderindex = (shaderindex+1) % len(shaders)
            rend.setShaders(vertex_shader, shaders[shaderindex])
            timesinceshaderchange =0
        
        
    
    mousemovx, mousemovy = pygame.mouse.get_rel()
    rend.light.x -= mousemovx*0.05
    
    # rend.light.y += mousemovy
        
    
    
    rend.update()
    triangleModel.rotation.y += 20*deltatime
    rend.render()
    
    rend.elapsedTime+= deltatime
    timesinceshaderchange+=deltatime
    
    
    pygame.display.flip()
 

pygame.quit()


