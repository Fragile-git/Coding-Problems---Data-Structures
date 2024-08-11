def binary_search(key,arr):
    low, high = 0, len(arr)-1

    while low <=high:
        mid = low + (high-low)//2 # update the mid value

        if key == arr[mid]:
            return f' The index of {key} in the list is {mid}'
        elif arr[mid]<key: # key is higher
            low = mid + 1 # narrows the searching in the higher value 
        else: 
            low = mid -1 # narrows the searching in the lower value 
    return 'Not Found' # if not found 

my_list = [11, 12, 22, 25, 34, 64, 90]
print(binary_search(25,my_list))
