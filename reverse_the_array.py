"""

Reverse the Array (Many Times)
In this problem you will build a new array using the numbers from an existing array. 
Add each number, one at a time, to the end of the new array. Then reverse the order of the numbers in the new array. 
Repeat this for each number added. For example, given the array [1, 2, 3, 4]. 
Add the first element [1] to the end of a new array and reverse it. 
Then add the second element [2] to the end of the new array and reverse the array.
Repeat this process n times where n is the size of the array. 
The result is the array [4, 2, 1, 3]. Below are the detailed steps for the array [1, 2, 3, 4].


"""

numbers = list(map(int,input('Enter count, integers separated by a space: ').split()))

new_arr = []

for i in numbers: 
    new_arr.append(i)
    new_arr.reverse()


print(new_arr) 





