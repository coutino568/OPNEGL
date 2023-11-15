from os import read
from texture import *
from mathcou import *
import math
import struct
from collections import namedtuple
#CLASE PARA LEER Y DEFINIR LOS COMPONENTES QUE CONFORMAN AL OBJETO EN LA ESCENA
V3 = namedtuple('Point3', ['x', 'y', 'z'])

class Object() :
    def __init__(self, filename,textureFileName , translate = V3(0,0,0), scale = V3(1,1,1), rotate = V3(0,0,0)) :
        
        
        self.filename = filename
        self.vertices =[]
        self.faces = []
        self.normals = []
        self.texcoords = []
        self.textureFilename= textureFileName
        
        
        with open(filename, "r") as file:
            self.lines= file.read().splitlines()
        self.readFile()
        # self.printMe()
        # if textureFileName !=None:
        #     self.texture= Texture(self.textureFilename)
            
        self.printMe()
        
        
    def printMe(self):
        # print("Mis "+str(len(self.vertices))+" vertices son :\n" + str(self.vertices))
        # print("Mis "+str(len(self.faces))+" caras son son :\n" + str(self.faces))
        # print("Mis "+str(len(self.normals))+" normales son :\n" + str(self.normals))
        # print("Mis "+str(len(self.texcoords))+" textcoord son :\n" + str(self.texcoords))
        
        print("Tengo estos vertices  "+str(len(self.vertices)))
        print("tengo estas caras "+str(len(self.faces)) )
        print("tengo estas normales "+str(len(self.normals)))
        print("tengo estas text coords "+str(len(self.texcoords)))
    
        
        
        
    def readFile(self):
        for line in self.lines:
            if line:
                    #divide cada linea en prefijo y contenido
                try:
                        prefix, value = line.split(' ', 1)
                except:
                    continue
                    #clasifica segun prefijos
                    #Vertices
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                    #texcoor
                elif prefix == 'vt': 
                    self.texcoords.append(list(map(float, value.split(' '))))
                    #vertex normals
                elif prefix == 'vn': 
                    self.normals.append(list(map(float, value.split(' '))))
                    #faces
                elif prefix == 'f': 
                    self.faces.append( [ list(map(int, vert.split('/'))) for vert in value.split(' ')] )

    #Define la operacion de traslacion de una matriz.
    def transformObject(self,movementX,movementY,movementZ):
        traslationMatrix = [[1,0,0,movementX],[0,1,0,movementY],[0,0,1,movementZ],[0,0,0,1]]
        self.objectmatrix = matrixVectorMultiplication(self.objectmatrix, traslationMatrix)
        
    
    #Define la operacion de escala de una matriz.
    def scaleObject(self,scaleX,scaleY,scaleZ):
        scaleMatrix = [[scaleX,0,0,0],[0,scaleY,0,0],[0,0,scaleZ,0],[0,0,0,1]]
        self.objectmatrix = matrixVectorMultiplication(self.objectmatrix, scaleMatrix)
        
    #Define la operacion de traslacion de una matriz.
    def rotateObject(self,rotationX,rotationY,rotationZ):
        
        RotationMatrixX = [[1,0,0,0],[0,math.cos(rotationX),-math.sin(rotationX),0,0],[0,0,1,movementZ],[0,0,0,1]]
        RotationMatrixY = [[math.cos(rotationY),0,math.sin(rotationY),0],[0,1,0,0],[-math.sin(rotationY),0,math.cos(rotationY),0],[0,0,0,1]]
        RotationMatrixZ = [[1,0,0,0],[0,math.cos(rotationX),-math.sin(rotationX),0,0],[0,0,1,0],[0,0,0,1]]

        self.objectmatrix = matrixVectorMultiplication(self.objectmatrix, traslationMatrix)
        
    def createObjectMatrix(self,):
        pass