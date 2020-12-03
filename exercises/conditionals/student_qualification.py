name = input("What's your name?: ")
phone = input("What's your phone number? [without +]: ")
country = input("Country of birth: ")
gender = input("Gender [male/female]: ")
year_birth = int(input("Year of birth: "))
type_student = input("Studying or working? [student/working]: ")

print()
score = 0

for i in range(1, 5):
    score += float(input(f"Your score in quizz {i}: "))

has_20 = (2020 - year_birth) > 20
startwith_25 = phone.startswith("25")

is_african = country.lower() in ["uganda", "kenya", "mozambique", "nigeria"]
is_student = type_student.lower() == "student"

is_female = gender.lower() == "female"
is_male = gender.lower() == "male"

avg_score = score / 4

print()

if not is_student:
    print("You don't meet the treshold")
    exit()

if is_african and is_female and has_20 and startwith_25 and avg_score >= 75:
    print("You qualify for a sholarship.")
elif is_african and is_male and has_20 and startwith_25 and avg_score >= 80:
    print("You qualify for a sholarship.")
else:
    print("You don't meet the treshold.")