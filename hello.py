print("Hello to tha program!")
var = int(input("Enter the first number: "))
var1 = int(input("Enter tha second number: "))
action = input("Enter the function which you want to perform on python calculator: ")
if action=="+":
    print("Sum is: " )
    print(var+var1)
elif action=="*":
    print("Product is:")
    print(var*var1)
elif action=="/":
    print("Divison is:")
    print(var/var1)
elif action=="-":
    print("Subtraction is: ")
    print(var-var1)
else :
    print("Invalid action")       

print("Match case ------")
number= int(input("Enter the number"))

match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Default input")
        