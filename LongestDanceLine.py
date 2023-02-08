import numpy as np

example = 'DanceFloor01.txt'
danceFloor1=np.loadtxt(example, skiprows=1, dtype=int)


def findPaths( danceFloor ):
    n = len(danceFloor)
    paths = np.zeros((n,n))

    for row in range(n):
        for column in range(n):
            stepsUp = 1
            stepsLeft = 1
            if(row>0):
                if(np.absolute(int(danceFloor[row][column])-int(danceFloor[row-1][column]))==1):
                    stepsUp = paths[row-1][column]+1
            if(column>0):
                if(np.absolute(int(danceFloor[row][column])-int(danceFloor[row][column-1]))==1):
                    stepsLeft = paths[row][column-1]+1
            if(stepsUp>stepsLeft):
                    paths[row][column] = stepsUp
            else:
                    paths[row][column] = stepsLeft

    return paths 


def buildLongestPath( paths , danceFloor ):

    lenght = int(paths.max())
    index = np.where( paths==lenght )
    i1 = index[0][0]
    i2 = index[1][0]
    rec=np.zeros(lenght)
    rec[0] = danceFloor[i1][i2]

    for i in range(lenght-1):
        if(i2!=0):
            if(np.absolute(int(danceFloor[i1][i2])-int(danceFloor[i1][i2-1]))==1 and int(paths[i1][i2])-int(paths[i1][i2-1])==1):
                i2 = i2-1
            else:
                i1 = i1-1
        else:
            i1 = i1-1
        
        rec[i+1] = danceFloor[i1][i2]


    longestPath= np.flip(rec)
    longestPath = [int(steps) for steps in longestPath]
    
    return longestPath

def PathString( path ):
	pathString = ""
	for step in path:
		pathString += str(int(step)) + "-"
	pathString = pathString[:-1]	
	return pathString

print( int(findPaths(danceFloor1).max()) )
print( PathString(buildLongestPath( findPaths(danceFloor1), danceFloor1 ) ) )
