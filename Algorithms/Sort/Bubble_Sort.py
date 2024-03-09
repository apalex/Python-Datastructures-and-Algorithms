#Bubble sort

from random import randint


def create_array(lenght_arr=10, maxint=50):
    return [randint(0, maxint) for _ in range(lenght_arr)]

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for item in range(1, len(arr)):
            if arr[item-1] > arr[item]: #Swaps if item in array is in a unsorted order
                arr[item], arr[item-1] = arr[item-1], arr[item]
                swapped = True
    return arr

array = create_array()
print(array)
array = bubble_sort(array)
print(array)
