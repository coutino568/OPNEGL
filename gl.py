import glm

from OpenGL.GL import*

from OpenGL.GL.shaders import compileProgram, compileShader

from shader import *

 
class Renderer(object):
    def __init__(self, screen):
        self.screen = screen
        _,_, self.width, self.height = screen.get_rect()
        self.ClearColor = [0,0,0]
        glEnable(GL_DEPTH_TEST)
        glViewport(0,0,self.width, self.height)
        self.scene= []
        self.activeShader = None
        
    def render(self):
        glClearColor(self.ClearColor[0],self.ClearColor[1],self.ClearColor[2],1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        
        if self.activeShader is not None:
            glUseProgram(self.activeShader)
        
        
        for obj in self.scene:
            obj.render()
            
    def setShaders(self,vertexShader,fragmentShader):
        if vertexShader is not None and fragmentShader is not None:
        
            self.activeShader = compileProgram (compileShader( vertexShader, GL_VERTEX_SHADER),
                                                compileShader(fragmentShader, GL_FRAGMENT_SHADER))
            
        else :
            self.activeShader = None
            
        