from typing import List

lis: List[int] = [1, 2, 3, 4, 5]
nlis: List[int] = []

for x in lis:
    nlis.append(x**2)

print(nlis)