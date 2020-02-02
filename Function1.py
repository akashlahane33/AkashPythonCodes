
# creating an empty list
list = []

# number of elemetns as input
num = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, num):
    ele = int(input())

    list.append(ele)  # adding the element

print(list)

def count(list):

    even = 0
    odd = 0

    for i in list:

        if i%2==0:
            even = even + 1
        else:
            odd = odd + 1

    return(even,odd)

even, odd = count(list)

print("even : {} and odd : {}".format(even,odd))

