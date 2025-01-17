# Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per Unit
# Persons living in room/flat

# Output
# Total amount you've to pay is

rent = float(input("Enter your hostel/flat rent = "))
food = float(input("Enter the amount of food ordered = "))
electricity_spend = float(input("Enter the total of electricity spend = "))
charge_per_unit = float(input("Enter the charge per unit = "))
persons = float(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print(f"Each person will pay = {output}")