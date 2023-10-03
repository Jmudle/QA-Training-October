# Function to convert a day-time string (DD:HH:MM) to minutes
def time_to_minutes(time_str):
    days, hours, minutes = map(int, time_str.split(':'))
    total_minutes = days * 24 * 60 + hours * 60 + minutes
    return total_minutes

# Function to convert minutes to a day-time string (DD:HH:MM)
def minutes_to_time(minutes):
    days, minutes = divmod(minutes, 24 * 60)
    hours, minutes = divmod(minutes, 60)
    return f"{days:02d}:{hours:02d}:{minutes:02d}"

# Function to add two day-time strings
def add_times(time1_str, time2_str):
    total_minutes = time_to_minutes(time1_str) + time_to_minutes(time2_str)
    return minutes_to_time(total_minutes)

# Function to find the difference between two day-time strings
def difference_times(time1_str, time2_str):
    minutes1 = time_to_minutes(time1_str)
    minutes2 = time_to_minutes(time2_str)
    difference = abs(minutes1 - minutes2)
    return minutes_to_time(difference)

# Function to convert a day-time string to hours
def convert_to_hours(time_str):
    total_minutes = time_to_minutes(time_str)
    hours = total_minutes / 60
    return hours

# Function to convert a day-time string to minutes
def convert_to_minutes(time_str):
    total_minutes = time_to_minutes(time_str)
    return total_minutes

# Main program
while True:
    print("Time Calculator:")
    print("1. Add 2 times")
    print("2. Find the difference between 2 times")
    print("3. Convert to Hours")
    print("4. Convert to Minutes")
    print("5. Convert Minutes to Time")
    print("6. Convert Hours to Time")
    print("7. Convert Days to Time")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        time1 = input("Enter the first time (DD:HH:MM): ")
        time2 = input("Enter the second time (DD:HH:MM): ")
        result = add_times(time1, time2)
        print(f"The sum of the two times is: {result}")
    elif choice == '2':
        time1 = input("Enter the first time (DD:HH:MM): ")
        time2 = input("Enter the second time (DD:HH:MM): ")
        result = difference_times(time1, time2)
        print(f"The difference between the two times is: {result}")
    elif choice == '3':
        time_str = input("Enter the time (DD:HH:MM): ")
        result = convert_to_hours(time_str)
        print(f"Time in hours: {result} hours")
    elif choice == '4':
        time_str = input("Enter the time (DD:HH:MM): ")
        result = convert_to_minutes(time_str)
        print(f"Time in minutes: {result} minutes")
    elif choice == '5':
        minutes = int(input("Enter the minutes: "))
        result = minutes_to_time(minutes)
        print(f"Time in DD:HH:MM format: {result}")
    elif choice == '6':
        hours = float(input("Enter the hours: "))
        minutes = hours * 60
        result = minutes_to_time(minutes)
        print(f"Time in DD:HH:MM format: {result}")
    elif choice == '7':
        days = int(input("Enter the days: "))
        result = f"{days:02d}:00:00"
        print(f"Time in DD:HH:MM format: {result}")
    elif choice == '8':
        print("Exiting the Time Calculator.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-8).")
