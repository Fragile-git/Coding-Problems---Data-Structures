"""
What's the difference
you will process two lists of numbers and return the difference. 
The difference are numbers that appear in one of the lists but not both. Consider the following two lists:

The lists can contain any valid integer including negative numbers and zero. 
The same number will not appear twice in the same list.

Input: Input will start with the number of items in the list, n. 
Following are n integers each separated by a single space

Output
Display the differences between the two lists. 
The numbers in the list must by displayed in ascending sequence. Display a message, as shown below, if there are no differences.

"""


list_1 = list(map(int,input('Enter first set of data separated by space: ').split()))
list_2 = list(map(int,input('Enter second set of data separated by space: ').split()))
diff =[]

for i in range(1,len(list_1)):
    if list_1[i] not in list_2:
        diff.append(list_1[i])

for i in range(1,len(list_2)):
    if list_2[i] not in list_1:
        diff.append(list_2[i])

if not diff:
    print('No Difference')
else:
    diff.sort()
    print(diff)


