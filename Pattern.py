print("# # # #")


print('# ',end="")
print('# ',end="")
print('# ',end="")
print('# ',end="")
print('# ',end="")

print()

for j in range(10):
    print('# ', end="")

print()

for i in range(10):
    for j in range(10):
        print('# ', end="")
    print()

print()

for i in range(10):
    for j in range(i):
        print('# ', end="")
    print()

for i in range(10):
    for j in range(10-i):
        print('# ', end="")
    print()