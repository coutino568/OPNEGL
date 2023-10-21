from OpenGL.GL import *

#pip installPyGLM

import glm

from buffer import Buffer
import pygame

from gl import Renderer

from shader import *



width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )

rend= Renderer(screen)

clock = pygame.time.Clock()

rend.setShaders(vertex_shader, fragment_shader)

triangle =[-0.5,-0.5,0.0,  1.0,0.0,0.0,
           0.0,0.5,0.0,  0.0,1.0,0.0,
           0.5,-0.5,0.0  ,0.0 ,0.0,1.0]


rend.scene.append(Buffer(triangle))
# rend = Renderer(screen)





isRunning =True

while isRunning:
    deltatime= clock.tick(60)/1000
    keys = pygame.key.get_pressed()
    
    
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
        
    rend.render()
    pygame.display.flip()
 

pygame.quit()


