x = [2,4,6,5,5,6,5,4,4,5]

for i in x:

    if i % 9 ==0:
        print(i)
        break
else:
    print('not found')