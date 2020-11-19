import math
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
        elif (len(args)>=1):
            self.init_args(args)

        elif("size"in kwargs.keys()):
            d=[]
            temp= [0] * kwargs["size"]
            for i in range(kwargs["size"]):
                d.append(temp.copy())
            self.init_list(d)
        

        # print(self.data)


    def __iter__(self):
        ind=0   
        while ind<self.size:
            yield self.data[ind]
            ind+=1


    def scalar_operation(self,other,type):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                if(type=="add"):
                    temp.data[i][j]=self.data[i][j]+other
                elif(type=="sub"):
                    temp.data[i][j]=self.data[i][j]-other                
                elif(type=="mul"):
                    temp.data[i][j]=self.data[i][j]*other
                elif(type=="div"):#standard div/0 exception no need for addition handeling
                    temp.data[i][j]=self.data[i][j]/other      
        return temp

    def Matrix_operation(self,other,type):
        temp=Matrix(size=self.size)
        for i in range(self.size):
            for j in range(self.size):
                if(type=="add"):
                    temp.data[i][j]=self.data[i][j]+other.data[i][j]
                elif(type=="sub"):
                    temp.data[i][j]=self.data[i][j]-other.data[i][j]              
                elif(type=="mul"):
                    temp.data[i][j]=self.data[i][j]*other.data[i][j]
                elif(type=="div"):#standard div/0 exception no need for addition handeling
                    temp.data[i][j]=self.data[i][j]/other.data[i][j]     
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


    def inverse(self):
        temp=Matrix(size=self.size)
        for i in range(self.size):
            for j in range(self.size):
                temp.data[i][j]=1/self.data[i][j]
        return temp

    def __rtruediv__(self,other):   
        return self.inverse().__mul__(other)

    def __truediv__(self,other):
        if type(other)== Matrix:
            return self.Matrix_operation(other,"div")
        if type(other)== int or type(other)== float:
            return self.scalar_operation(other,"div")


    def multiply_matrix(self,other):
        temp=Matrix(size=self.size)    
        for i in range(self.size):
            for j in range(self.size):
                for z in range(self.size):
                    temp.data[i][j]+=self.data[i][z]*other.data[z][j]
        return temp

    def __matmul__(self,other):
        if type(other)== Matrix:
            return self.multiply_matrix(other)
        if type(other)== int or type(other)== float:
            return self.multiply_matrix(Matrix(*([other]*self.size**2)))


    def __repr__(self):#includes wightspace for conviniance can be removed using indexing [1,-1]
        r="\n"
        for i in self:
            r+=str(i)
            r+="\n"
        return r

if __name__ == "__main__":
    matrix_1 = Matrix(4.,5.,6.,7.)
    matrix_2 = Matrix(2.,2.,2.,1.)
    matrix_3 = Matrix(1.,2.,3.,1.)
    matrix_4 = Matrix(3.,3.,2.,1.)
    matrix_11 = Matrix(1.,1.,1.,1.,1.,1.,1.,1.,1.)
    matrix_22 = Matrix(1.,1.,1.,1.,1.,1.,1.,1.,1.)
    test_s=2
    to_Test= [[matrix_1,matrix_2,test_s],[matrix_3,matrix_4,test_s],[matrix_11,matrix_22,test_s],[Matrix(1,2,3,4),Matrix(2,0,1,2),3]]
    for M1,M2,s in to_Test:
        print("="*40)
        print(f"\nM1:{M1}")
        print(f"M2:{M2}")
        print(f"M1+M2: {M1+M2}")
        print(f"M1-M2: {M1-M2}")

        try:
            print(f"M1/M2: {M1/M2}")
        except ZeroDivisionError as er:
            print("division by 0 failed",er)
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
        try:
            print(f"M1/s: {M1/s}")
            print(f"s/M1: {s/M1}")
        except ZeroDivisionError as er:
            print("division by 0 failed",er)     

    print("and iterator works:")  
    for i in matrix_1:
        print(i)  
    print(f"\n{repr(matrix_1)[1:-1]}\n{repr(matrix_1)[1:-1]}")



