name = input("What's your name?: ")
phone = input("What's your phone number? [without +]: ")
country = input("Country of birth: ")
gender = input("Gender [male/female]: ")
year_birth = int(input("Year of birth: "))
type_student = input("Profession?[student/working]")

score = 0
for i in range(1, 5):
    score += float(input(f"Score in quizz {i}: "))

has_20 = (2020 - year_birth) > 20

is_african = country.lower() in ["uganda", "kenya", "mozambique", "nigeria"]
is_student = type_student.lower() == "student"

is_female = gender.lower() == "female"
is_male = gender.lower() == "male"

avg_score = score / 4
startwith_25 = phone.startswith("25")

if is_african and is_female and has_20 and startwith_25 and avg_score >= 75:
    print("You qualify for a sholarship.")
elif is_african and is_male and has_20 and startwith_25 and avg_score >= 80:
    print("You qualify for a sholarship.")
else:
    print("You don't meet the treshold.")
"""
if type_student not in ["yes", "no"]:
  exit("You provided an invalid number")

try:
except:
  exit("You provided an invalid year of birth. Try again.")
"""