a = 5
b = 0

try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter the value:"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you cannot devide a number by zero", e)

except ValueError as e:
    print("Invalid Input", e)

except Exception as e:
    print("Something wentt wrong", e)

finally:
    print("Resource Closed")
