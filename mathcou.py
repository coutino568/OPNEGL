
#para multiplicaciones de dos matrices
def matrixMultiplication(matrix1, matrix2):
    # print(matrix1)
    # print(matrix2)
    result =  [[0 for x in range(len(matrix1))] for y in range(len(matrix2[0]))]
    
    if(len(matrix1[0])== len(matrix2)):
        #print("Tamaño valido")
        
        for i in range(0, len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                # local=0
                # value1= matrix1[j][j] * matrix2[j][i]
                # value2= matrix1[][j] * matrix2[j][i]
                # value3= matrix1[j][j]*matrix2[j][i]
                # result = value1+value2+value3
        # print(result)
                
        
    
    else:
        print("Tamaño Invalido")
    



#para operacion de un vectori y una matriz
def matrixVectorMultiplication (matrix, vector):
    
    result =[[0 for i in range (len(matrix))] for j in range (len(matrix[0]))]
    print(result)
    if(len(vector)==len(matrix[0])):
        #print("Tamaño valido")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] = matrix[i][j]*vector[j]
                
                
                
        print(result)        
    else:
        print("Tamaño invlaido")


# matrix1= [[5,2,4],[2,1,1],[1,2,3]]
# matrix2 = [[1,0,2],[4,3,1],[2,0,3]]

# matrix3= [[12,7],[4 ,0]]
# matrix4= [[5,2],[6,0]]

# vector1 = [100,0,0.00001]

# resultadoMatrices= matrixMultiplication(matrix1,matrix2)
#resultado esperado: [102,24 ] [20,8]
# resultadoMatrices= matrixMultiplication(matrix3,matrix4)

# #resultado esperado
# resultadoMatrices= matrixVectorMultiplication(matrix1,vector1)


def dotProduct (Vector1, Vector2):
    if len(Vector1) == len(Vector2):
        result = 0
        for i in range(len(Vector1)):
            result += Vector1[i]*Vector2[i]
        
        return result
        
    else:
        return []
    
    
# print(dotProduct([1,3],[5,4]))
    

def baricentricCoordinates(A, B, C, P):
    
    ABC_Area = getAreaOfTiangle(A,B,C)
    PBC_Area= getAreaOfTiangle(P,B,C)
    APC_Area= getAreaOfTiangle(A,P,C)
    ABP_Area= getAreaOfTiangle(A,B,P)
    
    if PBC_Area ==0 or ABC_Area ==0 or ABP_Area ==0 or APC_Area ==0:   
        
        return 0,0,0
        
    else :
        u= PBC_Area/ABC_Area
        v= APC_Area/ABC_Area
        w=  ABP_Area/ ABC_Area
    
    
        return u,v,w
    
    
    
    
    
def getAreaOfTiangle(A,B,C):
    # print (A)
    # print (B)
    # print(C)
    result = 0.5*((A[0]*B[1])+(B[0]*C[1])+(C[0]*A[1]))- 0.5*((A[1]*B[0])+(B[1]*C[0])+(C[1]*A[0]))
    
    
    
    return result