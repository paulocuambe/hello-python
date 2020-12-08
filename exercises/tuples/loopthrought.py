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

for person in people:
    [_, name], [_, age] = person.items()
    print(name, age)

print('\n---Tradutor---')
words = {'hello': 'olá', 'buy': 'comprar', 'list': 'lista'}
# .items() changes key pair values to tuples in a dict_items structure
for en, pt in words.items():
    print(en, pt, sep=' -> ')
