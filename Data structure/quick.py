
def quick(arr,pivot=None):
    n = len(arr)

    if n <= 1: return arr

    if pivot is None:
        pivot = arr[n//2]

    left = [x for x in arr if x > pivot] 
    mid = [x for x in arr if x == pivot] 
    right = [x for x in arr if x < pivot] 

    # return quick(left) + mid + quick(right) # Decreasing
    return quick(right) + mid + quick(left) # Increasing


my_list = [64, 34, 25, 90, 12, 22, 11]
sorted_list = quick(my_list)
print(f'Sorted List: {sorted_list}')




