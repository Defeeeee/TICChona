from typing import List

class Nota:
    def __init__(self, nota: any):
        self.nota = nota

    def isaprobado(self):
        if not self.nota.isdigit():
            return self.isaprobado_letras()
        else:
            self.nota = int(self.nota)
        if self.nota >= 6:
            return True, self.nota
        else:
            return False, self.nota
    def isaprobado_letras(self):
        match self.nota:
            case "A+":
                return True, self.nota
            case "A":
                return True, self.nota
            case "B":
                return True, self.nota
            case "C":
                return False, self.nota

notas: List[Nota] = [
    Nota(input("Ingrese la nota 1: ")),
    Nota(input("Ingrese la nota 2: ")),
    Nota(input("Ingrese la nota 3: ")),
]

notasaprobadas: List[int, str] = []

nota: int
for notaa in notas:
    ap: tuple[bool, any(str, int)] = notaa.isaprobado()
    if ap[0]:
        notasaprobadas.append(ap[1])

print("Notas aprobadas: ", notasaprobadas)



