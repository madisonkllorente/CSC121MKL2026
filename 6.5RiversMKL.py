#6.5 rivers MKL

rc = {
    'Nile':'Egypt',
    'Thames':'England',
    'Saint Lawrence': 'Canada',
}

for river, country in rc.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

print("Rivers Dictionary:")
for river in rc.keys():
    print(river.title())

print()

print("Country Dictionary:")
for country in rc.values():
    print(country.title())