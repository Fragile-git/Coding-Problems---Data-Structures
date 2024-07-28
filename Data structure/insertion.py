def insertion(arr):
    n = len(arr)

    # Start at index 1 
    # Index 0 is the first element of the sorted part 
    for i in range(1,n): # For every other element of the array do:
        key = arr[i]  # Take the current element of the unsorted part to be inserted into the sorted part 
        j = i - 1  # Initialize j to the last index of the sorted part
        
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            # Checks every element of the the sorted part ()
                # j >= 0 & j -= 1 ; Iterate through each element of the sorted part
            # Checks If the current element of the unsorted part (key) is less than the current element of the sorted part
                # If it's less, the index of the current element of the sorted part is decremented by 1
                # arr[j+1] = arr[j] ; Shift the element one position to the right
            

        arr[j+1] = key # If the current element doesn't satisfy the while condition 
                       # Place the key in its correct position in the sorted part
        print(f"Pass {i}, List: {arr}")


my_list = [64, 34, 25, 90, 12, 22, 11]
insertion(my_list)
print(f'Sorted List: {my_list}')


