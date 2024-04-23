from typing import List

lis1: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lis2: List[List[int]] = [[], [], []]

for lista in lis1:
    for x in lista:
        lis2[lis1.index(lista)].append(x**2)

print(lis2)