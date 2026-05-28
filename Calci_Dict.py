print("___This is the Calculator by using Dictionary Function___\n")
def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def div(a,b):
    
    return(a/b)

def mul(a,b):
    return(a*b)

def rem(a,b):
    return(a%b)

operations = {
    1: add,
    2: sub,
    3: div,
    4: mul,
    5: rem,
}

print("========Calculator==========")
print("choose 1. Addition")
print("choose 2. subtration")
print("choose 3. Division")
print("choose 5. Multipliction")
print("choose 6 Remainder")

a=int(input("Enter the First number="))
b=int(input("Enter the second number="))

choice=int(input("Share the choice number, Operation take place accordingly"))
if choice in operations:
    result=operations[choice](a,b)
    print("Your result =", result)
    
else:
    print("Enter the correct option")