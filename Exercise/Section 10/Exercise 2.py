try:
    total_value = float(input("Enter total value"))
    value = float(input("Enter Value"))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ZeroDivisionError:
    exit(f"Your total value cannot be zero.")
