print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip you would like to give? 10, 12, or 15? "))

totalBill = bill + ((bill * percentage)/100)
pay = round(totalBill/people, 2)
pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${pay}")