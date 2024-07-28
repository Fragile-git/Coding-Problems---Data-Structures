def bubble(arr):
    n = len(arr) 

    # This loop runs n times, where n is the length of the array
    for i in range(n):
        print(f"Pass: {i+1}, Swap checks: {n-i-1} , List: {arr} " )

        for j in range(0, n - i- 1):
            if arr[j] < arr[j+1]:
                # Swap if the elements found is greater than the next element 
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                """
                Basically for each pass: puts the largest/smallest element 
                of the unsorted part of the list at the end of the sorted list 

                arr[j] > arr[j+1] - Sort in Ascending
                arr[j] < arr[j+1] - Sort in descending
                """

my_list = [64, 34, 25, 90, 12, 22, 11]
bubble(my_list)
print(f'Sorted List: {my_list}')

