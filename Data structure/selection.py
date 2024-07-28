def selection(arr):
    n = len(arr) 

    # This loop runs n times, where n is the length of the array
    for i in range(n):
        index = i 
        print(f"Pass: {i+1}, List: {arr} " )

        for j in range(i+1,n): # compare the elements after the current index (i)
            if arr[index] > arr[j]: 
                index = j # get the index of the element 
                """
                Basically for each pass: finds the index of the largest/smallest element 
                and swaps with current index

                arr[index] < arr[j] - Sort in Ascending
                arr[index] > arr[j] - Sort in descending
                """
        # Swap the elements with the current element at index i
        arr[i] , arr[index] = arr[index], arr[i]

my_list = [64, 34, 25, 90, 12, 22, 11]
selection(my_list)
print(f'Sorted List: {my_list}')

