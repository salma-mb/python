num = int(input("enter your number:"))
if num < 0:
    print("factorial is not defined by negative number")
else:
    result = 1
    while num > 1:
        result *= num
        num -= 1
    print(result)