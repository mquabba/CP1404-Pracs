MAX_COLUMNS = 10
MIN_COLUMNS = 2

LOWER = 33
UPPER = 127

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number < LOWER or number > UPPER:
    number = int(
        input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

for value in range(LOWER, UPPER + 1):
    print("{:3} {:>4}".format(value, chr(value)))

columns = int(input("Enter number of columns: "))
while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
    print("Please use a value between {} and {}".format(MIN_COLUMNS, MAX_COLUMNS))
    columns = int(input("Enter number of columns: "))
number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns


print("Vertical then horizontal ordering")
for row in range(rows + 1):
    starting_value = LOWER + row
    value = starting_value

    for column in range(columns - 1):
        value_to_print = value + (column * rows)
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        value += 1


    value_to_print = value + ((column + 1) * rows)
    if value_to_print <= UPPER:
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    print()