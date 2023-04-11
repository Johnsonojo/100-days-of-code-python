################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Modifying a global scope

def multiply_enemies():
    global enemies
    enemies *= 2
    print(f"enemies inside multiply function: {enemies}")


multiply_enemies()
print(f"enemies outside multiply function: {enemies}")
