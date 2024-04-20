enemies = 1
# local scope is inside defined function
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# global scope is outside defined function

# modify global scope/variable by adding global to the variable

enemies = 0

def increase_enemies():
    global enemies
    enemies += 1