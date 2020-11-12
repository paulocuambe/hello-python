name = "Mukhera"
age = 21
salary = 100.0

print("Hi, my name is", name, "and I'm ", age, "years old.")
print("My base salary is", salary)

# Let's try other types of concatenating
sentence = "\nHi " + name + ", I'm glad to see you here!\n" + "You're so young, just " + str(
    age) + " and earning " + str(salary) + "$/hour."
print(sentence)

new_sentence = "Hi %s, I'm happy to see you again. You're %s years old right? \nI know a place that is hiring new talent and they are paying %s$/day."
print(new_sentence % (name, age, salary))

# Mass assignment
print("\n----- Mass Assignment below -----")
a, b, c = 1, 2, 4
print(a, b, c)

e = r = t = 9
print(e, r, t)