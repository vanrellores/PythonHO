#Nested If

username = input("Enter your username: ")
password = input("Enter your password: ")
department = input("Enter your department name: ")

if username == "John":
    if password == "1234":
        if department == "OCC":
            print(f"Welcome {username}")
        else:
            print("Access Denied")
    else:
        print("Incorrect Password - Please enter correct password")
else:
    print("User not found")



