def create_list(N):
    return [int(input(f"Enter element {i+1}: ")) for i in range(N)]

def display_list(list_):
    if list_:
        print("List elements:", list_)
    else:
        print("List is empty.")

def insert_element(list_):
    index = int(input("Enter index to insert element: "))
    if 0 <= index <= len(list_):
        element = int(input("Enter element to insert: "))
        list_.insert(index, element)
        print(f"Element {element} inserted at index {index}.")
    else:
        print("Invalid index.")

def delete_element(list_):
    index = int(input("Enter index to delete element: "))
    if 0 <= index < len(list_):
        deleted_element = list_.pop(index)
        print(f"Element {deleted_element} deleted from index {index}.")
    else:
        print("Invalid index.")

def main():
    list_ = []
    while True:
        print("\nMenu:")
        print("1. Create a list of N integers")
        print("2. Display the list elements")
        print("3. Insert an element at a specific index")
        print("4. Delete an element at a specific index")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            N = int(input("Enter the number of elements: "))
            list_ = create_list(N)
        elif choice == 2:
            display_list(list_)
        elif choice == 3:
            insert_element(list_)
        elif choice == 4:
            delete_element(list_)
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()