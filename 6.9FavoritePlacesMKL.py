#6.9 FavoritePlaces MKL

fp = {
    'Nataile':['France', 'Dillards'],
    'Miggy':['Miyako House', 'Church'],
    'Madison': ['Movie Theater', 'Thrift Store'],
}

for name, places in fp.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")

print()

print("Name Dictionary:")
for name in fp.keys():
    print(name.title())

print()

print("Places Dictionary:")
for places in fp.values():
    for place in places:
        print(place.title())
