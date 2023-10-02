control = input("1:Find the length of A, given B and C 2:Find the length of B given A and C 3:Find the Length of C given A and B:")

if control == "1":
    num1 = float(input ("please enter the length of side B"))
    num2 = float(input ("please enter the length of side C"))
    res = ((num2**2) - (num1**2)) ** 0.5
    print(res)
elif control == "2":
    num1 = float(input ("please enter the length of side A"))
    num2 = float(input ("please enter the length of side C"))
    res = ((num2**2) - (num1**2)) ** 0.5
    print(res)
elif control =="3":
    num1 = float(input ("please enter the length of side A"))
    num2 = float(input ("please enter the length of side B"))
    res = ((num2**2) - (num1**2)) ** 0.5
    print(res)