
# Describe the problem

def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it")
my_function()

# Reproduce the bug

from random import randint
dice_imgs = ["😎", "😂", "✌️", "👌", "🙈", "😔"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Fix the errors

age = int(input("What is your age? "))
if age > 18:
    print(f"You can drive at age {age}")
    