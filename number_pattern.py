

start = 1
end = int(input("Input How many lines: "))

print("1st pattern: ")


for line in range(start,end+1):
    for elements in range(1,line+1): # increasing value with respect to line
        print(elements, end=' ')
    print()
""" With respect to 2nd for Loop
1       = in range(1, 1 + 1 ) = range(1,2) = 1x 
1 2     = in range(1, 2 + 1 ) = range(1,3) = 2x 
1 2 3   = in range(1, 3 + 1 ) = range(1,4) = 3x 
1 2 3 4 = in range(1, 4 + 1 ) = range(1,5) = 4x 
"""


print()
for line in range(start,end+1):
    elements = end # get the last value with respect to the # of lines 
    for x in range(1,line+1):
        print(elements, end=' ')
        elements -= 1
    print()
print()
""" With respect to 2nd for Loop
4       = in range(1, 1 + 1 ) = range(1,2) = 1x
4 3     = in range(1, 2 + 1 ) = range(1,3) = 2x  
4 3 2   = in range(1, 3 + 1 ) = range(1,4) = 3x  
4 3 2 1 = in range(1, 4 + 1 ) = range(1,5) = 4x 

"""

print("2nd pattern: ")
for line in range(start,end+1):
    for elements in range(start,(end+2)-line): # (end +2) + 1 for inclusive end value, 
        # +1 so that decreasing elements happens at column 2 
        print(elements, end=' ')
    print()
""" With respect to 2nd for Loop
1 2 3 4 = in range(1, 6 - 1) = range(1,5) = 4x 
1 2 3   = in range(1, 6 - 2) = range(1,4) = 3x
1 2     = in range(1, 6 - 3) = range(1,3) = 2x
1       = in range(1, 6 - 4) = range(1,2) = 1x
"""


print()


for line in range(start,end+1):
    elements = end
    for y in range(start,(end+2)-line):
        print(elements, end=' ')
        elements -= 1
    print()
  

""" With respect to 2nd for Loop
4 3 2 1 = in range(1, 6 - 1) = range(1,5) = 4x 
4 3 2   = in range(1, 6 - 2) = range(1,4) = 3x
4 3     = in range(1, 6 - 3) = range(1,3) = 2x
4       = in range(1, 6 - 4) = range(1,2) = 1x
"""
"""
for line in range(start,end+1):
    elements = (end+1) - line 
    for y in range(start,(end+2)-line):
        print(elements, end=' ')
        elements -= 1
    print()

Pattern: 

4 3 2 1 
3 2 1 
2 1 
1
"""

print()

print("3rd pattern: ")
for line in range(start,end+1):
    for x in range(1,(end+1)-line): # spaces, (end+1) + 1 for inclusive end value,  
        # - line decrease the number of spaces with respect to the line number
        print(" ",end=' ')
    for elements in range(1,line+1): #increasing number 
        print(elements, end=' ')
    print()

""" With respect to 3rd for Loop
      1  = in range(1, 1 + 1) = range(1,2) = 1x 
    1 2  = in range(1, 2 + 1) = range(1,3) = 3x
  1 2 3  = in range(1, 3 + 1) = range(1,4) = 2x
1 2 3 4  = in range(1, 4 + 1) = range(1,5) = 1x
"""




print()

for line in range(start,end+1):
    elements = end # we start the value at the end parameter
    for x in range(1,(end+1)-line): # spaces, (end+1) + 1 for inclusive end value,  
        #  i decrease the number of spaces with respect to the line number
        print(" ",end=' ')
    for x in range(1,line+1):   #decreasing number 
        print(elements, end=' ')
        elements -= 1
    print()
""" With respect to 3rd for Loop
      4  = in range(1, 1 + 1) = range(1,5) = 4x 
    4 3  = in range(1, 2 + 1) = range(1,4) = 3x
  4 3 2  = in range(1, 3 + 1) = range(1,3) = 2x
4 3 2 1  = in range(1, 4 + 1) = range(1,2) = 1x
"""


print()

print("4th pattern: ")
for line in range(start,end+1):
    for x in range(1,line):  # spaces is 1,i because you want to start the spaces at the 2nd line range(1,2)
        print(" ",end=' ')

    for elements in range(1,(end+2)-line):
        # (end +2) + 1 for inclusive end value, 
        # +1 so that decreasing elements happens at column 2 
        print(elements, end=' ')
    print()

