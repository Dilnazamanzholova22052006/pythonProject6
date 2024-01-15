def mix_colors(col1, col2):
    if (col1 == "red" and col2 == "blue") or (col1 == "blue" and col2 == "red"):
        return "purple"
    elif (col1 == "red" and col2 == "yellow") or (col1 == "yellow" and col2 == "red"):
        return "orange"
    elif (col1 == "blue" and col2 == "yellow") or (col1 == "yellow" and col2 == "blue"):
        return "green"
    else:
        return "color error"
col1 = input("Enter the first color(red, blue, or yellow): ").lower()
col2 = input("Enter the second color (red, blue, or yellow): ").lower()
result = mix_colors(col1, col2)
print(result)
