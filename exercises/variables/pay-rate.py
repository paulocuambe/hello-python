name = input("Hello, there! What's your name?\n")
print("Hello " + name + "! Nice to meet you.")

hours = float(input("How many hours did you work?\n"))
rate_per_hour = float(input("What is you pay rate per hour?\n"))
pay = hours * rate_per_hour

print(name, "the payment of your work will be of", pay, "MT")