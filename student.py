students = [
    {"id": 1, 
     "name": "sarab", 
     "email": "sarabcheema@gmail.com", 
     "rollno": 234, 
     "course": "python"},
    {"id": 2, 
     "name": "ahmed", 
     "email": "ahmedcheema@gmail.com", 
     "rollno": 343, 
     "course": "java"},
    {"id": 3, 
     "name": "aqeel", 
     "email": "aqeelcheema@gmail.com", 
     "rollno": 789, 
     "course": "web"},
    {"id": 4, 
     "name": "naeem", 
     "email": "naeemcheema@gmail.com", 
     "rollno": 879, 
     "course": "app-dev"}
]


loop = True
while loop:
    print("1 => Enter a new student")
    print("2 => Update student data")
    print("3 => Delete student data")
    print("4 => Display all students")
    print("5 => Exit program!")
    try:
        choice = int(input("Choose the functionality: "))

        if choice == 1:
            newname = input("Enter the name of the student: ")
            newemail = input("Enter the email of the student: ")
            newrollno = int(input("Enter the roll number of the student: "))
            newcourse = input("Enter the course of the student: ")

            newstudent = {
                "id": len(students) + 1,
                "name": newname,
                "email": newemail,
                "rollno": newrollno,
                "course": newcourse
            }
            students.append(newstudent)
            print("New student added successfully!")

        elif choice == 2:
            updateid = int(input("Enter the ID of the student you want to update: "))
            for student in students:
                if student["id"] == updateid:
                    print("What do you want to update?")
                    print("1 => Name")
                    print("2 => Email")
                    print("3 => Roll Number")
                    print("4 => Course")

                    option = int(input("Enter your choice: "))

                    if option == 1:
                        student["name"] = input("Enter new name: ")
                    elif option == 2:
                        student["email"] = input("Enter new email: ")
                    elif option == 3:
                        student["rollno"] = int(input("Enter new roll number: "))
                    elif option == 4:
                        student["course"] = input("Enter new course: ")
                    else:
                        print("Invalid option!")

                    print("Student record updated successfully!")
                    break
            else:
                print("Student ID not found.")

        elif choice == 3:
            deleteid = int(input("Enter the ID of the student you want to delete: "))
            for student in students:
                if student["id"] == deleteid:
                    students.remove(student)
                    print("Student deleted successfully!")
                    break
            else:
                print("Student ID not found.")

        elif choice == 4:
            print("Students in the list:")
            for student in students:
                print(student)

        elif choice == 5:
            loop = False
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice! Please select a valid option.")

    except ValueError:
        print("Invalid input! Please enter a number.")

input("Press Enter to continue...")  
