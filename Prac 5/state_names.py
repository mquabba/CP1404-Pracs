CODE_TO_NAME = {"ACT": "Australian Capital Territory", "VIC": "Victoria",
                "QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "TAS": "Tasmania"}

state = input("Enter short state Name: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state Name")
    state = input("Enter short state: ").upper()