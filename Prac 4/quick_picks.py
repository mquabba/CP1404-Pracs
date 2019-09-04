import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_quick_picks = int(input("How many quick picks? "))
    while number_quick_picks < 0:
        print("error, doesn't make sense")
        number_of_quick_picks = int(input("How many quick picks? "))

for a in range(number_quick_picks):



