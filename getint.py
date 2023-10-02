min_value = 1
max_value = 100

attempts = 0

while attempts < 3:
    try:
        user_input = int(input(f"Enter an integer between {min_value} and {max_value}: "))
    
        if min_value <= user_input <= max_value:
            print(user_input)
            break
        else:
            print(f"Invalid input. Please enter a value between, {min_value} and {max_value}")
    except ValueError:
        print(f"Invalid input. Please enter a valid integer.")

    attempts += 1

if attempts == 3:
    print(None)
    

    