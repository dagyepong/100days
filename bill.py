print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 0, 6, 8, or 10? "))
people = int(input("How many people are to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
each_bill = bill_with_tip // people
print(f"Each one will pay $ {each_bill} ")
