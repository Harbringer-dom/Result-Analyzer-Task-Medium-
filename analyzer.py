def get_grade(marks):
    #Deciding the grade based on the marks range
    """
    Return grade based on marks
    A : 90-100
    B : 70-89
    C : below 69
    """
    
    # Conditions
    if 90 <= marks <= 100:
        return 'A'
    elif 70 <= marks < 89:
        return 'B'
    else:
        return 'C'


def enter_students():
    # Enter student details(name and marks)
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Student name: ")
        marks = float(input("Marks: "))
        students.append({"name": name, "marks": marks})
    return students


def analyze_marks(students):
    # Analyze the marks to find highest,lowest,average,passed and failed
    highest = students[0]
    lowest = students[0]
    average = sum(s["marks"] for s in students) / len(students)
    passed = sum(1 for s in students if s["marks"] >= 40)
    failed = len(students) - passed

    for s in students:
        if s["marks"] > highest["marks"]:
            highest = s
        if s["marks"] < lowest["marks"]:
            lowest = s

    return highest, lowest, average, passed, failed


def main():
    students = enter_students()
    highest, lowest, average, passed, failed = analyze_marks(students)
    print("Student Analysis: ")
    print(f"Highest: {highest['name']} ({highest['marks']})")
    print(f"Lowest: {lowest['name']} ({lowest['marks']})")
    print(f"Average: {average}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    for student in students:
        print(f"{student['name']}: {get_grade(student['marks'])}")


if __name__ == "__main__":
    main()

