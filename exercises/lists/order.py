people = [{
    'name': 'Paulo',
    'age': 21
}, {
    'name': 'Cristolde',
    'age': 28
}, {
    'name': 'Mabasso',
    'age': 27
}, {
    'name': 'Lucas',
    'age': 23
}]


def name(person):
    return person.get('name')


def age(person):
    return person.get('age')


print()
people.sort(key=name)
print(people)

print()
people.sort(key=age)
print(people)

print()
people.sort(key=age, reverse=True)
print(people)