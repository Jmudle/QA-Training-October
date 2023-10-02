var1 = int(input("please enter first number"))
var2 = int(input("please enter second number"))
print('Add +')
print('Subtract -')
print('Multiply *')
print('Divide /')
print('square s')
var3 = input("please choose calculation:")


if var3 == '+':
    sum = int(var1) + int(var2)
    print(sum)
elif var3 == '-':
    sum = int(var1) - int(var2)
    print(sum)
elif var3 == '*':
    sum = int(var1) * int(var2)
    print(sum)
elif var3 == '/':
    sum = int(var1) / int(var2)
    print(sum)
elif var3 == 's':
    sum = int(var1) ** int(var2)
    print(sum)
