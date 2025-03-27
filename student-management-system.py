# Student Management System using OOPs, Exception Handling, and File Handling

class Student:
    """Class to represent a Student with ID, Name, and Courses."""
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses

    def display_info(self):
        """Return student details as a formatted string."""
        return f"ID: {self.id}, Name: {self.name}, Courses: {', '.join(self.courses)}"

    def update_name(self, new_name):
        """Update the student's name."""
        self.name = new_name

    def update_courses(self, new_courses):
        """Update the courses of the student."""
        self.courses = new_courses


# Dictionary to store students (key: ID, value: Student object)
students_db = {}

print("===== WELCOME TO STUDENT MANAGEMENT SYSTEM =====")

while True:
    print('''
    1. Add Student
    2. View All Students
    3. Search Student by ID
    4. Update Student Details
    5. Delete Student
    6. Exit
    ''')
    
    try:
        choice = int(input("Enter your choice: "))  # Get user input
        
        # 1️⃣ Add a New Student
        if choice == 1:
            id = int(input("Enter Student ID: "))
            
            if id in students_db:  # Prevent duplicate ID
                print("❌ Student ID already exists!")
                continue
            
            name = input("Enter Student Name: ")
            courses = input("Enter Courses (comma-separated): ").split(",")
            
            students_db[id] = Student(id, name, courses)  # Add student to dictionary
            print("✅ Student Added Successfully!")

        # 2️⃣ View All Students
        elif choice == 2:
            if not students_db:  # Check if student database is empty
                print("⚠️ No students available!")
            else:
                print("\n--- Student List ---")
                for student in students_db.values():
                    print(student.display_info())

        # 3️⃣ Search Student by ID
        elif choice == 3:
            id = int(input("Enter Student ID to Search: "))
            student = students_db.get(id)  # Get student object from dictionary
            
            if student:
                print("✅ Student Found:", student.display_info())
            else:
                print("❌ Student Not Found!")

        # 4️⃣ Update Student Details
        elif choice == 4:
            id = int(input("Enter Student ID to Update: "))
            student = students_db.get(id)
            
            if student:
                print("\n1. Update Name\n2. Update Courses")
                update_choice = int(input("Enter your choice: "))
                
                if update_choice == 1:
                    new_name = input("Enter New Name: ")
                    student.update_name(new_name)
                    print("✅ Name Updated Successfully!")
                
                elif update_choice == 2:
                    new_courses = input("Enter New Courses (comma-separated): ").split(",")
                    student.update_courses(new_courses)
                    print("✅ Courses Updated Successfully!")
                
                else:
                    print("❌ Invalid Choice!")
            else:
                print("❌ Student Not Found!")

        # 5️⃣ Delete Student
        elif choice == 5:
            id = int(input("Enter Student ID to Delete: "))
            
            if id in students_db:
                del students_db[id]  # Remove student from dictionary
                print("✅ Student Deleted Successfully!")
            else:
                print("❌ Student Not Found!")

        # 6️⃣ Exit the Program
        elif choice == 6:
            print("✅ Exited Successfully!")
            break  # Terminate the loop

        else:
            print("❌ Invalid Choice! Please enter a number between 1-6.")

    except ValueError:
        print("❌ Invalid Input! Please enter a valid number.")
