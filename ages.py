# Define the list of ages
ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65, 36, 83, 50, 11, 79, 64, 78, 37, 3, 8, 68, 22, 4, 60, 33, 82, 45, 23, 5, 18, 28, 99, 17, 81, 14, 88, 50, 19, 59, 7, 44, 93, 35, 72, 25, 63, 11, 69, 11, 76, 10, 60, 30, 14, 21, 82, 47, 6, 21, 88, 46, 78, 92, 48, 36, 28, 51]

# Task 1: Record the length of the ages List in a variable and display it
length_of_ages = len(ages)
print("Length of ages list:", length_of_ages)

# Task 2: Display each age on a separate line
for age in ages:
    print(age)

# Task 3: Add one year to every age
for i in range(len(ages)):
    ages[i] += 1

# Display updated ages
print("Ages after adding one year:", ages)

# Task 4: Remove ages outside the range 16-65
for age in ages[:]:  # Iterate over a copy of the list to avoid issues
    if age < 16 or age > 65:
        ages.remove(age)

# Display updated ages
print("Ages after removing ages outside the range 16-65:", ages)

# Task 5: Display the count of 16-25 year olds
count_16_to_25 = len([age for age in ages if 16 <= age <= 25])
print("Count of 16-25 year olds:", count_16_to_25)

# Task 6: Sort the ages list
ages.sort()

# Display sorted ages
print("Sorted ages:", ages)

# Task 7: Calculate the proportion of ages between 16-25
count_16_to_25 = len([age for age in ages if 16 <= age <= 25])
proportion = count_16_to_25 / length_of_ages
print("Proportion of ages between 16-25:", proportion)
    


