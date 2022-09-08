x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(x)):
    for j in range (len(y)):
        result[i][j]=x[i][j]+y[i][j]
print(result)

x=[[5,1,3],[4,5,6],[7,8,9]]
y=[1,2,3]
out=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        out[i][j]=x[i][j]*y[i]
print(out)


x=[[5,1,3],[4,5,6],[7,8,9]]
out=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        out[i][j]=x[i][j]*9
print(out)

x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,9]]
out=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        out[i][j]=x[i][j]*y[i][j]
print(out)

import numpy as np
a=np.array([[12,7,3],[4,5,6],[7,8,9]])
a_inv=np.linalg.inv(a)
print(a_inv)


a=[[5,8,1],[6,7,3],[4,5,9]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(a[0])):
        res[j][i]=a[i][j]
print(res)







        

