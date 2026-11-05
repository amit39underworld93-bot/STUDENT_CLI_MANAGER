from student_manager import (
    add_student, 
    view_student, 
    search_student,
    update_student, 
    delete_student,
    add_marks, 
    view_marks,
    calculate_result,
    update_marks, 
    view_subjects,
    add_subjects, 
    update_subject
)

def main():
    while True:
        print("\n")
        print("=" * 40)
        print("         STUDENT CLASS MANAGER")
        print("=" * 40)

        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Add marks")
        print("7. View student's marks")
        print("8. Calculate result")
        print("9. Update marks")
        print("10. View all subjects")
        print("11. Add subject")
        print("12. Update subject")
        print("13. Exit")

        choice = input("\nEnter your choice between 1 to 13: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()
        
        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            view_marks()

        elif choice == "8":
            calculate_result()

        elif choice == "9":
            update_marks()

        elif choice == "10":
            view_subjects()

        elif choice == "11":
            add_subjects()

        elif choice == "12":
            update_subject()

        elif choice == "13":
            break   

        else:
            print("Something went wrong please enter a valid choice!!!")

main()