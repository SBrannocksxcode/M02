def check_qualification(last_name):
    if last_name == 'ZZZ':
        return False
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    elif gpa < 3.25:
        print("N/A")
    return True

def main():
    print("Welcome to the Student Qualification Checker!")
    while True:
        last_name = input("Enter student's last name (or ZZZ to quit): ")
        if not check_qualification(last_name):
            break

if __name__ == "__main__":
    main()
