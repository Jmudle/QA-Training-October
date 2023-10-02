mark= int(input("Please enter mark"))
if mark >100 or mark <1:
    print("Error: Please enter mark between 1 and 100")
grade= int(input("Please enter grade"))
if grade >2 or grade <1:
    print("Error: Please enter either 1 or 2")
elif grade == 1:
    if mark <50:
        print('Fail')
    elif 50<=mark<=60:
        print ('Pass')
    elif 61<=mark<=70:
        print ('Merit')
    elif 71<=mark<=100:
        print('Distinction')
    print('Thanks for using this service')
elif grade == 2:
    if mark <40:
        print('Fail')
    elif 40<=mark<=50:
        print ('Pass')
    elif 51<=mark<=65:
        print ('Merit')
    elif 66<=mark<=100:
        print('Distinction')
    print('Thanks for using this service')
    