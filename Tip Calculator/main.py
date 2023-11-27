print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people would likt to split the bill?"))
split = bill / people
percent_tip_add = 1 + (percent_tip / 100)
total = "{:.2f}".format(split * percent_tip_add)
print(f"Each person should pay: ${total}")