user_input = input("Add a new member: ")

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append(user_input + "\n")

file = open("members.txt", "w")
members = file.writelines(members)
file.close()

file = open("members.txt", "r")
print(file.read())
file.close()