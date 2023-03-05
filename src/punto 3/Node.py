class BNode:
    def __init__(self, t):
        self.t = t  # grado mínimo del árbol
        self.ids = []  # lista de IDs de estudiantes
        self.nombres = []  # lista de nombres de estudiantes
        self.promedios = []  # lista de notas de estudiantes
        self.children = []  # lista de punteros a los hijos
        
    def is_leaf(self):
        return len(self.children) == 0
