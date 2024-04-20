# List items in a dictionary

programming_language = {"Python": "This is great", "JavaScript": "This s nice", "Rust": "This is cool"}
print(programming_language)

#  Add items to the dictionary list
programming_language['Swift'] = "This is awesome"
print(programming_language)

# wipe an existing dictionary
# this is a new dictionary
names_of_cities = {"Joliet", "Bolingbrook", "Naperville"}
# print(names_of_cities)
names_of_cities = {}
# this last code wipes an existing dictionary

# edit arguments in dictionary
programming_language["Python"] = "This is more than great"
print(programming_language)

#  for loops

for key in programming_language:
    print(key)
    print(programming_language[key])