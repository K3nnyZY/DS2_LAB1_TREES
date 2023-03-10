from Node import Node

class BTree:
    def __init__(self, t):
        self.root = Node(leaf=True)# Crea un nodo raíz vacío y lo asigna al atributo root
        self.t = t # grado t


    def search(self, id):
        """
        Busca un estudiante en el árbol B utilizando su ID.
        -----------------
        Args:
            id: ID del estudiante a buscar.
        -----------------
        Returns:
            El objeto Estudiante correspondiente al ID buscado, o None si no se encontró ningún estudiante con ese ID.
        """
        actual_node = self.root # se inicializa actual_node con el nodo raíz del árbol
        while actual_node is not None: # mientras actual_node no sea None, se seguirá buscando
            i = 0 # se inicializa el índice i con 0
            while i < len(actual_node.keys) and id > actual_node.keys[i].id: # mientras i sea menor que la longitud de las claves del nodo actual y el ID buscado sea mayor que el ID de la clave en la posición i, se incrementa i
                i += 1
            if i < len(actual_node.keys) and id == actual_node.keys[i].id: # si i es menor que la longitud de las claves del nodo actual y el ID buscado es igual al ID de la clave en la posición i, se devuelve el objeto Estudiante correspondiente a la clave en la posición i
                return actual_node.keys[i]
            elif actual_node.leaf: # si el nodo actual es una hoja y el ID buscado no se encontró, se devuelve None
                return None
            else: # si el nodo actual no es una hoja y el ID buscado no se encontró, se continúa buscando en el hijo correspondiente a la posición i
                actual_node = actual_node.children[i]


    def insert(self, estudiante):
        """
        Inserta un objeto Estudiante en el árbol B.
        ----------------
        Args:
            estudiante: objeto Estudiante a insertar.
        """
        if self.root.keys: # Si el nodo raíz tiene claves (es decir, si el árbol no está vacío)
            if len(self.root.keys) == 2 * self.t - 1: # Si el nodo raíz tiene el número máximo de claves permitidas, se divide en dos nodos y se crea un nuevo nodo raíz
                new_root = Node()
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                self.root = new_root
            self._insert_non_full(self.root, estudiante) # Se inserta el estudiante en el árbol sin tener que crear un nuevo nodo
        else:
            self.root.keys.append(estudiante) # Si el árbol está vacío, se inserta el estudiante en la raíz del árbol


    def _insert_non_full(self, actual_node, estudiante):
        """
        Inserta un objeto Estudiante en un nodo del árbol B que no está lleno.
        -----------------
        Args:
            actual_node: nodo en el que se debe realizar la inserción.
            estudiante: objeto Estudiante a insertar.

        Returns:
            Nada.
        """
        i = 0 # Inicializa el índice i a cero
        while i < len(actual_node.keys) and estudiante.id > actual_node.keys[i].id: # Mientras i sea menor que el número de claves en actual_node y el id del estudiante sea mayor que la clave en la posición i
            i += 1 # Incrementa i en uno
        if actual_node.leaf: # Si actual_node es una hoja
            actual_node.keys.insert(i, estudiante) # Se inserta el estudiante en la posición i de la lista de claves del nodo actual_node
        else: # Si actual_node no es una hoja
            if len(actual_node.children[i].keys) == (2 * self.t) - 1: # Se encuentra el hijo apropiado y se verifica si está lleno
                self._split_child(actual_node, i) # Si el hijo está lleno, se divide en dos
                if estudiante.id > actual_node.keys[i].id:
                    i += 1
            self._insert_non_full(actual_node.children[i], estudiante) # Se inserta el estudiante en el hijo apropiado


    def _split_child(self, parent_node, child_index):
        """
        Divide un nodo hijo en dos durante la inserción de un objeto Estudiante en el árbol B.
        -------------------
        Args:
            parent_node: nodo padre del nodo hijo que se va a dividir.
            child_index: índice del nodo hijo que se va a dividir.
        """
        t = self.t # Se obtiene el valor de t del árbol B
        child_node = parent_node.children[child_index] # Se obtiene el nodo hijo que se va a dividir
        new_child_node = Node(leaf=child_node.leaf) # Se crea un nuevo nodo hijo con la misma característica de hoja del nodo hijo original
        parent_node.children.insert(child_index + 1, new_child_node) # Se inserta el nuevo nodo hijo en la lista de hijos del nodo padre
        parent_node.keys.insert(child_index, child_node.keys[t-1]) # Se inserta la clave central del nodo hijo original en el nodo padre
        new_child_node.keys = child_node.keys[t:] # Se copian las claves de la mitad derecha del nodo hijo original en el nuevo nodo hijo
        child_node.keys = child_node.keys[:t-1] # Se eliminan las claves de la mitad derecha del nodo hijo original
        if not child_node.leaf: # Si el nodo hijo original no es una hoja
            new_child_node.children = child_node.children[t:] # Se copian los hijos de la mitad derecha del nodo hijo original en el nuevo nodo hijo
            child_node.children = child_node.children[:t] # Se eliminan los hijos de la mitad derecha del nodo hijo original


    def update_promedio(self, id, nuevo_promedio):
        """
        Actualiza el promedio de un estudiante con un ID específico en el árbol B.
        -----------------
        Args:
            id: ID del estudiante cuyo promedio se actualizará.
            nuevo_promedio: nuevo valor del promedio del estudiante.
        """
        estudiante = self.search(id) # Se busca el estudiante con el ID especificado
        if estudiante is not None: # Si se encuentra el estudiante
            estudiante.promedio = nuevo_promedio # Se actualiza el promedio del estudiante
            actual_node = self.root # Se inicializa el nodo actual como la raíz del árbol
            while True: # Se repite hasta que se encuentre el estudiante
                i = 0
                while i < len(actual_node.keys) and id > actual_node.keys[i].id:
                    i += 1 # Se busca la posición donde debería estar el estudiante en la lista de claves del nodo actual
                if id == actual_node.keys[i].id: # Si se encuentra el estudiante en el nodo actual, se actualiza el promedio del estudiante
                    actual_node.keys[i].promedio = nuevo_promedio
                    break
                elif actual_node.leaf: # Si el nodo actual es una hoja y no se encontró el estudiante, se sale del ciclo
                    break
                else: # Si el nodo actual no es una hoja y no se encontró el estudiante, se continúa la búsqueda en el hijo correspondiente a la posición i
                    y = actual_node.children[i]
                    if len(y.keys) == (2 * self.t) - 1: # Si el hijo está lleno, se divide en dos
                        self._split_child(actual_node, i)
                        if id > actual_node.keys[i].id:
                            i += 1
                    actual_node = actual_node.children[i]
        else: # Si no se encuentra el estudiante, se muestra un mensaje indicando que no se encontró el estudiante
            print("Estudiante no encontrado.")


    def get_students_list(self):
        """
        Devuelve una lista de todos los estudiantes en el árbol B en orden ascendente de ID.
        ------------------
        Returns:
            Una cadena de texto que contiene una representación de cada estudiante en el árbol B separada por saltos de línea.
        """
        students_list = [] # Se crea una lista vacía para almacenar los estudiantes
        node_stack = [self.root] # Se crea una pila y se agrega la raíz del árbol
        while node_stack: # Se repite hasta que se procesen todos los nodos en la pila
            node = node_stack.pop() # Se saca el nodo en la cima de la pila
            for i in range(len(node.keys)):
                if not node.leaf: # Si el nodo no es una hoja, se agrega su hijo correspondiente a la pila
                    node_stack.append(node.children[i])
                students_list.append(node.keys[i]) # Se agrega el estudiante a la lista de estudiantes
            if not node.leaf: # Si el nodo no es una hoja, se agrega su último hijo a la pila
                node_stack.append(node.children[-1])
        return "\n".join(str(estudiante) for estudiante in students_list) # Se devuelve una cadena de texto que contiene una representación de cada estudiante en la lista separada por saltos de línea

