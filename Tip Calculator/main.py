print("Welcome to Usama's tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage % tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_percentage = tip / 100
tip_amount = (bill / people) * (tip_percentage + 1)
round_tip_amount = round(tip_amount, 2)
print(f"Each person should pay: ${round_tip_amount}")
