total = 0
number = int(input("number of items: "))
while number < 0:
    print("invalid number of items")
    number = int(input("number of item: "))
for i in range(number):
    price = float(input("price of item: "))
    total +- price

if total > 100:
    total *= 0.1

print("total price for ", number, " items is $", total, sep='')
print("Total price for {} items is ${:.2f}".format(number, total))
