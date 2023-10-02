mark = int(input("Please enter the mark"))
if mark >100 or mark <1:
    print('Error: Please enter a number between 1 and 100')
elif mark <50:
    print('Fail')
elif mark >=50 or mark <=60:
    print ('Pass')
elif mark >=61 or mark <=70:
    print ('Merit')
elif mark >=71 or mark <=100:
    print('Distinction')
print('Thanks for using this service')
