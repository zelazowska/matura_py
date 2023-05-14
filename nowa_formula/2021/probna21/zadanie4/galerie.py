temp = open("galerie.txt")
file = temp.readlines()
temp.close()

results1 = open("wyniki4_1.txt", "w")
results2a = open("wyniki4_2a.txt", "w")
results2b = open("wyniki4_2b.txt", "w")
results3 = open("wyniki4_3.txt", "w")

#4.1
countries = []
for lines in file:
    lines = lines.rstrip().split()
    country, city, gallery = lines[0], lines[1], lines[2:]
    countries.append(country)

results1.write("4.1\n")
for country in countries:
    results1.write(f"{country} {countries.count(country)}\n")
    
#4.2a
results2a.write("4.2a\n")
results2b.write("4.2b\n")
biggest_area_city = ''
smallest_area_city = ''
biggest_area = 0
smallest_area = 1000000000009
#4.2b
max_locals_city = ''
min_locals_city = ''
max_locals = 0
min_locals = 1000000000009

for lines in file:
    lines = lines.rstrip().split()
    country, city, gallery = lines[0], lines[1], lines[2:]
    galleries = []
    total_area = 0 
    areas = set()
       
    counter = 0
    for number in gallery:
        if number != '0':
            counter += 1
            galleries.append(int(number))
    
    area = 0
    for i in range(1, len(galleries),2):
        area = galleries[i-1]*galleries[i]
        total_area += area
        areas.add(area)
        
    #4.2b
    if total_area < smallest_area:
        smallest_area_city = city
        smallest_area = total_area

    if total_area > biggest_area:
        biggest_area_city = city
        biggest_area = total_area
    
    #4.3
    if len(areas) < min_locals:
        min_locals_city = city
        min_locals = len(areas)

    if len(areas) > max_locals:
        max_locals_city = city
        max_locals = len(areas)
        
    
    results2a.write(f"{city} {total_area} {int(counter/2)}\n")
results2b.write(f"{biggest_area_city} {biggest_area}\n{smallest_area_city} {smallest_area}")
results3.write(f"4.3\n{max_locals_city} {max_locals}\n{min_locals_city} {min_locals}")
    
results1.close()
results2a.close()
results2b.close()
results3.close()