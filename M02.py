"""steven brannock
M02 Lab
This application allows for the user to input the last and fisrtb name of a student as well as their GPA.
If ZZZ is entered it will close the application.
If the students Gpa is 3.5 or above the output will acknowledge that the student has made the deans list.
If the GPAS is greater than or equal to 3.25 but not equal to or greater than 3.5 than the output will acknowledge that the student has made the honor roll.
Any GPA entered less than 3.25 will give an output of not applicable N/A.
"""
def check_qualification(last_name):
    #checks for ZZZ which would result in the application closing
    if last_name == 'ZZZ':
        return False
    #checks for first name of the student
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    #gives the output based on students GPA
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    elif gpa < 3.25:
        print("N/A")
    return True

def main():
    #welcomes user to the application
    print("Welcome to the Student Qualification Checker!")
    while True:
        #checks for the students last name
        last_name = input("Enter student's last name (or ZZZ to quit): ")
        if not check_qualification(last_name):
            break

if __name__ == "__main__":
    main()
