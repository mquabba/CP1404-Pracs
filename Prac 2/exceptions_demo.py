try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid a number!")
except ZeroDivisionError:
    print("Number must be greater than zero!")
print("Finished.")