#Selection Sort (Bad solving algorithm)

#import sys

#def selection_sort(unsorted_list):
#    sorted_list = []
#    print("%-25s %-25s" % (values, sorted_list))
#    for i in range(0, len(unsorted_list)):
#        index_to_move = index_of_min(unsorted_list)
#        sorted_list.append(unsorted_list.pop(index_to_move))
#        print("%-25s %-25s" % (values, sorted_list))
#    return sorted_list



#def index_of_min(values):
#    min_index = 0
#    for i in range(1, len(values)):
#        if values[i] < values[min_index]:
#            min_index = i
#    return min_index

#arr = [5, 2, 1, 6, 8, 3, 20]
#print(selection_sort(arr))
#Type in console 'python big_o.py numbers/1.txt

#OR

from random import randint

#Creates a random array with size="" and a maximum integer of max=""
def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


def selection_sort(arr):
    sort_length = 0 #Length of current sorted portion
    while sort_length < len(arr):
        min_index = None #Index of smallest item in arr
        for index, item in enumerate(arr[sort_length:]):
            #Check item/element to see if smallest
            if min_index == None or item < arr[min_index]:
                #Update with current smallest
                min_index = index + sort_length
        #After for loop completion, swap values
        arr[sort_length], arr[min_index] = arr[min_index], arr[sort_length]
        sort_length += 1
    return arr

arr = create_array()
print("Unsorted:", arr)
arr= selection_sort(arr)
print("Sorted:", arr)
