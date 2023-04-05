# You are painting a wall. The instruction on the paint says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll eed to buy.
# Number of cans =(wall height * wall width) /coverage per can
import math

test_h = int(input("Weight of wall: "))
test_w = int(input("Width of wall: "))
coverage_per_can = 5


def paint_calc(height, width):
    area_of_wall = height * width
    number_of_cans = math.ceil(area_of_wall/coverage_per_can)
    print(f"You'll need {number_of_cans} cans of paint.")


paint_calc(height=test_h, width=test_w)
