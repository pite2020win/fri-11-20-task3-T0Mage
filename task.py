import math#Matrix. 


class Matrix():

    def init_list(self,l):
        self.data=l
        self.size=len(l[0])
    def init_args(self,*args):
        self.data=[]
        self.size=int(math.sqrt(len(*args)))
        for i in range(self.size):
            temp=[]
            for j in range(self.size):
                temp.append(args[0][i*self.size+j])
            self.data.append(temp)

    def __init__(self,*args,**kwargs):
        if len(args)==1:
            self.init_list(args[0])
        else:
            self.init_args(args)

        if("size"in kwargs.keys()):
            d=[]
            temp= [0] * kwargs["size"]
            for i in range(kwargs["size"]):
                d.append(temp)
            self.init_list(d)

        # print(self.data)

    def scalar_operation(self,other,type):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                if(type=="add"):
                    temp.data[i][j]=self.data[i][j]+other
                if(type=="sub"):
                    temp.data[i][j]=self.data[i][j]-other                
                if(type=="mul"):
                    temp.data[i][j]=self.data[i][j]*other
                if(type=="div"):#standard div/0 exception no need for addition handeling
                    temp.data[i][j]=self.data[i][j]/other      
        return temp

    def Matrix_operation(self,other,type):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                if(type=="add"):
                    temp.data[i][j]=self.data[i][j]+other.data[i][j]
                if(type=="sub"):
                    temp.data[i][j]=self.data[i][j]-other.data[i][j]              
                if(type=="mul"):
                    temp.data[i][j]=self.data[i][j]*other.data[i][j]
                if(type=="div"):#standard div/0 exception no need for addition handeling
                    temp.data[i][j]=self.data[i][j]/other.data[i][j]     
        return temp    

    def add_scalar(self,other):
        temp=Matrix(size=self.size)    
        for i in range(2):
            for j in range(2):
                temp.data[i][j]=self.data[i][j]+other
        return temp


    def add_Matrix(self,other):
        
        temp=Matrix(size=self.size)    
        for i in range(2):
            for j in range(2):
                temp.data[i][j]=self.data[i][j]+other.data[i][j]
        return temp

    def __neg__(self):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                temp.data[i][j]=- self.data[i][j]
        return temp

    def __radd__(self,other):   
        return self.__add__(other)

    def __add__(self,other):
        if type(other)== Matrix:
            return self.Matrix_operation(other,"add")
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"add")

    def __rsub__(self,other):   
        return -self.__sub__(other)

    def __sub__(self,other):
        if type(other)== Matrix:
            return self.Matrix_operation(other,"sub")
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"sub")


    def __rmul__(self,other):   
        return self.__mul__(other)

    def __mul__(self,other):
        if type(other)== Matrix:
            return self.Matrix_operation(other,"mul")
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"mul")

    def __rtruediv__(self,other):   
        return self.__mul__(other)

    # def __div__(self,other):   
    #     return self.__truediv__(other)

    def __truediv__(self,other):
        if type(other)== Matrix:
            return self.Matrix_operation(other,"div")
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"div")


    def __rmatmul__(self,other):   
        return self.__mul__(other)


    def multiply_matrix(self,other):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                tempSum=0
                for z in range(self.size):
                    tempSum+=self.data[i][z]*other.data[z][j]
                temp.data[i][j]=tempSum
        return temp
    def __matmul__(self,other):
        if type(other)== Matrix:
            return self.multiply_matrix(other)
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"mul")



    def dot(self,other):
        temp=Matrix(size=self.size)    
        for i in range(2):
            for j in range(2):
                temp.data[i][j]=self.data[i][j]*other.data[i][j]
        return temp

    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    matrix_1 = Matrix(4.,5.,6.,7.)
    matrix_2 = Matrix(2.,2.,2.,1.)

    # matrix_3 = matrix_2 @matrix_1
    # matrix_3 = matrix_2*matrix_1
    # matrix_4 = matrix_2 + matrix_1
    # matrix_4 = 6 + matrix_1
    # matrix_5 = matrix_1 + 6
    # print(matrix_1)
    # print(matrix_2)
    # print(f"dot product of matrixes{matrix_2}:")
    # print(matrix_3)
    # print("sum of matrixes:")
    # print(matrix_4)
    # print("sum of matrixes1 and 6:")
    # print(matrix_5)
    # print("6 and sum of matrixes1:")
    # print(matrix_5)

    matrix_3 = Matrix(1.,2.,3.,1.)
    matrix_4 = Matrix(3.,3.,2.,1.)
    matrix_11 = Matrix(1.,1.,1.,1.,1.,1.,1.,1.,1.)
    matrix_22 = Matrix(1.,1.,1.,1.,1.,1.,1.,1.,1.)
    test_s=2
    to_Test= [[matrix_1,matrix_2,test_s],[matrix_3,matrix_4,test_s],[matrix_11,matrix_22,test_s],]
    for M1,M2,s in to_Test:
        print(f"\nM1:{M1}")
        print(f"M2:{M2}")
        print(f"M1+M2: {M1+M2}")
        print(f"M1-M2: {M1-M2}")
        
        print(f"M1/M2: {M1/M2}")
        print(f"M1*M2: {M1*M2}")
        print(f"M1@M2: {M1@M2}")
        print(f"M2@M1: {M2@M1}")

        print(f"\nM1:{M1}")
        print(f"s: {s}")
        print(f"M1-s: {M1-s}")
        print(f"s-M1: {s-M1}")
        print(f"M1+s: {M1+s}")
        print(f"s+M1: {s+M1}")
        print(f"M1*s: {M1*s}")
        print(f"s*M1: {s*M1}")
        print(f"M1/s: {M1/s}")
        print(f"s/M1: {s/M1}")


        # result=matrix_1@matrix_2
        # print(f"matrix multiplication:{result}\n")



