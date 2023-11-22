from OpenGL.GL import *
from numpy import array, float32
import pygame
import glm
from mathcou import normalize
from obj import Object

class Model (object):
    def __init__(self, fileName, texturename):
        
        # self.vertBuffer = array(data, dtype= float32)
        
        self.VBO = glGenBuffers(1)
        self.VAO = glGenVertexArrays(1)
        
        self.position = glm.vec3(0,0,0,)
        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)
        self.scale= glm.vec3(1,1,1)
        self.myObject = Object(fileName,texturename)
        self.convertToVertBuffer()
        self.loadTexture(texturename)
    
    def convertToVertBuffer(self):
        converted = []
        for i in range(0, len (self.myObject.faces)):
            for j in range(0,len(self.myObject.faces[i])):
                #agregar los vertices de la cara
                vertex= self.myObject.vertices[self.myObject.faces[i][j][0]-1]
                vertx=vertex[0]
                verty=vertex[1]
                vertz=vertex[2]
                converted.append(vertx)
                converted.append(verty)
                converted.append(vertz)
                #agregar las textcoords
                textcoords= self.myObject.texcoords[self.myObject.faces[i][j][1]-1]
                uv1=textcoords[0]
                uv2=textcoords[1]
                converted.append(uv1)
                converted.append(uv2)
                
                
                #agregar las normales
                normals= self.myObject.normals[self.myObject.faces[i][j][2]-1]
                normalx=normals[0]
                normaly=normals[1]
                normalz=normals[2]
                converted.append(normalx)
                converted.append(normaly)
                converted.append(normalz)
            


            
            
            
        self.vertBuffer = array(converted, dtype= float32)
        print(len(self.vertBuffer)/8)
            
            
            
    
    
    
    def loadTexture(self, textureName):
        
        self.textureSurface = pygame.image.load(textureName) 
        self.textureData = pygame.image.tostring(self.textureSurface,"RGB",True)
        self.textureBuffer = glGenTextures(1)
        
        
        
        
    def getModelMatrix(self):
        identity = glm.mat4(1)
        translateMat = glm.translate(identity, self.position)
        
        pitch = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        yaw = glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        roll = glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1))
        
        rotationMat = pitch*yaw*roll
        scalemat = glm.scale(identity, self.scale)
        
        return translateMat * rotationMat * scalemat
    
    def render(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)
        
        glBufferData(GL_ARRAY_BUFFER, self.vertBuffer.nbytes,self.vertBuffer,GL_STATIC_DRAW)
        
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE, 4*8, ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(0)
        
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,4*8,ctypes.c_void_p(4*3))
        
        glEnableVertexAttribArray(1)
        
        
        glVertexAttribPointer(2,3,GL_FLOAT,GL_FALSE,4*8,ctypes.c_void_p(4*5))
        
        glEnableVertexAttribArray(2)
        
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.textureBuffer)
        # print(self.textureSurface.get_width())
        
        
        myheight= self.textureSurface.get_height()-1
        mywidth = self.textureSurface.get_width()-1
        glTexImage2D(GL_TEXTURE_2D , 0, GL_RGB, mywidth, myheight,0, GL_RGB, GL_UNSIGNED_BYTE ,self.textureData)
        glGenerateTextureMipmap(self.textureBuffer)

        
        
        
        
        glDrawArrays(GL_TRIANGLES,0,int(len(self.vertBuffer)/8))