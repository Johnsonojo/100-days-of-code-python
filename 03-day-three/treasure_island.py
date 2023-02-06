def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = input(
        "You are at a cross road. Where do you want to go? Type 'left' or 'right'. ").lower()
    if direction == "left":
        if input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower() == "wait":
            if input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower() == "yellow":
                print("You found the treasure! You Win!")
            elif input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower() == "red":
                print("It's a room full of fire. Game Over.")
            elif input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower() == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")


treasure_island()
