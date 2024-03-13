emails = {'koshal' : 'guptakoshal1@gmail.com',
          'sachin' : 'Skumar8084064@gmail.com'}

def addEntry():
    name = int(input("Enter name: "))
    em = int(input("Enter email: "))
    emails[name] = em
    print("Entry done.\n")

def delEntry():
    name = int(input("Enter name: "))
    del emails[name]
    print("Entry deleted.\n")

def sortKey():
    global emails
    emails = dict(sorted(emails.items(), key = lambda x:x[0]))
    print("Sorted by names.")

def sortKey():
    global emails
    emails = dict(sorted(emails.items(), key = lambda x:x[1]))
    print("Sorted by emails.")

def printTup():
    for items in emails.items():
        print(items)
    print()



