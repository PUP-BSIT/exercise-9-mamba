all_records = []

def list_records():
    print("\nList Student Records")
    for record in all_records:
        print(f"\nName: {record['name']}")
        print(f"Age: {record['age']}")  
        print(f"Year & Section: {record['year & section']}")    
        print(f"Course: {record['course']}")  
        print(f"Student ID: {record['student_id']}")

    if not all_records:
        print("\nNo records found.")
    else:
        print("\nAll records listed successfully.")

def add_student():
    print("\nAdd Student Record")
    name = input("\nName: ")
    age = input("Age: ")
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
    is_found = False
    student_id = input("\nEnter Student ID to update: ")

    for record in all_records:
        if record['student_id'] == student_id:
            record['name'] = input("\nNew Name: ")
            record['age'] = input("New Age: ")
            record['year & section'] = input("New Year & Section: ")
            record['course'] = input("New Course: ")  
            print(f"\nRecord for {student_id} updated successfully.")
            is_found = True
            break

    if not is_found:
        print("\nRecord not found.")
    
def delete_record():
    print("\nDelete Student Record")
    is_found = False
    target_id = input("\nEnter Student ID to delete: ")

    for record in all_records:
        if record["student_id"] == target_id:
            all_records.remove(record)
            print("\nRecord deleted.")
            is_found = True
            break

    if not is_found:
        print("\nRecord not found.")

def search_record(): 
    print("\nSearch Student Record")
    is_found = False
    search_id = input("\nEnter a Student ID: ")

    for record in all_records:
        if record["student_id"] == search_id:
            print(f"\nName: {record['name']}")
            print(f"Age: {record['age']}")
            print(f"Year & Section: {record['year & section']}")
            print(f"Course: {record['course']}")
            print(f"Student ID: {record['student_id']}")
            is_found = True
            break

    if not is_found:
        print("\nRecord not found.")
    
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
                list_records()
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

