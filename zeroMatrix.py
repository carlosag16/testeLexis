import numpy as np

nlin = 10
ncol = 5
a = np.arange(50).reshape(nlin,ncol)
a[4,4] = 0
a[3,3]=0
a[0,1]=0
#print(a)
b_lin = []
b_col = []
for i in range(0,nlin):
    for j in range(0,ncol):
        if (a[i,j] == 0):

            b_lin.append(i)
            b_col.append(j)

for i in b_lin:
    for k1 in range(0,ncol):
        a[i,k1] = 0

for i in b_col:
    for k1 in range(0,nlin):
        a[k1,i] = 0
print(a)