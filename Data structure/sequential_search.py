def sequential_search(key,arr):
    for index in arr:
        if key == index:
            return f'The index of {key} in the list is {arr.index(index)}'
    
    return 'Not Found'


my_list = [64, 34, 25, 90, 12, 22, 11]
print(sequential_search(90,my_list))



