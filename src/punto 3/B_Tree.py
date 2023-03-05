from Node import BNode

class Tree:
    """
    Clase que representa un árbol B que almacena información de estudiantes de una universidad.
    """
    def __init__(self, t):
        """
        Inicializa un árbol B vacío con el grado mínimo especificado.

        parameters:
        --------------
        t (int): el grado mínimo del árbol
        """
        self.root = BNode(t)
        self.t = t
        

    def search(self, id):
        """
        Busca un estudiante por su número de identificación.

        parameters:
        --------------
        id (int): el número de identificación del estudiante a buscar
        --------------
        returns:
        Si se encuentra el estudiante, retorna una tupla con su nombre completo y promedio académico.
        Si no se encuentra el estudiante, retorna None.
        """
        return self._search(self.root, id)
    

    def _search(self, node, id):
        """
        Función auxiliar que realiza la búsqueda recursiva en el árbol.

        parameters:
        --------------
        node (BNode): el nodo actual de la búsqueda
        id (int): el número de identificación del estudiante a buscar
        --------------
        returns:
        Si se encuentra el estudiante, retorna una tupla con su nombre completo y promedio académico.
        Si no se encuentra el estudiante, retorna None.
        """
        i = 0
        while i < len(node.ids) and id > node.ids[i]:
            i += 1
        if i < len(node.ids) and id == node.ids[i]:
            return node.nombres[i], node.promedios[i]
        elif node.is_leaf():
            return None
        else:
            return self._search(node.children[i], id)
    

    def insert(self, id, nombre, promedio):
        """
        Inserta un nuevo estudiante en el árbol.

        parameters:
        --------------
        id (int): el número de identificación del estudiante
        nombre (str): el nombre completo del estudiante
        promedio (float): el promedio académico del estudiante
        """
        node = self.root
        if len(node.ids) == 2*self.t - 1:
            new_root = BNode(self.t)
            new_root.children.append(node)
            self.root = new_root
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, id, nombre, promedio)
        else:
            self._insert_non_full(node, id, nombre, promedio)
    

    def _split_child(self, node, i):
        """
        Divide el hijo i del nodo en dos nuevos nodos y los inserta en el nodo padre.

        parameters:
        --------------
        node (BNode): el nodo padre que se va a dividir
        i (int): la posición del hijo que se va a dividir
        """
        t = self.t
        y = node.children[i]
        z = BNode(t)
        node.children.insert(i+1, z)
        node.ids.insert(i, y.ids[t-1])
        node.nombres.insert(i, y.nombres[t-1])
        node.promedios.insert(i, y.promedios[t-1])
        z.ids = y.ids[t:]
        z.nombres = y.nombres[t:]
        z.promedios = y.promedios[t:]
        if not y.is_leaf():
            z.children = y.children[t:]
            y.children = y.children[:t]
    

    def _insert_non_full(self, node, id, nombre, promedio):
        """
        Inserta un nuevo estudiante en un nodo no lleno del árbol.

        parameters:
        --------------
        node (BNode): el nodo donde se insertará el nuevo estudiante
        id (int): el número de identificación del estudiante
        nombre (str): el nombre completo del estudiante
        promedio (float): el promedio académico del estudiante
        """
        i = len(node.ids) - 1
        if node.is_leaf():
            node.ids.append(0)
            node.nombres.append(0)
            node.promedios.append(0)
            while i >= 0 and id < node.ids[i]:
                node.ids[i+1] = node.ids[i]
                node.nombres[i+1] = node.nombres[i]
                node.promedios[i+1] = node.promedios[i]
                i -= 1
            node.ids[i+1] = id
            node.nombres[i+1] = nombre
            node.promedios[i+1] = promedio
        else:
            while i >= 0 and id < node.ids[i]:
                i -= 1
            i += 1
            if len(node.children[i].ids) == 2*self.t - 1:
                self._split_child(node, i)
                if id > node.ids[i]:
                    i += 1
            self._insert_non_full(node.children[i], id, nombre, promedio)


    def print_tree(self):
        """
        Imprime el árbol en consola.
        """
        self._print_node(self.root)

    def _print_node(self, node, level=0):
        """
        Función auxiliar que imprime un nodo y sus hijos recursivamente en consola.

        parameters:
        --------------
        node (BNode): el nodo actual a imprimir
        level (int): el nivel de profundidad actual del nodo en el árbol
        """
        print("  "*level + f"ids: {node.ids}")
        if not node.is_leaf():
            for child in node.children:
                self._print_node(child, level+1)
                print(" "*level + f"nombres: {child.nombres}")
                print(" "*level + f"promedios: {child.promedios}")

