import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def get_row(matrix, row):
    """
    Gets row of a given matrix.
    """
    return matrix[row]

def get_column(matrix, column_number):
    """
    Gets a column of a given matrix.
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

def dot_product(vector_one, vector_two):
    """
    Finds the dot product of two given vectors
    """
    result = 0  
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        det = 0
        if self.h == 1:
            det = self.g[0][0]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a * d - b * c)
        return det
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace += self[i][i]
        
        return trace
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here             
        result = []

        if self.h == 1 :
            result.append([1/self.g[0][0]])
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            factor = 1 / (a*d - b*c)
            row_1 = [factor*d, -factor*b]
            row_2 = [-factor*c, factor*a]
            result.append(row_1)
            result.append(row_2)
         
        return Matrix(result)
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for c in range(self.w):
            new_row = []
            for r in range(self.h):
                new_row.append(self[r][c])
            transpose.append(new_row)
        return Matrix(transpose)
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
 
        # TODO - your code here
        matrixSum = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c])
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        # TODO - your code here
        ans = []
        for i in range(self.h):
            rows = []
            for j in range(self.w):
                rows.append(self[i][j] * -1)
            ans.append(rows)
        return Matrix(ans)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """  
        # TODO - your code here
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
 
        # TODO - your code here
        matrixSub = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] - other.g[r][c])
            matrixSub.append(row)
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """  
        # TODO - your code here
        m_rows = self.h
        p_columns = other.w
        
        result = []
        
        for i in range(m_rows):
            row = []
            for j in range(p_columns):
                dp = dot_product(get_row(self.g,i),get_column(other.g,j))
                row.append(dp)
            result.append(row)
        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass  
            # TODO - your code here
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] *= other   
        
        return self
            