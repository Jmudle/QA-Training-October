initial_investment = int(input("Please enter your starting capital"))
target_value = int(input("Please enter your goal"))
interest_rate = float(input("Please enter your rate"))
years = 0
while initial_investment < target_value:
    initial_investment += initial_investment * interest_rate
    years += 1
    print(f"It will take", years,"years for the initial investment to grow to", target_value, "at a", interest_rate, "%", "interest rate.")
  