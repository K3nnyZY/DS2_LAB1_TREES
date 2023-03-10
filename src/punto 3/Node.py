class Estudiante:
    def __init__(self, id, nombre, promedio):
        self.id = id
        self.nombre = nombre

        self.promedio = promedio
    def __str__(self):
        return f"Estudiante {self.id}: {self.nombre}, promedio: {self.promedio}"

class Node:
    def __init__(self, leaf=True):
        self.keys = [] 
        self.children = [] 
        self.leaf = leaf

    def __str__(self):
        return str(self.keys) 