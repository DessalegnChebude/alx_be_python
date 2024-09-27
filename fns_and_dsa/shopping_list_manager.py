def display_menu():
    print("Shoping List Manager")
    print("1, Add Item")
    print("2, Remove Item")
    print("3, View List")
    print("4, Exit")

def main():
    shoping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()
        if choice == "1":
            items = input("Enter your shoping itme. ").lower()
            shoping_list.append(items)
            print(shoping_list)
        elif choice == "2":
            user_input = input("Enter your shoping item. ").lower()
            if user_input in shoping_list:
                shoping_list.remove(user_input)
                print(f"Shoping_List: {shoping_list}")
            else:
                print("Item doesn't exist in the shoping list.")
        elif choice == "3":
            if len(shoping_list) == 0:
                print("Shoping list is empty")
            else:
                for item in shoping_list:
                    print(item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()