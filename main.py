todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index} - {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the to-do to edit: "))
            existing_todo = todos[number]
            print("You will edit: ", existing_todo)
            new_todo = input("new to-do: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the completed to-do: "))
            print("You will remove ", todos[number], "from the list.")
            confirm = input("Proceed? (y/n)")
            match confirm:
                case "y" | "yes" | "1":
                    todos.pop(number)
        case 'exit':
            break

print("Bye!")
