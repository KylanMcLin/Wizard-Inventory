# CITC-2391-C01 Summer 2020
# Program 1
# Name: Kylan McLin
# Date: 7/26/2020
# Lab4


# main function
def main():
    inventory_list = ["wooden staff",
                      "wizard hat",
                      "cloth shoes"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show(inventory_list)
        elif command.lower() == "add":
            add(inventory_list)
        elif command.lower() == "change":
            change(inventory_list)
        elif command.lower() == "drop":
            drop(inventory_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


# display name of project and menu
def display_menu():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("show - Show All Items")
    print("add - Add an Item")
    print("change - Change an Item")
    print("drop - Drop an Item")
    print("exit - Exit Program")
    print()


# Show command
def show(inventory_list):
    i = 1
    for inventory in inventory_list:
        print(str(i), " - ", inventory)
        i += 1
    print()

# add command
def add(inventory_list):
    inventory = input("Name: ")
    inventory_list.append(inventory)
    print(inventory, "was added.\n")


# change command
def change(inventory_list):
    number = int(input("Item Number: "))
    if number < 1 or number > len(inventory_list):
        print("Invalid item number.\n")
    else:
        inventory_list.pop(number - 1)
        updated_name = input("Updated Name: ")
        inventory_list.insert(number - 1, updated_name, )
        print("Item Number", number, "was updated\n")


# drop command
def drop(inventory_list):
    number = int(input("Item Number: "))
    if number < 1 or number > len(inventory_list):
        print("Invalid item number.\n")
    else:
        inventory = inventory_list.pop(number - 1)
        print(inventory, "was dropped.\n")


if __name__ == '__main__':
    main()
