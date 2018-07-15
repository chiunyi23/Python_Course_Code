import random
# from copy import deepcopy

class Matrix:
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.rows = nrows
        self.cols = ncols
        self.mat = [[None] * (self.cols) for i in range(self.rows)]
        self.set_matrix()

    def set_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                num = random.randint(0, 9)
                self.mat[i][j] = num
        
    def add(self, _matrix):
        """return a new Matrix object after summation"""
        if (self.rows is not _matrix.rows) or (self.cols is not _matrix.cols):
            return None
        add_matrix = Matrix(self.rows, self.cols)
        for i in range(add_matrix.rows):
            for j in range(add_matrix.cols):
                add_matrix.mat[i][j] = self.mat[i][j] + _matrix.mat[i][j]
        return add_matrix

    def sub(self, _matrix):
        """return a new Matrix object after substraction"""
        if (self.rows is not _matrix.rows) or (self.cols is not _matrix.cols):
            return None
        sub_matrix = Matrix(self.rows, self.cols)
        for i in range(sub_matrix.rows):
            for j in range(sub_matrix.cols):
                sub_matrix.mat[i][j] = self.mat[i][j] - _matrix.mat[i][j]
        return sub_matrix

    def mul(self, _matrix):
        """return a new Matrix object after multiplication"""
        if self.cols is not _matrix.rows:
            return None
        mul_matrix = Matrix(self.rows, _matrix.cols)
        for i in range(mul_matrix.rows):
            for j in range(mul_matrix.cols): 
                sum = 0   
                for k in range(self.cols):
                    sum = sum + self.mat[i][k] * _matrix.mat[k][j]
                mul_matrix.mat[i][j] = sum
        return mul_matrix

    def transpose(self):
        """return a new Matrix object after transpose"""
        trans_matrix = Matrix(self.cols, self.rows)
        for i in range(trans_matrix.rows):
            for j in range(trans_matrix.cols):
                trans_matrix.mat[i][j] = self.mat[j][i]
        return trans_matrix 
    
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.mat[i][j], end=' ')
            print("")
        print("")
        
""" Matrix A """
rowsA = int(input("Enter A matrix's rows:"))
colsA = int(input("Enter A matrix's cols:"))
matrix_a = Matrix(rowsA, colsA)
print("Matrix A(", rowsA, ",", colsA, "):")
matrix_a.display()

""" Matrix B """
rowsB = int(input("Enter B matrix's rows:"))
colsB = int(input("Enter B matrix's cols:"))
matrix_b = Matrix(rowsB, colsB)
print("Matrix B(", rowsB, ",", colsB, "):")
matrix_b.display()

""" add matrixs """
matrix_add = matrix_a.add(matrix_b)
print("======== A + B ===========")
if matrix_add:
    matrix_add.display()
else:
    print("Matrixs' size should be in the same size", end='\n\n')

""" subtract maxtrixs """
matrix_sub = matrix_a.sub(matrix_b)
print("======== A - B ===========")
if matrix_sub:
    matrix_sub.display()
else:
    print("Matrixs' size should be in the same size", end='\n\n')

""" multiply matrixs """
matrix_mul = matrix_a.mul(matrix_b)
print("======== A * B ===========")
if matrix_mul:
    matrix_mul.display()
else:
    print("Matrix A's row should be in the same size of Matrix B's column", end='\n\n')

""" transpose the matrix """
print("== the transpose of A*B ==")
if matrix_mul:
    matrix_trans = matrix_mul.transpose()
    matrix_trans.display()
else:
    print("Matrix A*B does not exist", end='\n\n')
