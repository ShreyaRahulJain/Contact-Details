ci=[]
def add_contact(ci):
    ac=[]
    name=input("Enter name - ")
    ac.append(name)
    phone=int(input("Enter phone number - "))
    ac.append(phone)
    email=input("Enter email - ")
    ac.append(email)
    address=input("Enter address - ")
    ac.append(address)
    ci.append(ac)
    print(ci)
def full(ci):
    print(ci)
def search(ci):
    s=int(input("Enter the seach number - "))
    for i in ci:
        if i[1]==s:
            print(i)
def update(ci):
    n=input("Enter the name whose details have to be changed - ")
    for i in ci:
        if i[0]==n:
            i[1]=int(input("Enter the new phone number - "))
            i[2]=input("Enter the new email - ")
            break
        else:
            print("Name not found")
    print(ci)
def delete_contact(ci):
    sn=input("Enter whose details have to be deteled - ")
    for i in ci:
        if i[0]==sn:
            ci.remove(i)
    print(ci)
while 1:
    print("1 - Add contact")
    print("2 - View list")
    print("3 - Search contact")
    print("4 - Update contact")
    print("5 - Delete contact")
    print("6 - Exit")
    choice=int(input("Enter choice - "))
    if choice==6:
        print("Terminated")
        break
    if choice==1:
        add_contact(ci)
    elif choice==2:
        full(ci)
    elif choice==3:
        search(ci)
    elif choice==4:
        update(ci)
    elif choice==5:
        delete_contact(ci)
