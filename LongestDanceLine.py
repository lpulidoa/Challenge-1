import numpy as np

def findPaths( dance_floor ):
    n = len(dance_floor)
    paths = np.zeros((n,n))

    for row in range(n):
        for column in range(n):
            stepsUp = 1
            stepsLeft = 1
            if(row>0):
                if(np.absolute(int(dance_floor[row][column])-int(dance_floor[row-1][column]))==1):
                    stepsUp = paths[row-1][column]+1
            if(column>0):
                if(np.absolute(int(dance_floor[row][column])-int(dance_floor[row][column-1]))==1):
                    stepsLeft = paths[row][column-1]+1
            if(stepsUp>stepsLeft):
                    paths[row][column] = stepsUp
            else:
                    paths[row][column] = stepsLeft

    return paths 


def buildLongestPath( dance_floor , paths ):

    lenght = int(paths.max())
    last_step = np.where( paths==lenght )
    row = last_step[0][0]
    column = last_step[1][0]
    longest_path = np.zeros(lenght)
    longest_path[0] = dance_floor[row][column]

    for step in range(lenght-1):
        if(column!=0):
            if(np.absolute(int(dance_floor[row][column])-int(dance_floor[row][column-1]))==1 and int(paths[row][column])-int(paths[row][column-1])==1):
                column-=1
            else:
                row-=1
        else:
            row-=1
        
        longest_path[step+1] = dance_floor[row][column]

    longest_path = np.flip(longest_path)
    
    return longest_path


def pathToString( path ):
	path_string = ""
	for step in path:
		path_string += str(int(step)) + " - "
	path_string = path_string[:-2]	
	return path_string


def winningPath( file ):
     danceFloor = np.loadtxt( file , skiprows=1, dtype=int)
     possible_paths = findPaths(danceFloor)
     path_lenght = int(possible_paths.max())
     winner_path = pathToString( buildLongestPath( danceFloor , possible_paths ) )

     print("Longest Endavans Line Dance is:", winner_path )
     print("Length of Path is:", path_lenght )


winningPath('DanceFloor01.txt')
