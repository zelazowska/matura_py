import math
from collections import Counter

temp = open("punkty.txt")
file = temp.readlines()
temp.close()
results = open("wyniki4.txt", "w")


def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    
def getDistance(x1, x2, y1, y2):
    distance = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
    return distance

#4.1
counter = 0

for lines in file:
    x, y = lines.split(" ")
    if isPrime(int(x)) and isPrime(int(y)):
        counter+=1
        
results.write(f"ZADANIE 4\n\nZadanie 4.1\nPunktow, gdzie obie wspolrzedne to liczby pierwsze: {counter}\n\n")

#4.2
twin_points = 0

for lines in file:
    x, y = lines.split(" ")
    if(Counter(x).keys() == Counter(y).keys()):
        twin_points += 1

results.write(f"Zadanie 4.2\nPunktow o wspolrzednych cyfropodobnych: {twin_points}\n\n")

#4.3
point_a = None
point_b = None
longest_distance = 0
distance = 0
points = []

for lines in file:
    lines = lines.strip("\n")
    a = lines.split(" ")
    points.append((int(a[0]), int(a[1])))
#naive 
for x in points:
    for y in points:
        distance = getDistance(x[0], y[0], x[1], y[1])
        if distance > longest_distance:
            longest_distance = round(distance)
            point_a = x
            point_b = y

results.write(f"Zadanie 4.3\nPunkty: {point_a} {point_b}, odleglosc: {longest_distance}\n\n")     

#4.4
inside = 0
edges = 0
outside = 0
square = []
for lines in file:
    lines = lines.strip("\n")
    a = lines.split(" ")
    square.append((int(a[0]), int(a[1])))
    
for points in square:
    if points[0] == 5000 and points[1] <= 5000 or points[0] <= 5000 and points[1] == 5000:
        edges+=1
    elif points[0] < 5000 and points[1] < 5000:
        inside+=1
    else:
        outside+=1
        
results.write(f"Zadanie 4.4\nWewnatrz:{inside}\nNa bokach:{edges}\nNa zewnatrz:{outside}") 

    



results.close()
