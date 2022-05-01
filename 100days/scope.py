enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

"""Global scope variable is accessible everywhere within the file but local scope is limited to declared function variable"""