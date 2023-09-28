while True:
    # Get user input and strip space characters from the input ex. hi  removes the space after hi
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        #todo = input("Enter a todo: ") + "\n"

        #file = open("files/subfiles/todos.txt", "r")
        #todos = file.readlines()
        #file.close()

        with open("files/subfiles/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        #file = open("files/subfiles/todos.txt", "w")
        #file.writelines(todos)
        #file.close()

        with open("files/subfiles/todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:
        #file = open("files/subfiles/todos.txt", "r")
        #todos = file.readlines()
        #file.close()
        #| "display" to have two

        with open("files/subfiles/todos.txt", "r") as file:
            todos = file.readlines()

        #new_todos = []

        #for item in todos:
            #new_item = item.strip("\n")
            #new_todos.append(new_item)

        #new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            row = f"{index + 1}- {item}"
            print(row)

        #print(len(todos)) length function to print the length of something

    elif 'edit' in user_action:
        number = int(user_action[5:]) #int(input("Number of the todo to edit: "))
        print(number)
        number = number - 1

        with open("files/subfiles/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("files/subfiles/todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:]) #int(input("Number of the todo to complete: "))

        with open("files/subfiles/todos.txt", "r") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("files/subfiles/todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was remove from the list."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid.")

    #case _:
        #print("Hey, you entered an unknown command")

print("Bye!")