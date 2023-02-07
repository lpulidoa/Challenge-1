import numpy as np

file = 'DanceFloor02.txt'

A=np.loadtxt(file, skiprows=1, dtype=int)
A.astype(int)
n=len(A)
caminos=np.zeros((n,n))

m=0
for i in range(n):
	
	for j in range(n):
		n1=1
		n2=1
		if(i>0):
			if(np.absolute(int(A[i][j])-int(A[i-1][j]))==1):
				n1=caminos[i-1][j]+1
		if(j>0):
			if(np.absolute(int(A[i][j])-int(A[i][j-1]))==1):
				n2=caminos[i][j-1]+1
		if(n1>n2):
				caminos[i][j]=n1
		else:
				caminos[i][j]=n2
		if(caminos[i][j]>m):
			m=caminos[i][j]

print(A)						
print(caminos)
print(m)
x=np.where(caminos==m)
print(x)


i1=x[0][0]
i2=x[1][0]
m=int(m)
rec=np.zeros((m,2))
rec[0][0]=i1
rec[0][1]=i2
for i in range(m-1):
	#print(caminos[i1][i2])
	#print(caminos[i1][i2-1])
	if(i2!=0):
		if(np.absolute(int(A[i1][i2])-int(A[i1][i2-1]))==1 and int(caminos[i1][i2])-int(caminos[i1][i2-1])==1): #if(int(caminos[i1][i2])-int(caminos[i1][i2-1])==1):
			i2=i2-1
		else:
			i1=i1-1
	else:
		i1=i1-1
	rec[i+1][0]=i1
	rec[i+1][1]=i2
		
print(rec)