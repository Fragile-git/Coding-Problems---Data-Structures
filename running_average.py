"""
Running Average: 

Given an array of integers, write a program to compute the running average 
of the elements in the array and represent the average as a floating-point 
number with two decimal places. 

The running average at a given index i is the 
average of all the elements from the start of the array up to and including index i.
"""

size = int(input('Enter the size of the array: '))
print('Enter the elements of the array, one per line: ')
array = []

for i in range(0,size):
    element = float(input()) 
    array.append(element)
    ave = sum(array)/len(array) 
    print(f'Running Average at index {i}: {ave:.2f}') #two decimal places




