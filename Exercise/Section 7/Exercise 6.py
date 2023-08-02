filenames = ["doc.txt", "report.txt", "presentation.txt"]

#content = "Hello"

#for contents, file, in zip(content, filenames):
#    file = open(f"{file}", "w")
#    file.write(content)
#    file.close()

for filename in filenames:
    file = open(filename, "w")
    file.write("Hello")
    file.close()