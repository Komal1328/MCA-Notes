#pr9

phonebook={}

def entry():
    name=input("Enter name")
    phno=int(input("Enter number: "))
    phonebook[name]=phno
    print("Entry done")

def del_entry():
    name=input("Enter name to delete:")
    if name in phonebook:
        del phonebook[name]
    else:
        print("entry not found")

def search():
    name=input("Enter name to delete:")
    if name in phonebook:
        print("name: ",name,"number: ",phonebook[name])
    else:
        print("entry not found")

def sortp():
    global phonebook
    phonebook=dict(sorted(phonebook.items(), key=lambda x:x[0]))
    print("sorted phonebook")

def display():
    for key in phonebook.keys():
        print(key,":",phonebook[key])

print("1.entry 2.delete 3.search 4.sort 5.display 6.exit")
while(True):
    ch=int(input("Enter your choice: "))
    if ch==1:
        entry()
    elif ch==2:
        del_entry()
    elif ch==3:
        search()
    elif ch==4:
        sortp()
    elif ch==5:
        display()
    elif ch==6:
        break
    else:
        print("Enter valid choice")
        
    





    
