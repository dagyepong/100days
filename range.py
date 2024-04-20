for number in range(1, 11, 3):
    print(number)
# this loop adds up plus 3 which is the number at the end of the syntax

total = 0
for number in range(1, 101):
    total += number
print(total)
# Sums up numbers from 1 to 100

# add up even numbers

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# or this code also works. Ref Fizzbuzz.py

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

