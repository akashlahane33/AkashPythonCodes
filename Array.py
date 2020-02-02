#import array as arr  - we can import like this also..but we will import like below
from numpy import *
from array import *

vals = array('i',[5,9,8,4,2])

print(vals)
print(vals.buffer_info())  #array functions
vals.reverse()
print(vals)

print(vals[1])

for i in range(5):
    print(vals[i])

for i in range(5):
    print(vals[i])


