import numpy as np

example = 'DanceFloor01.txt'

danceFloor=np.loadtxt(example, skiprows=1, dtype=int)
danceFloor.astype(int)
n=len(danceFloor)
caminos=np.zeros((n,n))

# Volver función de calcular caminos
m=0
for i in range(n):
	
	for j in range(n):
		n1=1
		n2=1
		if(i>0):
			if(np.absolute(int(danceFloor[i][j])-int(danceFloor[i-1][j]))==1):
				n1=caminos[i-1][j]+1
		if(j>0):
			if(np.absolute(int(danceFloor[i][j])-int(danceFloor[i][j-1]))==1):
				n2=caminos[i][j-1]+1
		if(n1>n2):
				caminos[i][j]=n1
		else:
				caminos[i][j]=n2
		if(caminos[i][j]>m):
			m=caminos[i][j]

print(danceFloor)						
print(caminos)
print(m)
x=np.where(caminos==m)
print(x)

#def findLongestPath( danceFloor ):
	

# volver función de reconstruir caminos 
i1=x[0][0]
i2=x[1][0]
m=int(m)
rec=np.zeros((m,2))
rec[0][0]=i1
rec[0][1]=i2
for i in range(m-1):
	if(i2!=0):
		if(np.absolute(int(danceFloor[i1][i2])-int(danceFloor[i1][i2-1]))==1 and int(caminos[i1][i2])-int(caminos[i1][i2-1])==1): 
			i2=i2-1
		else:
			i1=i1-1
	else:
		i1=i1-1
	rec[i+1][0]=i1
	rec[i+1][1]=i2
		
print(rec)

longestPath= []
for index in rec: 
	longestPath.insert(0,danceFloor[int(index[0])][int(index[1])])
	
print(longestPath)

# volver función de hacer el string 
def PathString(path):
	pathString = ""
	for step in path:
		pathString += str(step) + "-"
	pathString = pathString[:-1]	
	return pathString

print(PathString(longestPath))
