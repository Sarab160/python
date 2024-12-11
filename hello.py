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
