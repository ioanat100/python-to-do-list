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
            todos = file.readlines()
        for i,todo in enumerate(todos):
            print(f"{i+1}. {todo.strip()}")
    elif user_action.lower().startswith('edit'):
        # find out what we're editing
        if len(user_action) > 5:
            number = int(user_action[5:])
        else:
            number = int(input("Number of the to-do to edit: "))
        with open("todo.txt", "r") as file:
            todos = file.readlines()
        existing_todo = todos[number - 1]
        confirmation = input(f"You will edit: {existing_todo}. Continue? (y/n)")
        try:
            if confirmation == "y" or confirmation == "yes" or confirmation == 1:
                new_todo = input("new to-do: ")
                todos[number] = new_todo + "\n"
                with open('todo.txt', 'w') as file:
                    file.writelines(todos)
            elif confirmation == "n" or confirmation == "no" or confirmation == 0:
                print("Understood. No changes were made.")
                continue
        except:
            print("You entered an unexpected command. No action was taken")
            continue
    elif user_action.startswith('complete'):
        number = int(input("Number of the completed to-do: "))
        with open('todo.txt','r') as file:
            todos = file.readlines()
        print("You will remove ", todos[number - 1], "from the list.")
        confirm = input("Proceed? (y/n)")
        if confirm == "y" or confirm == "yes" or confirm == "1":
            todos.pop(number - 1)
            with open('todo.txt', 'w') as file:
                for todo in todos:
                    file.writelines(todo)
        else:
            print("No action was taken")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("You entered an unexpected command. No action was taken.")
        continue
print("Bye!")
