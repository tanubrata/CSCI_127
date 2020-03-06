# Name: Tanubrata Dey
# Date: Feb 27, 2018
# This Program prints: elevation data of NYC and displays using the default color map



import numpy as np
import matplotlib.pyplot as plt



elevations = np.loadtxt('elevationsNYC.txt')


mapShape = elevations.shape + (3,)


floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = 1.0
        elif elevations[row,col] <= 6:
            floodMap[row,col,0] = 1.0
       
            
        elif elevations[row,col] <= 20:
            floodMap[row,col,0] = 0.5
            floodMap[row,col,1] = 0.5
            floodMap[row,col,2] = 0.5
            
            
            
        else:
            floodMap[row,col,1] = 1.0
     



plt.imsave('floodMap.png', floodMap)
