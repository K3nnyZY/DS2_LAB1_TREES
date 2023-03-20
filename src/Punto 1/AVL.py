from Node import Node
import csv
from tkinter import Canvas
import tkinter as tk

class AVL_Tree():
    def __init__(self) -> None:
        self.root: Node = None


    def delete(self, user_id):
        """
        Elimina un nodo con un user_id dado del árbol AVL
        ---------------
        Parameters:
            user_id (int): identificador único del usuario a eliminar
        """
        self.root = self._delete(self.root, user_id)


    def _delete(self, root, user_id):
        """
        Funcion recursiva que elimina un nodo con un user_id dado del subárbol dado
        --------------
        Parameters:
            root (Node): raíz del subárbol
            user_id (int): identificador único del usuario a eliminar
        --------------
        Returns:
            root: Node con la raíz del subárbol actualizado
        """
        if not root: # Si no hay nodo, se devuelve el nodo
            return root
        elif user_id < root.user_id: # Se avanza por el subárbol izquierdo si el user_id es menor al user_id del nodo actual
            root.left = self._delete(root.left, user_id)
        elif user_id > root.user_id: # Se avanza por el subárbol derecho si el user_id es mayor al user_id del nodo actual
            root.right = self._delete(root.right, user_id)
        else: # Se encontró el nodo con el user_id a eliminar
            if not root.left: # Si el nodo no tiene hijo izquierdo
                temp = root.right
                root = None
                return temp
            elif not root.right: # Si el nodo no tiene hijo derecho
                temp = root.left
                root = None
                return temp
            else: # Si el nodo tiene dos hijos
                # Se encuentra el nodo con el user_id más pequeño en el subárbol derecho
                temp = self.get_min_node(root.right)
                # Se reemplaza el user_id del nodo actual por el user_id del nodo encontrado
                root.user_id = temp.user_id
                # Se elimina el nodo encontrado del subárbol derecho
                root.right = self._delete(root.right, temp.user_id)
        if not root:
            return root
        # Se actualiza la altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Se obtiene el factor de equilibrio del nodo actual
        balance = self.Balance(root)
        # Si el nodo está desequilibrado, se realizan rotaciones
        # para reequilibrarlo
        if balance > 1 and self.Balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.Balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.Balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.Balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root



    def get_max(self, root:Node):
        """
        Regresa el nodo mas grande en un subárbol
        ---------------
        Parameters:
            root(Node): Nodo raíz del subárbol en el que se quiere encontrar el nodo con el valor maximo.
        ----------------
        Returns:
        Node: El nodo con el valor maximo en el subárbol.
        """
        while root.right is not None:
            root = root.right
        return root


    def get_min(self, node:Node):
        """
        Función para encontrar el nodo con el valor mínimo en un subárbol.
        --------------
        Parameters:
        node (Node): Nodo raíz del subárbol en el que se quiere encontrar el nodo con el valor mínimo.
        --------------
        Returns:
        Node: El nodo con el valor mínimo en el subárbol.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current


    def Search_Node(self, root: Node, user_id):
        """
        Función para buscar un nodo en el árbol según su ID de usuario y retornar el nodo si lo encuentra.
        ---------------
        Parameters:
        root (Node): Nodo raíz del subárbol en el que se quiere buscar el nodo.
        user_id (int): ID del usuario que se quiere buscar.
        ---------------
        Returns:
        Node: El nodo con el ID de usuario buscado, si lo encuentra. None en caso contrario.
        """
        if root is None:
            # Si el nodo es None, no se ha encontrado el ID del usuario, por lo que se retorna None
            return None
        if root.user_id == user_id:
            # Si se encuentra el nodo con el ID del usuario, se retorna el nodo
            return root
        if user_id > root.user_id:
            # Si el ID del usuario es mayor al ID del nodo actual, se llama recursivamente a Search_Node() sobre el subárbol derecho
            return self.Search_Node(root.right, user_id)
        else:
            # Si el ID del usuario es menor al ID del nodo actual, se llama recursivamente a Search_Node() sobre el subárbol izquierdo
            return self.Search_Node(root.left, user_id)


    def insert(self, user_id, user_name):
        """
        Función para insertar un nodo en el árbol AVL. Si el nodo con el ID del usuario ya existe, imprime un mensaje indicándolo.
        --------------
        Parameters:
        user_id (int): ID del usuario a insertar.
        user_name (str): Nombre del usuario a insertar.
        """
        if self.root is None:
            # Si la raíz es None, se crea un nuevo nodo con los datos del usuario y se establece como la nueva raíz
            self.root = Node(user_id, user_name)
        elif self.Search_Node(self.root, user_id) is not None:
            # Si el nodo con el ID del usuario ya existe en el árbol, se imprime un mensaje indicándolo
            print("el nodo esta en el arbol")
        else:
            # Si el nodo con el ID del usuario no existe en el árbol, se llama a la función _insert_() para insertarlo
            self.root = self._insert_(self.root, user_id, user_name)

    def _insert_(self, root: Node, user_id, user_name):
        """
        Función recursiva para insertar un nodo en el árbol AVL.
        --------------
        Parameters:
        root (Node): Nodo raíz del subárbol en el que se quiere insertar el nodo.
        user_id (int): ID del usuario a insertar.
        user_name (str): Nombre del usuario a insertar.

        Returns:
        Node: El nodo raíz actualizado después de la inserción del nuevo nodo.
        """
        if root is None:
            # Si la raíz es None, se crea un nuevo nodo con los datos del usuario y se retorna
            return Node(user_id, user_name)
        elif user_id < root.user_id:
            # Si el ID del usuario es menor al ID del nodo actual, se llama recursivamente a _insert_() sobre el subárbol izquierdo
            root.left = self._insert_(root.left, user_id, user_name)
        else:
            # Si el ID del usuario es mayor o igual al ID del nodo actual, se llama recursivamente a _insert_() sobre el subárbol derecho
            root.right = self._insert_(root.right, user_id, user_name)
        self.get_level()
        # Se llama a la función get_level() para actualizar el nivel de cada nodo
        balance = self.Balance(root)
        # Se calcula el balance del nodo actual
        if ((balance < -1) and user_id < root.left.user_id):
            # Si el balance es menor a -1 y el ID del usuario es menor al ID del hijo izquierdo del nodo actual, se realiza una rotación hacia la izquierda
            return self.left_rotate(root)
        if (balance > 1 and user_id > root.right.user_id):
            # Si el balance es mayor a 1 y el ID del usuario es mayor al ID del hijo derecho del nodo actual, se realiza una rotación hacia la derecha
            return self.right_rotate(root)
        if (balance < -1 and user_id > root.left.user_id):
            # Si el balance es menor a -1 y el ID del usuario es mayor al ID del hijo izquierdo del nodo actual, se realiza una doble rotación (derecha-izquierda)
            root.left = self.right_rotate(root.left)
            return self.left_rotate(root)
        if (balance > 1 and user_id < root.right.user_id):
            root.right = self.left_rotate(root.right)
            return self.right_rotate(root)
        return root


    def get_level(self):
        """
        Función que actualiza el nivel de cada nodo del árbol según su posición en el mismo.
        --------------
        Parameters:
        None
        """
        if self.root.level != 0:
            # Si el nivel del nodo raíz no es cero, se establece en cero
            self.root.level = 0
        node = self.root
        s = [node]
        while len(s) > 0:
            node = s.pop(0)
            if node.left is not None:
                s.append(node.left)
                node.left.level = node.level + 1
            if node.right is not None:
                s.append(node.right)
                node.right.level = node.level + 1


    def left_rotate(self, root: Node):
        """
        Función que realiza una rotación a la izquierda en el árbol a partir del nodo dado.
        ---------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere realizar la rotación.
        --------------
        Returns:
        Node: El nodo que quedó como raíz del subárbol rotado.
        """
        child = root.left
        if child is None:
            # Si el hijo izquierdo es None, no se puede realizar la rotación y se retorna el nodo actual
            return root
        root.left = child.right
        child.right = root
        self.get_level() # Se actualiza el nivel de cada nodo después de la rotación
        return child

    
    def right_rotate(self, root: Node):
        """
        Función que realiza una rotación a la derecha en el árbol a partir del nodo dado.
        ----------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere realizar la rotación.
        ----------------
        Returns:
        Node: El nodo que quedó como raíz del subárbol rotado.
        """
        child = root.right
        if child is None:
            # Si el hijo derecho es None, no se puede realizar la rotación y se retorna el nodo actual
            return root
        root.right = child.left
        child.left = root
        self.get_level() # Se actualiza el nivel de cada nodo después de la rotación
        return child


    def Balance(self, root:Node):
        """
        Función que calcula el balance del árbol a partir del nodo dado.
        ----------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere calcular el balance.
        ---------------
        Returns:
        int: El balance del árbol a partir del nodo dado.
        """
        rheight = self.Search_max(root.right)
        lheight = self.Search_max(root.left)
        if (rheight != 0):
            rheight -= root.level
        if (lheight != 0):
            lheight -= root.level
        return rheight - lheight


    def Search_max(self, root:Node):
        """
        Función que busca el nodo con la mayor altura a partir del nodo dado.
        -----------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere buscar el nodo con mayor altura.
        -----------------
        Returns:
        int: La altura del nodo con mayor altura a partir del nodo dado.
        """
        if root is None:
            return 0
        node = root
        s = [node]
        while len(s) > 0:
            node = s.pop(0)
            if node.left is not None:
                s.append(node.left)
            if node.right is not None:
                s.append(node.right)
        return node.level


    def get_height(self, root:Node):
        """
        Función que calcula la altura de un subárbol a partir del nodo dado.
        ------------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere calcular la altura del subárbol.
        ------------------
        Returns:
        int: La altura del subárbol a partir del nodo dado.
        """
        if root is None:
            return 0
        temp = self.Search_max(root)
        return temp - root.level + 1


    def get_height_node(self, root: Node, user_id):
        """
        Función que calcula la altura de un nodo específico a partir del nodo dado.
        -------------------
        Parameters:
        root (Node): Nodo a partir del cual se quiere calcular la altura del nodo específico.
        user_id (int): ID del usuario del nodo del cual se quiere calcular la altura.
        ------------------
        Returns:
        int: La altura del nodo específico a partir del nodo dado.
        """
        if root is None:
            return 0
        if root.user_id == user_id:
            return 1
        if user_id > root.user_id:
            return 1 + self.get_height_node(root.right, user_id)
        else:
            return 1 + self.get_height_node(root.left, user_id)


    def LevelTraversal(self):
        """
        Función que imprime los nodos del árbol según su nivel.
        """
        print("\nLevel Order traversal:") # Imprime mensaje informativo
        self.get_level() # Actualiza los niveles de cada nodo
        h = self.get_height(self.root) # Calcula la altura del árbol
        for i in range(1, h+2): # Recorre cada nivel del árbol
            self.current_level(self.root, i)


    def current_level(self, root: Node, level):
        """
        Función auxiliar para imprimir los nodos de un nivel específico del árbol.
        --------------
        Parámetros:
        root (Node): nodo raíz del subárbol
        level (int): nivel del árbol a imprimir
        -------------
        Retorna:
        None
        """
        if root is None: # Si el nodo es nulo, se retorna inmediatamente
            return
        if level == 1: # Si se alcanza el nivel deseado, se imprime el nombre y el ID del usuario
            print(f"User_name: {root.user_name:}, User_ID (ASCII): {root.user_id}")
        elif level > 1: # Si aún no se ha alcanzado el nivel deseado, se llama recursivamente a current_level() con los subárboles izquierdo y derecho
            self.current_level(root.left, level-1)
            self.current_level(root.right, level-1)


    def find_uncle(self, root: Node, user_id):
        """
        Función para encontrar el tío de un nodo dado su ID de usuario.
        -----------
        Parameters:
        root: Node
            El nodo raíz del árbol
        user_id: int
            El ID del usuario del nodo para el que se busca el tío.
        --------
        Returns:
        Node
            El nodo del tío si se encuentra, None de lo contrario.
        """
        if root is None or root.user_id == user_id:
            return None
        parent = self.find_parent(root, user_id)
        if parent is None:
            return None
        grand_parent = self.find_parent(root, parent.user_id)
        if grand_parent is None:
            return None
        if grand_parent.left == parent:
            return grand_parent.right
        else:
            return grand_parent.left


    def find_grand_parent(self, root: Node, user_id):
        """
        Función para encontrar el abuelo de un nodo dado su ID de usuario.
        -----------
        Parameters:
        root: Node
            El nodo raíz del árbol
        user_id: int
            El ID del usuario del nodo para el que se busca el abuelo.
        --------
        Returns:
        Node
            El nodo del abuelo si se encuentra, None de lo contrario.
        """
        if root is None or root.user_id == user_id:
            return None
        parent = self.find_parent(root, user_id)
        if parent is None:
            return None
        return self.find_parent(root, parent.user_id)


    def find_parent(self, root: Node, user_id):
        """
        Función para encontrar el padre de un nodo dado su ID de usuario.
        -----------
        Parameters:
        -----------
        root: Node
            El nodo raíz del árbol
        user_id: int
            El ID del usuario del nodo para el que se busca el padre.
        --------
        Returns:
        Node
            El nodo del padre si se encuentra, None de lo contrario.
        """
        if root is None:
            return None
        if root.left is not None and root.left.user_id == user_id:
            return root
        if root.right is not None and root.right.user_id == user_id:
            return root
        if user_id < root.user_id:
            return self.find_parent(root.left, user_id)
        else:
            return self.find_parent(root.right, user_id)


    COUNT = [10]
    def _print_tree_(self, root:Node, space):
        """Imprime una represencacion para el arbol dado"""
        if (root == None) :
            return
        space += self.COUNT[0]
        self._print_tree_(root.right, space)
        print()
        for i in range(self.COUNT[0], space):
            print(end = " ")
        print(f"{root.user_id}")
        self._print_tree_(root.left, space)

    def print_tree(self,root):
        print("\nrepresetacion grafica del arbol:")
        self._print_tree_(root, 2)


    def build_tree_csv(self, *file_paths):
        """
        Función para construir el árbol a partir de un conjunto de archivos CSV.
        -----------
        parametro:
        file_paths: Lista de rutas de archivos CSV.
        """
        existing_user_ids = set()
        for file_path in file_paths:
            with open(file_path, newline='',encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    user_id = sum([ord(char) for char in row['User_ID']])
                    if user_id not in existing_user_ids:
                        user_name = row['User_name']
                        self.insert(user_id, user_name)
                        existing_user_ids.add(user_id)


    def dibujar_arbol(self, canvas, nodo, x, y, distancia):
        if nodo is not None:
            canvas.create_oval(x, y, x + 30, y + 30, fill='white', outline='black')
            canvas.create_text(x + 15, y + 15, text=str(nodo.user_id))
            if nodo.left is not None:
                canvas.create_line(x + 15, y + 30, x - distancia + 15, y + 60)
                self.dibujar_arbol(canvas, nodo.left, x - distancia, y + 60, distancia // 2)
            if nodo.right is not None:
                canvas.create_line(x + 15, y + 30, x + distancia + 15, y + 60)
                self.dibujar_arbol(canvas, nodo.right, x + distancia, y + 60, distancia // 2)

    def mostrar_arbol(self):
        ventana = tk.Tk()
        ventana.title("Árbol de Usuarios")

        canvas = Canvas(ventana, width=800, height=400, bg='white')
        canvas.pack()

        self.dibujar_arbol(canvas, self.root, 400, 20, 200)

        ventana.mainloop()