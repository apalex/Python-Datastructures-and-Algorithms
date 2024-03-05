# Linear Search (One by one, from start to finish)

def linear_search(list, target):
   for i in range(0, len(list)):
       if list[i] == 'target':
           return i
   return None

def verify(index):
   if index is not None:
       print('Target found at index: ", index)
   else:
       print('Target not found in list")

numbers = [1, 2, 3, 4, 5]
result = linear_search(numbers, 3)
verify(result)

# OR 

def linear_search(lst, target):
   for index, value in enumerate(lst):
       if value == target:
           return index
   return -1
