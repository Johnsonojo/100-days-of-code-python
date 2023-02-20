# Write a program which will mark a spot with an X. The map is made of 3 rows of blank squares. Your program should allow you to enter a position of the treasure using a two-digit system. The first digit is the vertical column number and the second is the horizontal row number.

def treasure_map():
    row1 = ["⬜", "⬜", "⬜"]
    row2 = ["⬜", "⬜", "⬜"]
    row3 = ["⬜", "⬜", "⬜"]
    map = [row1, row2, row3]

    # print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")

    horizontal = int(position[0])
    vertical = int(position[1])

    map[vertical - 1][horizontal - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")


treasure_map()
