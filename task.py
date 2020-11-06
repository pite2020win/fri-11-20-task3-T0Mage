#Matrix. 


class Matrix():
    def __init__(self,a=0,b=0,c=0,d=0):
        self.data=[[a,b],[c,d]]
    def __add__(self,other):
        if type(other)== Matrix:
            temp=Matrix()    
            for i in range(2):
                for j in range(2):
                    temp.data[i][j]=self.data[i][j]+other.data[i][j]
            return temp
        if type(other)== int:
            temp=Matrix()    
            for i in range(2):
                for j in range(2):
                    temp.data[i][j]=self.data[i][j]+other
            return temp
    def dot(self,other):
        temp=Matrix()    
        for i in range(2):
            for j in range(2):
                temp.data[i][j]=self.data[i][j]*other.data[i][j]
        return temp

    def __repr__(self):
        return str(self.data)
if __name__ == "__main__":
    matrix_1 = Matrix(4.,5.,6.,7.)
    matrix_2 = Matrix(2.,2.,2.,1.)

    matrix_3 = matrix_2.dot(matrix_1)
    matrix_4 = matrix_2 + matrix_1
    # matrix_4 = 6 + matrix_1
    matrix_5 = matrix_1 + 6
    print(matrix_1)
    print(matrix_2)
    print("dot product of matrixes:")
    print(matrix_3)
    print("sum of matrixes:")
    print(matrix_4)
    print("sum of matrixes1 and 6:")
    print(matrix_5)


