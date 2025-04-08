def list_record(): #TODO BUENACIFRA
def add_student(): #TODO BERNAS
def update_record(): #TODO BUENACIFRA
def delete_record(): #TODO TERO
def search_record(): #TODO ROLDAN
    
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
            
