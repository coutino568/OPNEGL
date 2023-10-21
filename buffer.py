from OpenGL.GL import *
from numpy import array, float32

class Buffer(object):
    def __init__(self,data):
        self.data=data
        self.vertBuffer = array(data, dtype=float32)
        
        self.VBO = glGenBuffers(1)
        
        self.VAO = glGenVertexArrays(1)
        
        
    def render(self):
        
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)
        
        glBufferData( GL_ARRAY_BUFFER, self.vertBuffer.nbytes ,self.vertBuffer , GL_STATIC_DRAW)

        glVertexAttribPointer(0,3,GL_FLOAT, GL_FALSE, 4*6, ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(0)
        
        
        glVertexAttribPointer(1,3,GL_FLOAT, GL_FALSE, 4*6, ctypes.c_void_p(4*3))
        
        glEnableVertexAttribArray(1)
        
        glDrawArrays(GL_TRIANGLES,0,int(len(self.vertBuffer)/6))
        