def sumKwCyfr(n):
    suma = 0
    while n>0:
        cyfra = n%10
        suma += cyfra*cyfra
        n = n//10
    return suma
        

        

print(sumKwCyfr(123))