import inflect  # Used for converting numbers to word-based ordinals
p = inflect.engine()

cat_names = []

while True:
    ordinal = p.number_to_words(p.ordinal(len(cat_names) + 1))
    print(f'Enter the name of the {ordinal} cat (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names += [name]

print('The cat names are:')
for name in cat_names:
    print(name)

