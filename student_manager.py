def add_student(students):
    name = input("Enter student name: ")
    try:
        marks = float(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print("Student added!\n")
    except ValueError:
        print("Invalid marks.\n")


def show_students(students):
    if not students:
        print("\nNo student records available.\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"{s['name']} - {s['marks']}")
    print()


def calculate_average(students):
    if not students:
        print("No data available.\n")
        return

    avg = sum(s["marks"] for s in students) / len(students)
    print(f"Average Marks: {avg:.2f}\n")


def highest_lowest(students):
    if not students:
        print("No data available.\n")
        return

    highest = max(students, key=lambda x: x["marks"])
    lowest = min(students, key=lambda x: x["marks"])

    print(f"Highest: {highest['name']} ({highest['marks']})")
    print(f"Lowest: {lowest['name']} ({lowest['marks']})\n")


def menu():
    students = []

    while True:
        print("==== Student Manager ====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Calculate Average")
        print("4. Highest & Lowest")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            highest_lowest(students)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.\n")


menu()
