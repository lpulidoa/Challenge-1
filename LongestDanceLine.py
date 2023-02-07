import numpy as np

danceFloor = 'DanceFloor02.txt'

overView=np.loadtxt(danceFloor, skiprows=1, dtype=int)
overView.astype(int)
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
