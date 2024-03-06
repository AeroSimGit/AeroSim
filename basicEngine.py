"""
basicEngine.py - part of the AeroSim software written by Andrew Timokhov licensed under the MIT license

MIT License

Copyright (c) 2024 Andrew Timokhov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import numpy as np
import helperConstants as constants


####RUNTIME CONSTANTS####
wing = [[0, 0], [1, 2], [2, 1], [3, 0]]  # Wing shape
angle = 0  # Angle, not yet implemented
speed = 5  # Wind speed from the reference point of the wing in meters per second (m/s)
wingBottomLength = constants.distance(wing[0], wing[len(wing) - 1])
#DragCoefficient = 
#########################

##Mutable variables used during runtime

wingTopLength = 0
forceY=0

# some calculations using Bernouli

for i in range(len(wing) - 1):
    wingTopLength = wingTopLength + constants.distance(wing[i], wing[i + 1])

wingTopSpeed = speed * (wingTopLength / wingBottomLength)
print(wingTopSpeed)

wingTopPressure = constants.atmPressure+1/2*constants.airDensity*(speed**2-wingTopSpeed**2)
print(wingTopPressure)

for i in range(len(wing)-1):
    slope = -1/((wing[i+1][1]-wing[i][1])/(wing[i+1][0]-wing[i][0]))
    radians = np.arctan(slope)
    
    
    sine = np.sin(radians)
    if (sine <=0):
        sine=-sine
    print(sine)
    forceY=forceY-wingTopPressure*constants.distance(wing[i],wing[i+1])*sine
    print(forceY)
forceY=forceY+constants.atmPressure*constants.distance(wing[0], wing[len(wing)-1])
print(forceY)
    
    
