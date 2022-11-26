## Zadanie 1. 
### Wiązka zadań Ciągi rekurencyjne

1.1 


    |i 	|wynik(i)|
    |-------|--------|
    |2      |   1    |
    |3	|   1    |
    |4 	|   3    |
    |5 	|   3    |
    |6 	|   5    |
    |7	|   5    |
    |8 	|   9    |
   
1.2


    |i      | E(i)|
    |-------|-----| 
    |0	| 1   |
    |3	| 1   |
    |5	| 2   |
    |7	| 3   |   
    |9	| 5   |
    |10	| 8   |

    E(0) = E(1) = E(2) = 1 
    E(i) = E(i-3) + E(i-1) dla parzystego i > 2 
    E(i) = E(e-1) 	       dla nieparzystego i > 2

1.3 
   
    W[0] ← 1 
    W[1] ← 1 
    W[2] ← 1 
    max_wart ← 1 
    dla i = 3, 4, …, 1 000 wykonuj 
        jeżeli i mod 2 = 0 
            W[i] ← W[i-3] + W[i-1] + 1
        w przeciwnym razie 
            W[i] ← W[i-1] mod 7
        jeżeli W[i] > max_wart
            W[i] ← max_wart
    zwróć max_wart
    

## Zadanie 2. 
### Wiązka zadań Ułamki dwójkowe

2.1


    | Kolejne wykonanie (*)| Wartość zmiennej y |
    |----------------------|--------------------|
    |           1 	       |        0,2         |
    |           2	       |        0,4         |
    |           3 	       |        0,8         |
    |           4 	       |        0,6         |
    |           5 	       |        0,2         |
    Liczba wypisana przez algorytm: 0,10011

2.2
    1. Podaj przykład liczby x, dla której po wykonaniu funkcji binarny(x,4) zmienna y ma wartość 0, a po wykonaniu funkcji binarny(x, 3) zmienna y nie jest równa 0.
        - x = 0,0625
            - WYJAŚNIENIE: dla iteracji nr. 4 liczba y przed porównaniem z 1 musi być równa 1, dlatego x = 0,0625 (bo przy zakończeniu 4 iteracji wyniesie 1, wówczas y=y-1 => y=1-1=0, a dla 3 iteracji wyniesie 0,5, (bo y=0,5 <= 1))

2.3
    FIX NEEDED

## Zadanie 3. 
### Wiązka zadań  Ciekawe mnożenia


## 1.4 TEST Z OGÓLNEJ WIEDZY INFORMATYCZNEJ

44.
    100110010
    - 2+16+32+256 = 306

    10011001
    - 1+8+16+128 = 153 

    1001100100
    - 4+32+64+512 = 612

    472(8)
    - 2+56+256 = 314 

    P P F P 

56.
    P F P F

57.
    P P F P
