#Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_Bill = bill*(tip/100)+bill
print(f"${total_Bill:.2f}")
print(f"The amount to be paid for {people} is ${round(total_Bill/people, 3)}")


