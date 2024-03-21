#Quicksort

#from random import randint

#def create_array(lenght_arr=10, maxint=50):
#    return [randint(0, maxint) for _ in range(lenght_arr)]

#def quicksort(values):
#    if len(values) <= 1:
#        return values
#    #Make 2 empty lists
#    less_than_pivot = []
#    greater_than_pivot = []
#    pivot = values[0] #Choose pivot value
#    for value in values[1:]:
#        if value <= pivot:
#            less_than_pivot.append(value)
#        else:
#            greater_than_pivot.append(value)
#    #Combines all 3 lists to make a sorted list
#    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot) #Recursion here
    

#array = create_array()
#print(array)
#array = quicksort(array)
#print(array)

#OR

from random import randint

def create_array(lenght_arr=10, maxint=50):
    return [randint(0, maxint) for _ in range(lenght_arr)]


def quicksort(arr):
    if len(arr) <= 1: return arr

    smaller_than_pivot = []
    equal_to_pivot = []
    larger_than_pivot = []
    pivot = arr[randint(0, len(arr) - 1)]
    for value in arr:
        if value < pivot:
            smaller_than_pivot.append(value)
        elif value == pivot:
            equal_to_pivot.append(value)
        else:
            larger_than_pivot.append(value)
    return quicksort(smaller_than_pivot) + equal_to_pivot + quicksort(larger_than_pivot)

array = create_array()
print("Unsorted Values:", array)
s = quicksort(array)
print("Sorted Values:", s)
