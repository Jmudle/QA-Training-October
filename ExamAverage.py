math_mark = 0
english_mark = 0
ict_mark = 0

for subject in ["Math", "English", "ICT"]:
    while True:
        try:
            mark = int(input(f"Enter the {subject} exam mark (0-100): "))
            if 0 <= mark <= 100:
                if subject == "Math":
                    math_mark = mark
                elif subject == "English":
                    english_mark = mark
                elif subject == "ICT":
                    ict_mark = mark
                break
            else:
                print("Invalid mark. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

average_mark = (math_mark + english_mark + ict_mark) / 3

result = "Pass" if average_mark >= 65 else "Fail"

print(f"Average Mark: {average_mark:.2f}")
print(f"Overall Result: {result}")

