grade = int(input("Enter grade: "))

def check_grade():
    if grade >= 90:
        print("Excellent!")
    elif grade < 90 and grade >= 75:
        print("First Class")
    elif grade < 75 and grade >= 40:
        print("Average")
    else:
        print("The biggest room is the room for I.M.P.R.O.V.E.M.E.N.T")


check_grade()


    