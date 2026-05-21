expenses = []
def add_expense(item, amount):
    expenses.append({"item": item, "amount": amount})
    print(f"Added: {item} - {amount}\n")
    
    
add_expense("pizza", 300)
add_expense("auto", 120)

def get_expenses():
    for expense in expenses:
        print(f"{expense['item']} - {expense['amount']}\n")
              
##get_expenses()

def delete_expenses(item_name):
    found = False
    for expense in expenses:
        if expense['item'] == item_name:
            expenses.remove(expense)
            print(f"Deleted: {item_name}\n")
            found = True
            return
        
    if found == False:
        print(f"{item_name} is not available in the list\n")

##delete_expenses("")

def update_expense( item_name, new_amount):
    for expense in expenses :
        if expense['item'] ==item_name:
            expense['amount'] = new_amount
            print(f"Updated amount of {item_name} is {new_amount}")
            return
update_expense("pizza", 370)
get_expenses()
