import numpy as np


class GaussMethods:
    def __init__(self , a , b):
        self.a = a
        self.b = b
        self.n = len(b)

    # swap lines
    def swapLines(self , k):
        for i in range(k+1 , self.n):
            if np.fabs(self.a[i][k]) > np.fabs(self.a[k][k]):
                for j in range(k , self.n):
                    self.a[k][j], self.a[i][j] = self.a[i][j] , self.a[k][j]
                self.b[k] , self.b[i] = self.b[i] , self.b[k]
                print(f"swap L{k} with L{i}")
                for l in self.a:
                    print(l , end="\n")
                break

    # divide the pivot row << convert it to ones
    def pivotDivision(self , k):
        pivot = self.a[k][k]

        for j in range(k , self.n):
            self.a[k][j] = self.a[k][j] / pivot

        self.b[k] = self.b[k] / pivot

    # Eliminate the othe value of matrix

    def eleminator(self , k):
        for i in range(self.n):
            if i == k or self.a[i][k] == 0 : continue
            factor = self.a[i][k]
            for j in range(k,self.n):
                self.a[i][j] -= factor * self.a[k][j]
            self.b[i] -= factor * self.b[k]



class Gauss(GaussMethods):
    def __init__(self , a , b):
        super().__init__(a,b)

    # calculate matrix
    def calculateMatrix(self):
        for k in range(self.n):
            if np.fabs(self.a[k][k]) < 1.0e-12:
                super().swapLines(k)

            # divide pivot row
            super().pivotDivision(k)
            # elimination loop
            super().eleminator(k) 
        return [self.b , self.a]


a = [[0,2,0,1], [2,2,3,2], [4,-3,0, 1], [6,1, -6, -5]]
b = [0,-2, -7,6]

gauss = Gauss(a,b)

result = gauss.calculateMatrix()

for l in result[1]:
    print(l , end="\n")
