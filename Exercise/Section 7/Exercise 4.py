#file = ["snail"]

#doc = ["file.txt"]

#for content, filename in zip(file, doc):
#    file = open(f"../Section 7/{filename}", "w")
#    file.write(content)
#    file.close()

with open("file.txt", "w") as file:
    file.write("snail")