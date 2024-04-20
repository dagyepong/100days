def my_function():
    name = input("What is your name?\n ")
    print(f"Hello {name} ")
my_function()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
greet_with_name("Nana")

# more than 1 parameter
def greet_with_name(name, location, meal):
    print(f"Hello {name}")
    print(f"Where in {location} has the best {meal}? ")
greet_with_name("Nana", "Ghana", "Fufu")

# changing the order of parameter
# still needs to fix par 2&1 kinda buggy
def greet_with_name(location:2, meal:1, name:3):
    print(f"Hello there! Are you from {location} ?")
    print(f"Where in {location} can I get the best {meal}? ")
    print(f"Thanks {name}")
greet_with_name('Fufu', 'Ghana', 'John')
