# Name: Tanubrata Dey
# Date:  Mar 5, 2018
# This program prints: to create a map that outlines the coastline



import numpy as np
import matplotlib.pyplot as plt



elevations = np.loadtxt('elevationsNYC.txt')


mapShape = elevations.shape + (3,)


floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0: 
            
           floodMap[row,col,2] = 0.5    
        elif elevations[row,col] <=1:
            
           floodMap[row,col,0] = 0.75
           floodMap[row,col,1] = 0.75
           floodMap[row,col,2] = 0.75
        else:
            floodMap[row,col,1] = 0.5
            floodMap[row,col,0] = 0.5
            floodMap[row,col,2] = 0.5
     




plt.imsave('coast.png', floodMap)
