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
        self.elapsedTime =0
        
        self.target = glm.vec3(0,0,0)
        self.angle =0
        self.camDistance =5
        
        
        self.activeShader = None
        
        self.camPosition = glm.vec3(0,0,0)
        self.camRotation = glm.vec3(0,0,0)
        self.viewMatrix = self.getViewMatrix()
        self.light = glm.vec3(0.3,-0.5,0)
        
        self.projectionMatrix = glm.perspective(glm.radians(60),self.width / self.height,0.1,1000)
        
        
    def update(self):
        self.getViewMatrix = glm.lookAt(self.camPosition, self.target, glm.vec3(0,1,0))
         
    
    def getViewMatrix(self):
        identity = glm.mat4(1)

        translateMatrix = glm.translate(identity, self.camPosition)

        pitch = glm.rotate(identity, glm.radians( self.camRotation.x ), glm.vec3(1,0,0) )
        yaw   = glm.rotate(identity, glm.radians( self.camRotation.y ), glm.vec3(0,1,0) )
        roll  = glm.rotate(identity, glm.radians( self.camRotation.z ), glm.vec3(0,0,1) )

        rotationMatrix = pitch * yaw * roll

        camMatrix = translateMatrix * rotationMatrix

        return glm.inverse(camMatrix)
    
    
    
    
    
    
    
    def render(self):
        glClearColor(self.ClearColor[0],self.ClearColor[1],self.ClearColor[2],1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        
        if self.activeShader is not None:
            glUseProgram(self.activeShader)
            
            glUniformMatrix4fv( glGetUniformLocation(self.activeShader,"viewMatrix"),1,GL_FALSE,glm.value_ptr(self.viewMatrix))
            glUniformMatrix4fv( glGetUniformLocation(self.activeShader,"projectionMatrix"),1,GL_FALSE,glm.value_ptr(self.projectionMatrix))
            
            glUniform1i(glGetUniformLocation(self.activeShader,"tex"),0)
            glUniform1f(glGetUniformLocation(self.activeShader,"time"),self.elapsedTime)
            
            glUniform3fv(glGetUniformLocation(self.activeShader,"light"),1,glm.value_ptr(self.light))
        
        
        for obj in self.scene:
            if self.activeShader is not None:
                glUniformMatrix4fv(glGetUniformLocation(self.activeShader, "modelMatrix"),1, GL_FALSE,glm.value_ptr(obj.getModelMatrix()))
            obj.render()
            
    def setShaders(self,vertexShader,fragmentShader):
        if vertexShader is not None and fragmentShader is not None:
        
            self.activeShader = compileProgram (compileShader( vertexShader, GL_VERTEX_SHADER),
                                                compileShader(fragmentShader, GL_FRAGMENT_SHADER))
            
        else :
            self.activeShader = None
            
        