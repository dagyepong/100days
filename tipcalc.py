print("Welcome to the tip calculator. ")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people do you split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
# final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person will pay: ${final_bill}")

