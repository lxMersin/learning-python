print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? "))
bill_percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = float(input("How many people to split the bill? "))

full_price = bill_total / 100
tip = full_price * bill_percentage_tip + bill_total
total = tip / split
final_amount = round(total, 2)
final_amount = "{:.2f}".format(total)

print(f"Each person should pay ${final_amount}")