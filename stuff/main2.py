"""
Ejercicio:
    Dados los enteros l, k, n ingresados por consola
    Mostrar todos los enteros entre l y k (inclusive) que sean divisibles por n
"""

l: int = int(input("Ingrese el valor de l: "))
k: int = int(input("Ingrese el valor de k: "))
n: int = int(input("Ingrese el valor de n (divisor): "))

i: int
print(f"Los enteros entre {l} y {k} divisibles por {n} son:")
for i in range(l, k + 1):
    if i % n == 0:
        print(i)