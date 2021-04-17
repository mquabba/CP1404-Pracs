names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

first_initials = [name[0] for name in names]
print(first_initials)


full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: use a list comprehension to create a list of all of the full_names
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)
# in lowercase format
# lowercase_full_names =

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)
# from the above list of strings
# numbers =

# TODO: use a list comprehension to create a list of only the numbers that are
big_numbers = [number for number in numbers if number > 9]
print(big_numbers)
# greater than 9 from the numbers (not strings) you just created