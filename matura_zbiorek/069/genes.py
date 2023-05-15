from collections import Counter

temp = open("dane_geny.txt")
file = temp.read().split()

species = []
for genes in file:
    genes = genes.rstrip()
    species.append(len(genes))

print(len(Counter(species).values()))