def get_todos():
    with open("files/subfiles/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    # Get user input and strip space characters from the input ex. hi  removes the space after hi
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        # todo = input("Enter a todo: ") + "\n"

        # file = open("files/subfiles/todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        todos.append(todo)

        # file = open("files/subfiles/todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        with open("files/subfiles/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        # file = open("files/subfiles/todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        # | "display" to have two

        todos = get_todos()

        # new_todos = []

        # for item in todos:
        # new_item = item.strip("\n")
        # new_todos.append(new_item)

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            row = f"{index + 1}- {item}"
            print(row)

        # print(len(todos)) length function to print the length of something

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])  # int(input("Number of the todo to edit: "))
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("files/subfiles/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Try to input an integer")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])  # int(input("Number of the todo to complete: "))

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("files/subfiles/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Your input is out of the index.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

    # case _:
    # print("Hey, you entered an unknown command")

print("Bye!")
