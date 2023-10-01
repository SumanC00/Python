def get_average():
    with open("files/data.txt", 'r') as file:  # opens file from files directory in same folder as bonus11.py
        data = file.readlines()  # [1:]        # Reads all the lines in txt file as separate items, [1:] will not read 0

    values = data[1:]       # does the removing of first line but separate so easier to see
    values = [float(i) for i in values]

    average_local = sum(values) / len(values) # adds values and divides by amount
    return average_local  # returns the data, which is the items in txt file besides first item (which is 0)


average = get_average()  # set the definition to the avg variable
print(average)  # print avg variable
