#import array as arr  - we can import like this also..but we will import like below
from numpy import *

arr = array([1,2,3,4,5])

print(arr.dtype)
print(arr)


arr1 = linspace(0,15,10)
print(arr1)

arr2 = arange(0,15,3)
print(arr2)

arr3 = logspace(0,15,10)
print(arr3)

arr4 = zeros(15)
print(arr4)

arr5 = ones(15,int)
print(arr5)