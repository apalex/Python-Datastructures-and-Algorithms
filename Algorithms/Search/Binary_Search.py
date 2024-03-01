#Binary Search 
#Cuts the list in half on every recursive call by comparing middle value to target
#Worst/Average case 0(log2(n))

def binary_search(array, target):
    index_first = 0
    index_last = len(array) - 1
    #// means floor divison operator, it rounds down to the nearest whole number
    while index_first <= index_last:
        mid_point = (index_first + index_last) // 2
        if array[mid_point] == target:
            return mid_point
        elif array[mid_point] < target:
            index_first = mid_point + 1
        else:
            index_last = mid_point - 1
    return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')

list_search = [1, 2, 3, 4, 5, 6, 7, 8]
result = binary_search(list_search, 3)
verify(result)

search_names = ['Apoo', 'Kid', 'Luffy']
for n in search_names:
    index = binarch_search(names, n)
    print(index)