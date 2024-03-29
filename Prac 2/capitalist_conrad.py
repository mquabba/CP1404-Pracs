import random

MIN_PRICE = 0.01
MAX_DECREASE = 0.05
MAX_PRICE = 1000.0
MAX_INCREASE = 0.1

INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_output.txt"

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
day = 0
print("The Starting price: ${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)


out_file.close()