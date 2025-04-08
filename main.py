all_records = []

def list_record(): #TODO BUENACIFRA

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    year_section = input("Year and Section:")
    course = input("Course:")
    student_id = input("Enter Student ID: ")
    record = {
        "Name": name,
        "Age": age,
        "Year and Section: ": year_section,
        "Course": course,
        "Student ID": student_id,
    }
    all_records.append(record)
    print("Student Record added Successfully")

    
def update_record(): #TODO BUENACIFRA
    
def delete_record(): #TODO TERO
        print("\nDelete Student Record")
        target_id = int(input("Enter Student ID to delete: "))
        for i, record in enumerate(records):
            if record["id"] == target_id:
                print(f"Deleting record: {record}")
                del records[i]
                print("Record deleted.")
                return
        print("Record not found.")

def search_record(): #TODO ROLDAN
    search_term = input("Enter a student name: ").lower()
    found_records = False 

    for record in student_records:
        if search_term in str(record).lower():
            print(record)
            found_records = True

    if not found_records:
        print("No matching records found.")
    
def main_menu(): 
    while True:
        print("\nStudent Record Management System")
        print("1. List All Student Records")
        print("2. Add Student Record")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Search Student Record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_record()
            case "2":
                add_student()
            case "3":
                update_record()
            case "4":
                delete_record()
            case "5":
                search_record()
            case "6":
                print("Exiting...")
                break
            
main_menu()
            
