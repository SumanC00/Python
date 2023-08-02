while True:
    user_action = input("Type add, display or show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("files/subfiles/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/subfiles/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open("files/subfiles/todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index + 1}- {item}"
                print(row)
            #print(len(todos)) length function to print the length of something
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        #case _:
            #print("Hey, you entered an unknown command")

print("Bye!")