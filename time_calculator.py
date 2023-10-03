def calculate_duration(start_time, end_time):
    # Parse the input time strings into hours and minutes
    start_hours, start_minutes = map(int, start_time.split(':'))
    end_hours, end_minutes = map(int, end_time.split(':'))

    # Calculate the total minutes for both times
    start_total_minutes = start_hours * 60 + start_minutes
    end_total_minutes = end_hours * 60 + end_minutes

    # Calculate the duration in hours and minutes
    duration_minutes = end_total_minutes - start_total_minutes
    duration_hours = duration_minutes // 60
    duration_minutes %= 60

    return duration_hours, duration_minutes

while True:
    print("Main Menu:")
    print("1. Calculate Duration")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        start_time = input("Enter the start time (HH:MM): ")
        end_time = input("Enter the end time (HH:MM): ")

        try:
            hours, minutes = calculate_duration(start_time, end_time)
            print(f"Duration: {hours} hours and {minutes} minutes")
        except ValueError:
            print("Invalid input format. Please use HH:MM format for time.")
    elif choice == '9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
