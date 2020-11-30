maximum = minimun = None
count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break

    try:
        number = float(user_input)
        if count == 0:
            maximum = number
            minimum = number
        elif number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number

        count += 1
    except:
        print(" Invalid input")

print("Max:", maximum)
print("min:", minimum)
print("Count:", count)