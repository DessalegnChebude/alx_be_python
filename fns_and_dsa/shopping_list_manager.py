def display_menu():
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            items = input("Enter the item to add:").lower()
            shopping_list.append(items)
            print(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            user_input = input("Enter your shoping item. ").lower()
            if user_input in shopping_list:
                shopping_list.remove(user_input)
                print(f"shopping_list: {shopping_list}")
            else:
                print("Item doesn't exist in the shoping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Shoping list is empty")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f'{index}. {item}')
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()