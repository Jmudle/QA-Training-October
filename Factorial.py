number = int(input("please enter a number to factor:"))
fact = 1
current_num = 1
while current_num <= number:
    fact *= current_num
    current_num += 1
    print(f"The factorial of {number} is {fact}")