""" With respect to 3rd for Loop
1 2 3 4  = in range(1, 6 - 1) = range(1,5) = 4x 
  2 3 4  = in range(1, 6 - 2) = range(1,4) = 3x
    3 4  = in range(1, 6 - 3) = range(1,3) = 2x
      1  = in range(1, 6 - 4) = range(1,2) = 1x
"""



print()

for line in range(start,end+1):
    printing = end
    for x in range(1,line):  # spaces is 1,i because you want to start the spaces at the 2nd line range(1,2)
        print(" ",end=' ')
    for x in range(1,(end+2)-line):
        # (end +2) + 1 for inclusive end value, 
        # +1 so that decreasing elements happens at column 2 
        print(printing, end=' ')
        printing -= 1
    print()
""" With respect to 3rd for Loop
1 2 3 4  = in range(1, 6 - 1) = range(1,5) = 4x 
  2 3 4  = in range(1, 6 - 2) = range(1,4) = 3x
    3 4  = in range(1, 6 - 3) = range(1,3) = 2x
      1  = in range(1, 6 - 4) = range(1,2) = 1x
"""




print()

print("5th pattern: ")

for line in range(start, end+1):
    right = line
    for x in range(start,(end+1)-line): # spaces
        print(" ", end=' ')
    for left in range(1,line+1): # left side with middle 
        print(left, end=" ")
    for x in range(1,line): # right side 
        print(right-1, end=" ")
        right -=1
    print()
""" With respect to 3rd for Loop
      1  = in range(1, 1 + 1) = range(1,2) = 1x 
    1 2  = in range(1, 2 + 1) = range(1,3) = 3x
  1 2 3  = in range(1, 3 + 1) = range(1,4) = 2x
1 2 3 4  = in range(1, 4 + 1) = range(1,5) = 1x

    With respect to 4th for Loop
        = in range(1,1) = 0x, since you want to start at the second line
1       = in range(1,2) = 1x
2 1     = in range(1,3) = 2x
3 2 1   = in range(1,4) = 3x
"""

print()

for line in range(start,end+1):
    right = end -line # for the decreasing value ; i = 1 : 5-1 ; i = 2 : 5-2 
    for x in range(1,line): # spaces
        print(" ", end=' ')
    for left in range(start,(end+2)-line): # left side with middle 
        print(left, end=" ")
    for right in range(start,(end+1)-line): 
        print(right, end=" ")
        right -= 1 
    print()




""" With respect to 3rd for Loop
1 2 3 4  = in range(1, 6 - 1) = range(1,2) = 1x 
  1 2 3  = in range(1, 6 - 1) = range(1,3) = 3x
    1 2  = in range(1, 3 + 1) = range(1,4) = 2x
      1  = in range(1, 4 + 1) = range(1,5) = 1x

    With respect to 4th for Loop
3 2 1   = in range(1, 5 - 1) = range(1,4) = 3x 
2 1     = in range(1, 5 - 2) = range(1,3) = 2x 
1       = in range(1, 5 - 3) = range(1,2) = 1x 
        = in range(1, 5 - 4) = range(1,1) = 0x, since you dont want to print anymore at the 4th line 
"""




print()

print("6th pattern: ")
end_6 = (end+1)*2
for line in range(start,end_6):
    if line < end_6/2: 
        for elements in range(start,line):
            print(elements, end=' ')
    else:
        for elements in range(start,(end_6-line)):
            print(elements, end=' ')
    print()



"""
An hourglass pattern is a geometric figure represented within a 2D grid. 
The figure consists of a top triangle, a middle line, and a bottom triangle. 
Write a program that receives a number and generates an hourglass
pattern of height 2n+1. The hourglass is centered within the grid. Use the *
character to represent the hourglass and spaces for the empty areas.
"""
size = int(input('Enter size: '))

for i in range(size+1,0,-1): # decreasing 
    spaces = ' ' * (size+1-i) # increasing number of sizes 
    top = spaces + '*' * (2*i-1)
    print(top)
    
for i in range(2,size+2):
    spaces = ' ' * (size+1-i)
    bot = spaces + '*' * (2*i-1)
    print(bot)


    
    



    
















