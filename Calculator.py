print('Add +')
print('Subtract -')
print('Multiply *')
print('Divide /')
print('square s')
var1 = input(int (0))
var3 = input('choose calculation')
var2 = input(int (0))


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
