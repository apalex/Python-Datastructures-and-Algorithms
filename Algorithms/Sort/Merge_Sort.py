#Merge Sort

from random import randint

def create_array(length_arr=10, maxint=50):
    return [randint(0, maxint) for _ in range(length_arr)]

#https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0 #Initial index of first subarray
        j=0 #Initial index of second subarray
        k=0 #Initial index of merged subarray
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",alist)
