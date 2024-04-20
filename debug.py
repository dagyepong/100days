year = int(input("What's your birth year? "))
if year > 1980 and year <= 1994:
    print("You're a millenial. ")
elif year > 1994:
    print("You're a Gen z. ")
# Always understand the problem before you can debug

def mutate(a_liist):
    b_list = []
    for item in a_liist:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])
# always double check your breakpoint in a loop