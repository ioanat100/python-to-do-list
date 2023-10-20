todos = []

while True:
    user_action=input("Type add, show, edit or exit: ")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo=input("Enter a to-do: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the to-do to edit: "))
            existing_todo=todos[number]
            print("You will edit: ", existing_todo)
            new_todo=input("new to-do: ")
            todos[number]=new_todo
        case 'exit':
            break

print("Bye!")