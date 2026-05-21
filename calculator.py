print("Hii this is the basic calculator")
Num1=int(input("Enter your First number"))
Num2=int(input("Enter the second number"))

choice=int(input("Choose as per your operaation:  1--Addition, 2--Subtraction , 3--Division, 4--Multiplication,, 5--Remainder\n"))

match choice:
 case 1:
    print("Addition=",Num1+Num2)
 case 2:
    print("Subtracti=",Num1-Num2)
 case 3:
    print("Division=",Num1/Num2)
 case 4:
    print("Multiplication=",Num1*Num2)
 case 5:
    print("Remainder=",Num1%Num2)
 case _:
    print("Wrong choice")

