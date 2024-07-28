
"""
Moving Zeroes:

Given an array nums, write a program that moves all O's to the 
end of the array while maintaining the relative order of the 
non-zero elements.

"""

size = int(input('Enter the size of the array: '))
print('Enter the elements of the array: ')
list = []

for i in range(size):
    element=int(input())
    list.append(element)

# list = [0, 1, 2, 0, 3, 4, 0, 5]

zeroes = [i for i in list if i == 0] # get the elements with 0
not_zeroes = [i for i in list if i>0] # get the elements with non-zero 

list_1 = not_zeroes + zeroes # combine the lists


print(list)
print(f'Original Array: {list}')
print(f'Modified Array: {list_1}')


# better with the use of stack:
for i in range(len(list)):
    if list[i] == 0:
        list.append(list.pop(i))

print(f'Modified Array: {list}')
