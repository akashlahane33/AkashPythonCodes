#import array as arr  - we can import like this also..but we will import like below
from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([51,2,53,4,55])

arr1 = arr1 + 5    # add 5 to each element
arr3 = arr1 + arr2
print(arr3)
print(sqrt(arr3))
print(sum(arr3))
print(sort(arr3))
print(max(arr3))
print(concatenate([arr1,arr2]))

arr4 = arr1.view() #shallow copy
print(arr4)

arr5 = arr1.copy() #deep copy
print(arr5)