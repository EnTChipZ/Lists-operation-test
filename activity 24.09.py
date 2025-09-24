my_list=[]

def parse_value(s):
    s=s.strip()
    if s=="":
        return s
    if s.lower()=="true":
        return True
    if s.lower()=="false":
        return False
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s

while True:
    print("Choose a number to perform operation on list")
    print("1. Append")
    print("2. Insert")
    print("3. Remove")
    print("4. Pop")
    print("5. Clear")
    print("6. Index")
    print("7. Count")
    print("8. Sort")
    print("9. Reverse")
    print("10. View List")
    print("11. View List Data and Data type")
    print("12. Exit")

    userinput = input("Enter your choice: ")
    try:
        choice = int(userinput)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        while True:
            number_of_input = input("How many elements would you like to store: ")
            print(" -------------------------------")
            try:
                number_of_input=int(number_of_input)
                for _ in range(number_of_input):
                    element=input("Enter the element you want to store: ").strip()
                    while len(element)==0:
                        print("Sorry, we don't accept a blank input to be store in our list. Try again!")
                        element=input("Enter the element you want to store: ").strip()
                    my_list.append(parse_value(element))
                print(f"{number_of_input} element/s was already stored.")
                print("Exiting list operation number 1")
                print("-----------------------------------------------------\n")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == 2:
        while True:
            number_of_input = input("How many elements would you like to store: ")
            try:
                number_of_input = int(number_of_input)
                if number_of_input <= 0:
                    print("Please enter a positive number.")
                    continue

                for i in range(number_of_input):
                    element_to_be_store = input(f"Enter element #{i+1} to store: ").strip()
                    while len(element_to_be_store) == 0:
                        print("Sorry, we don't accept a blank input to be stored in our list. Try again!")
                        element_to_be_store = input(f"Enter element #{i+1} to store: ").strip()
                    element_val = parse_value(element_to_be_store)

                    while True:
                        element_index_number_position = input("Enter the index position you want to store the element: ")
                        try:
                            idx = int(element_index_number_position)
                            before_len = len(my_list)
                            my_list.insert(idx, element_val)
                            if idx >= before_len:
                                print(f"{element_val!r} was inserted at the end (index >= current length).")
                            else:
                                print(f"{element_val!r} was successfully inserted at index {idx}.")
                            break
                        except ValueError:
                            print("Invalid input. Please enter a position value in whole number.")

                print(f"{number_of_input} element/s was already stored.")
                print("Exiting list operation number 2")
                print("-----------------------------------------------------\n")
                break

            except ValueError:
                print("Invalid input. Please enter a number of elements you want to store.")

    elif choice == 3:
        while True:
            userinput = input("How many elements would you like to remove: ")
            try:
                userinput = int(userinput)
                if userinput > len(my_list):
                    print(f"The number of elements in your list is {len(my_list)}. You can't delete more than that.")
                    continue
                successful = 0
                for _ in range(userinput):
                    element = input("Enter element to be remove: ")
                    val = parse_value(element)
                    if val in my_list:
                        my_list.remove(val)
                        successful += 1
                    else:
                        print(f"{val} not found in the list.")
                print("Exiting list operation number 3")
                print("-----------------------------------------------------\n")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == 4:
        if len(my_list) == 0:
            print("List is empty! You can't pop an element from an empty list.")
        else:
            popped = my_list.pop()
            print("Popped element:", popped)
            print("Updated list:", my_list)
            print("Exiting list operation number 4")
            print("-----------------------------------------------------\n")

    elif choice == 5:
        my_list.clear()
        print("List cleared:", my_list)
        print("Exiting list operation number 5")
        print("-----------------------------------------------------\n")

    elif choice == 6:  # Index (fixed: parse search value; guard empty list)
        if not my_list:
            print("List is empty.")
        else:
            element_raw = input("Enter the element to find index: ")
            element = parse_value(element_raw)
            indices = [i for i, x in enumerate(my_list) if x == element]
            if indices:
                print(f"Element {element!r} these are the indices: {indices}")
            else:
                print(f"Element {element!r} not found in list.")
        print("Exiting list operation number 6")
        print("-----------------------------------------------------\n")

    elif choice == 7:
        element = input("Enter element to count: ")
        val = parse_value(element)
        print("Count of", val, ":", my_list.count(val))
        print("Exiting list operation number 7")
        print("-----------------------------------------------------\n")

    elif choice == 8:
        try:
            my_list.sort(key=lambda x: str(x))
            print("Sorted list:", my_list)
        except Exception as e:
            print("Could not sort list:", e)
        print("Exiting list operation number 8")
        print("-----------------------------------------------------\n")

    elif choice == 9:
        my_list.reverse()
        print("Reversed list:", my_list)
        print("Exiting list operation number 9")
        print("-----------------------------------------------------\n")

    elif choice == 10:
        print("Current list:", my_list)
        print("Exiting list operation number 10")
        print("-----------------------------------------------------\n")

    elif choice == 11:
        print("List contents:", my_list)
        print("Data type:", type(my_list))
        if my_list:
            print("Per-item types:")
            for i, v in enumerate(my_list):
                print(f"[{i}] {v!r} -> {type(v)}")
        print("Exiting list operation number 11")
        print("-----------------------------------------------------\n")

    elif choice == 12:
        print("Exiting list operation program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1-12.")
        continue
