prompt = "Enter a to-do: "

todos = []

while True:
    todo = input(prompt)
    print(todo.capitalize())
    todos.append(todo)