#Bogo Sort (The worst solving algorithm, randomizes list until it hits/is sorted)

#1 (simpler)
import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
   for index in range(len(values)):
       if values[index] > values[index + 1]:
           return False
   return True


def bogo_sort(values):
   attempts = 0
   while not is_sorted(values):
       print(attempts)
       random.shuffle(values)
       attempts += 1
   return True

print(bogo_sort(numbers))
#Type in console python big_o.py numbers/num.txt
