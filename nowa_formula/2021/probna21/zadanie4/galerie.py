file = open("galerie_przyklad.txt").read()

countries = []
countries_counter = []
for lines in file:
    lines = lines.strip()
    country, city, *nums = lines.split()
    countries.append(country)
    
print(countries)