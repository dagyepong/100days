print("Welcome to the Python Deliveries! ")
console_type = input("What console do you want to purchase? Steam Deck, Aya Neo, or OneX Player: ")
console_capacity = input("What is your choice of hard drive size? 500GB, 1TB, or 2TB: ")
warranty_service = input("Do you want a service after purchase? Y or N: ")
bill = 0

if console_type == "Steam Deck":
    bill += 400
elif console_type == "Aya Neo":
    bill += 600
elif console_type == "OneX Player":
    bill += 800
    if console_capacity == "500GB":
        bill += 100
    elif console_capacity == "1TB":
        bill += 150
    elif console_capacity == "2TB":
        bill += 200
        if warranty_service == "Y":
            bill += 50
    


print(f"Your final bill is ${bill}")

