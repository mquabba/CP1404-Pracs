numbers = []

for a in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("First number is", numbers[0])
print("Smallest number is", min(numbers))
print("Largest number is", max(numbers))
print("Last number is", numbers[-1])
print("Average numbers is", sum(numbers) / len(numbers))

usernames = ['giltson98', 'derekf', 'BaseStdIn', 'jimbo', 'WhatSup',
             'swei45', 'StartServer', 'BaseInterpreterInterface', 'NicolEye',
             'InteractiveConsole', 'Command', 'ExecState', 'InterpreterInterface',
             'bob']
username = input("Enter username:")
if username is usernames:
    print("access granted")
else:
    print("access denied")