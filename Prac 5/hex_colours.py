COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter colour name: ")