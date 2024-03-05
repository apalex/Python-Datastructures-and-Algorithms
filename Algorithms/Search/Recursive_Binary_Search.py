#Recursive Binary Search

def recursive_binary_search(lis, target):
   if len(lis) == 0:
       return False
   else:
       midpoint = (len(lis))//2
       if lis[midpoint] == target:
           return True
       elif lis[midpoint] < target:
           return recursive_binary_search(lis[midpoint + 1:], target)
       else:
           return recursive_binary_search(lis[:midpoint], target)

def verify(result):
   print('Target is found: ', result)

list_search = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(list_search, 10)
verify(result)
