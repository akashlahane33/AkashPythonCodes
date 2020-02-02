# Program to take input of city names from user in list and count letter of each name and print it.
# creating an empty list
list = []

# number of elemetns as input
num = int(input("Enter names of number of elements : "))

# iterating till the range
for i in range(0, num):
    ele = str(input())

    list.append(ele)  # adding the element

print(list)

def count(list):

    Numberoflettersinlist = 0

    for i in list:

        Numberoflettersinlist = len(i)
        print("Count of letters in string {}".format(Numberoflettersinlist))

count(list)






