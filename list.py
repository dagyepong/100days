states_of_america = ["Delaware", "Illinois", "Michigan", "Indiana", "Ohio", "Virginia", "Idaho", "Arizona", "Alaska", "Hawaii", "Montana", "New Mexico", "Nevada", "Nebraska", "Oregon", "Kansas", "Tennessee", "Georgia", "Rhode Island", "New York", "Vermont", "Florida", "Wyoming", "Washington"]
print(states_of_america[0])

states = len(states_of_america)
print(states)

# Nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# For loop examaple , Indentation is really important in looping
for fruit in  fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
# For loop with range
total = 0
for number in range(1, 101):
    total += number
print(number)

# random shuffle
import random
x = [1, 2, 3, 4, 5]
random.shuffle(x)
