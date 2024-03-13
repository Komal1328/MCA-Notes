phonebook={'p1':1234,
           'p5':5678,
           'p3':9123,
           'p2':5677}
print(phonebook) 

name=input("Enter the name to be inserted: ")
no=int(input("Enter the number: "))
phonebook.update({name:no})
print(phonebook)

name=input("Enter the name to be deleted: ")
del phonebook[name]
print(phonebook)

name=input("Enter the name for searching: ")
print(phonebook.get(name))

