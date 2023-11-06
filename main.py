todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith('add'):
        if len(user_action) > 4:
            todo = user_action[4:] + '\n'
        else:
            todo = input("Enter a to-do: ") + "\n"
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo)
        with open('todo.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.lower().strip() == 'show':
        with open('todo.txt', 'r') as file:
            print(file.read())
    elif user_action.startswith('edit'):
        number = int(input("Number of the to-do to edit: "))
        existing_todo = todos[number]
        print("You will edit: ", existing_todo)
        new_todo = input("new to-do: ")
        todos[number] = new_todo
    elif user_action.startswith('complete'):
        number = int(input("Number of the completed to-do: "))
        print("You will remove ", todos[number], "from the list.")
        confirm = input("Proceed? (y/n)")
        match confirm:
            case "y" | "yes" | "1":
                todos.pop(number)
    elif user_action.startswith('exit'):
        break
    else:
        print("You entered an unexpected command. No action was taken.")
        continue
print("Bye!")
