phonebook = {}

def addEntry():
    name = input("Enter Name:")
    number = int(input("Enter Number:"))
    phonebook[name] = number
    print("Entry done.")

def delEntry():
    name = input("Enter Name:")
    if name in phonebook:
        del phonebook[name]
    else:
        print("Entry doesnt exist.")

def searchEntry():
    name = input("Enter Name:")
    if name in phonebook:
        print("Name:", name, "Number:", phonebook[name])
    else:
        print("Entry doesnt exist.")

def sortDict():
    global phonebook
    phonebook = dict(sorted(phonebook.items(), key=lambda x: x[0]))
    print("Entries sorted.")

def display():
    for key in phonebook.keys():
        print(key, ":", phonebook[key])

while(True):
    choice = int(input("Enter you choice: \n1. Enter Data\n2. Delete Data\n3. Search Data\n4. Display Data\n5. Sort Data\n6. Exit\n"))
    if choice == 1:
        addEntry()
    elif choice == 2:
        delEntry()
    elif choice == 3:
        searchEntry()
    elif choice == 4:
        display()
    elif choice == 5:
        sortDict()
    elif choice == 6:
        break
    else:
        print("Invalid choice.")

