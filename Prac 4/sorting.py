from operator import itemgetter

names_with_ages = [['Derek', 7], ['Aaron', 9], ['Carrie', 8], ['Bob', 6]]

names_with_ages.sort()
print(names_with_ages)

names_with_ages.sort(key=itemgetter(1))
print(names_with_ages)

data = [['Carrie', 7], ['Bob', 6], ['Derek', 7], ['Aaron', 6]]
data.sort(key=itemgetter(1, 0))
print(data)

# TODO: sort the following list of tuples by last name then first name
items = [('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6)
        ('123', 'Derek', 'Smith', 7), ('124', 'Carrie', 'Brown', 7),
         ]
print(items)