total = count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break

    try:
        number = float(user_input)
        total += number
        count += 1
    except:
        print("Invalid Input")

print(total, count, total / count)
