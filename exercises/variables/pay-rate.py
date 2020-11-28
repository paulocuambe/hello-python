name = input("Hello, there! What's your name? ")
print("Hello " + name + "! Nice to meet you.")

hours = float(input("How many hours did you work? "))
rate_per_hour = float(input("What is you pay rate per hour? "))
pay = hours * rate_per_hour

print(name, "the payment of your work will be of", pay, "MT")