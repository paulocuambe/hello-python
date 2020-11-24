try:
    a = "211312" * 1 + 45562
    print(a**2)
except:
    print("Something unexpected occured.")

try:
    age = int(input("How old are you? "))

    if age <= 15:
        print("You cannot pass from here.")
    elif age < 18:
        print("You can only pass with an adult.")
    elif age <= 25:
        print("You're allowed to pass and enjoy all our amazing gadgets.")
    else:
        print(
            "You're allowed to pass and enjoy all our amazing gadgets. Use RXGAN71 code to enjoy free meals."
        )
except:
    print("I guess that the age you provided is not a valid one.")
