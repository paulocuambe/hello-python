try:
    hours = float(input("How many hours did you work?\n"))
    rate = float(input("What is you pay rate per hour?\n"))

    # Give the employee 1.5 times the hourly rate for hours worked above 40 hours
    if hours > 160:
        extra_hours = hours - 160
        pay = (hours - extra_hours) * rate + extra_hours * rate * 1.5
    else:
        pay = hours * rate

    print("The payment of your work will be of", pay, "MT")
except:
    print("Error. Please enter a numeric input.")
