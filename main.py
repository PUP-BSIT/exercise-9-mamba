all_records = []

def list_record():
    print("\nList Student Records")
    for record in all_records:
        print(f"\nName: {record['name']}")
        print(f"Age: {record['age']}")  
        print(f"Year & Section: {record['year & section']}")    
        print(f"Course: {record['course']}")  
        print(f"Student ID: {record['student_id']}")
        print("\nAll records listed successfully.")
    if not all_records:
        print("\nNo records found.")

def add_student():
    print("\nAdd Student Record")
    name = input("\nName: ")
    age = int(input("Age: "))
    year_section = input("Year & Section: ")
    course = input("Course: ")
    student_id = input("Enter Student ID: ")
    record = {
        "name": name,
        "age": age,
        "year & section": year_section,
        "course": course,
        "student_id": student_id,
    }
    all_records.append(record)
    print("\nStudent record added successfully.")

    
def update_record():
    print("\nUpdate Student Record")
    student_id = input("\nEnter Student ID to update: ")
    for record in all_records:
        if record['student_id'] == student_id:
            record['name'] = input("\nName: ")
            record['age'] = input("Age: ")
            record['year & section'] = input("Year & Section: ")
            record['course'] = input("Course: ")  
            
            print(f"\nRecord for {student_id} updated successfully.")
        print("\nRecord not found.")
    
def delete_record():
    print("\nDelete Student Record")
    target_id = int(input("\nEnter Student ID to delete: "))
    for record in all_records:
        if record["student_id"] == target_id:
            print(f"\nDeleting record: {record}")
            all_records.remove(record)
            print("\nRecord deleted.")
            return
            
        print("\nRecord not found.")

def search_record(): 
    search_id = input("\nEnter a Student ID: ")
    for record in all_records:
        if record["student_id"] == search_id:
            print(f"\nName: {record['name']}")
            print(f"Age: {record['age']}")
            print(f"Year & Section: {record['year & section']}")
            print(f"Course: {record['course']}")
            print(f"Student ID: {record['student_id']}")
            return
        print("\nNo matching records found.")
    
def main_menu(): 
    while True:
        print("\nStudent Record Management System\n")
        print("1. List All Student Records")
        print("2. Add Student Record")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Search Student Record")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        
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

