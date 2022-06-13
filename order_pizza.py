
from re import I


bill = 0 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
    if bill == 15:
        bill +=2
    if bill >=20:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")



