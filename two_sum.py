
""" 
Given an array of integers and a target sum, 
find two numbers in the array that add up to the target sum. 
give me a sample of integers 

"""

 

def find_sum(array,target):
    for i,value in enumerate(array): # iterate every element of the array
        if target-value in array[i+1:]: 
            # (target - value) is the value needed to add up the target sum
            # Start comparing starting after the next index until the last index of the array
            return [i,array.index(target-value,i+1)] # return the index 
    return None

# Input the array: 
nums = []
num = int(input("Give the length of the array: "))
for i in range(num):
    add = int(input(f"Enter index {i}: "))
    nums.append(add)
    
# find the target value:     
target = int(input("Give a target: "))
x = find_sum(nums,target)

if x is None:
    print("No Solution Found")
else:
    print(f"The Indices of the 2 Numbers that add to {target} is {x[0]} and {x[1]}")



