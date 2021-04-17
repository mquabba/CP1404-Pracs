menu_string = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(menu_string)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(menu_string)
    choice = input(">>> ").upper()
print("Finished.")