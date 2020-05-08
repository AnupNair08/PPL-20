#Program for LU decomposition of a matrix
import numpy as np
def lu(mat,n):
    l = [[0 for x in range(n)] for y in range(n)]
    u = [[0 for x in range(n)] for y in range(n)]

    #Building each row of the Upper Triangular Matrix
    #U[i][j] = A[i][j] - sum(L[i][j] , U[j][k]) for j from 0 to i and k from i to n-1


    #L[i][k] = A[i][k] - sum(L[i][j], U[j][k]) / U[k][k] for j from 0 to i and k from i to n-1


    for i in range(n):
        for j in range(i,n):
            s = 0
            for k in range(i):
                s += l[i][k] * u[k][j]
            u[i][j] = mat[i][j] - s

        for k in range(i,n):
            if(i == k):
                l[i][i] = 1
            else:
                s = 0
                for j in range(i):
                    s += l[k][j] * u[j][i]
                l[k][i] = int((mat[k][i] - s ) / u[i][i] ) 
    return l,u
mapping = ['a','b','c','d','e','f','g','h','i','j']
l = []
C = []
n = int(input('Enter number of equations : '))
print('Enter the equations : ')
for i in range(n):
    m = []
    for j in range(0,n+1):
        c = int(input('Enter {} : '.format(mapping[j])))
        if(j == n):
            C.append(c)
        else:
            m.append(c)
    l.append(m)

L,U = lu(l,n)
Z = np.linalg.solve(L,C)
X = np.linalg.solve(U,Z)
print('Solution of the system of linear equtaions by LU decomposition is :')
print(X)


