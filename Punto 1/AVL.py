from Node import Node
import csv

class AVL_Tree():
    def __init__(self) -> None:
        self.root: Node = None


    def delete(self, user_id):
        self.root = self._delete(self.root, user_id)

    def _delete(self, root, user_id):
        if root is None:
            return root

        elif user_id < root.user_id:
            root.left = self._delete(root.left, user_id)

        elif user_id > root.user_id:
            root.right = self._delete(root.right, user_id)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.user_id = temp.user_id
            root.user_name = temp.user_name
            root.right = self._delete(root.right, temp.user_id)

        if root is None:
            return root

        root.level = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.Balance(root)

        if balance > 1 and self.Balance(root.right) >= 0:
            return self.left_rotate(root)

        if balance < -1 and self.Balance(root.left) <= 0:
            return self.right_rotate(root)

        if balance > 1 and self.Balance(root.right) < 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        if balance < -1 and self.Balance(root.left) > 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        return root


    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current



    def Search_Node(self, root: Node, user_id):
        """Función para buscar un nodo según su dato y retornar el nodo si lo encuentra"""
        if root is None:
            return None
        if root.user_id == user_id:
            return root
        if user_id > root.user_id:
            return self.Search_Node(root.right, user_id)
        else: 
            return self.Search_Node(root.left, user_id)


    def insert(self, user_id, user_name):
        if self.root is None:
            self.root = Node(user_id, user_name)
        elif self.Search_Node(self.root, user_id) is not None:
            print("el nodo esta en el arbol")
        else:
            self.root =  self._insert_(self.root, user_id, user_name)


    def _insert_(self, root: Node, user_id, user_name):
        #Si la raíz es nula entonces me retorna el dato del nodo
        if root is None:  
            return Node(user_id, user_name) 
        #Como la idea es insertar un nodo en un AVL, debemos usar su concepto de busqueda
        elif user_id < root.user_id: #Si el dato del nodo que queremos insertar es menor a el nodo en el que estamos
            #Nos movemos al lado izquierdo, llamando a la función de nuevo (recursividad) hasta  quedar en nulo
            #y que el condicional de arriba lo inserte
            root.left = self._insert_(root.left, user_id, user_name) 
        else:#Lo mimso con el lado derecho            
            root.right = self._insert_(root.right, user_id, user_name)

        self.get_level() #calculamos el nivel cada vez que pasados de nodo en nodo para ver si hay un desbalance
        
        #Calculamos el balance a cada uno de nuestros nodos.
        balance = self.Balance(root)
        # Dependiendo del caso de desbalance, se realizan las rotaciones necesarias
        if ((balance < -1) and user_id < root.left.user_id):
            return self.left_rotate(root)
        if (balance > 1 and user_id > root.right.user_id):
            return self.right_rotate(root)
        if (balance < -1 and user_id > root.left.user_id):
            root.left = self.right_rotate(root.left)
            return self.left_rotate(root)
        if (balance > 1 and user_id < root.right.user_id):
            root.right = self.left_rotate(root.right)
            return self.right_rotate(root)
        return root
    

    def get_level(self):
        if self.root.level != 0:
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
        child = root.left
        if child is None:
            return root
        root.left = child.right
        child.right = root
        self.get_level()
        return child
    
    
    def right_rotate(self, root: Node):
        child = root.right
        if child is None:
            return root
        root.right = child.left
        child.left = root
        self.get_level()
        return child

    
    
    def Balance(self, root:Node):
        rheight = self.Search_max(root.right)
        lheight = self.Search_max(root.left)
        if (rheight != 0):
            rheight -= root.level
        if (lheight != 0):
            lheight -= root.level
        return rheight - lheight
    

    def Search_max(self, root:Node):
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
        if root is None:
            return 0
        temp = self.Search_max(root)
        return temp - root.level


    def LevelTraversal(self):
        print("\nLevel Ordel traversal:")
        self.get_level()
        h = self.get_height(self.root)
        for i in range(1, h+2):
            self.current_level(self.root, i)

    
    def current_level(self, root: Node, level):
        if root is None:
            return
        if level == 1:
            print(f"User_name: {root.user_name:}, User_ID (ASCII): {root.user_id}")
        elif level > 1:
            self.current_level(root.left, level-1)
            self.current_level(root.right, level-1)

    
    COUNT = [10]
    def _print_tree_(self, root:Node, space):
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
            existing_user_ids = set()
            for file_path in file_paths:
                with open(file_path, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        user_id = sum([ord(char) for char in row['User_ID']])
                        if user_id not in existing_user_ids:
                            user_name = row['User_name']
                            self.insert(user_id, user_name)
                            existing_user_ids.add(user_id)
