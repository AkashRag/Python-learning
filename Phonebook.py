phonebook={}

def add_contact(name, number):
    phonebook[name]=number
    print(f"{name} added successfully")

def search_contact(name):
    if name in phonebook:
        print(f"{name} phone book main available hai")
    else:
        print(f"{name} phonebook main available nii hai")
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} is removed from the list")
    else:
        print(f"{name} is not available in the list")
def show_All():
    if phonebook:
        for name, number in phonebook.items():    
            print(f"{name} :{number}")
    else:
        print("The phonebook is Empty")

#Main Program

while True:

    print("\n=============PhoneBook=================")
    print("1. Add contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All")
    print("5. Exit")

    choice=int(input("choose:"))
    
    match choice:
        case 1:
            name=input("Name=")
            number=input("Enter the number=")
            add_contact(name,number)
        case 2:
            name=input("Enter the Name=")
            search_contact(name)
        case 3:
            name=input("Enter the name=")
            delete_contact(name)
        case 4:
            show_All()
        case 5:
            print("==Bye==")
            break
        case _:
            print("Choosed the wrong option")




