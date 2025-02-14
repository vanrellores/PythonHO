UserOne = int(input("Enter User1 Score: "))
UserTwo = int(input("Enter User2 Score: "))
UserThree = int(input("Enter User3 Score: "))

if UserOne > UserTwo and UserOne > UserThree:
    print("User One scored the highest!")
elif (UserTwo > UserOne and UserTwo > UserThree):
    print("User Two scored the highest!")
elif UserThree > UserOne and UserThree > UserTwo:
    print("User Three scored the highest!")
else:
    print("It's a tie")