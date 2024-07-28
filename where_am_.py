"""

In this problem you will need to determine which quadrant a given point is in. 
There are four quadrants, just like a normal quadrant.
Given the X, Y coordinates of a point display 1, 2, 3, or 4 to indicate the quadrant in which the point is located.

"""

while True:

    points = tuple(map(int,input('Enter X and Y separated by a space: ').split()))

    if points[0]>=1: # x is positive
        if points[1]>=1: # y is positive 
            print('Quadrant 1')
        else: 
            print('Quadrant 4') # y is negative 

    if points[0]<=1: # x is negative
        if points[1]>=1: # y is positive 
            print('Quadrant 2')
        else: 
            print('Quadrant 3') # y is negative 








