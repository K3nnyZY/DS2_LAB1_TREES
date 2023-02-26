from Node import Node

class AVLTree:
    """AVL tree class and functions
    -----------------
    atributes:
    root = Node"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.recursive_insert(self.root, data)


    def recursive_insert(self, node, data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self.recursive_insert(node.left, data)
        else:
            node.right = self.recursive_insert(node.right, data)

        node.height = 1 + max(self.get_hight(node.left), self.get_hight(node.right))

        balance = self.get_balance(node)

        if balance > 1 and data < node.left.data:
            return self.right_rotation(node)

        if balance < -1 and data > node.right.data:
            return self.left_rotation(node)

        if balance > 1 and data > node.left.data:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        if balance < -1 and data < node.right.data:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node


    def get_hight(self, node):
        if not node:
            return 0
        return node.height


    def get_balance(self, node):
        if not node:
            return 0
        return self.get_hight(node.left) - self.get_hight(node.right)


    def left_rotation(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self.get_hight(node.left), self.get_hight(node.right))
        new_root.height = 1 + max(self.get_hight(new_root.left), self.get_hight(new_root.right))
        return new_root


    def right_rotation(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self.get_hight(node.left), self.get_hight(node.right))
        new_root.height = 1 + max(self.get_hight(new_root.left), self.get_hight(new_root.right))
        return new_root


    def inorder_traversal(self, node):
        # Caso base: si el nodo es nulo, no hay nada que hacer aquí, retornamos una lista vacía
        if not node:
            return []
        # Paso recursivo: llamamos al método para el subárbol izquierdo, obteniendo su lista de valores en inorden
        left_values = self.inorder_traversal(node.left)
        # Agregamos el valor del nodo actual a la lista de valores en inorden
        current_value = [node.data]
        # Paso recursivo: llamamos al método para el subárbol derecho, obteniendo su lista de valores en inorden
        right_values = self.inorder_traversal(node.right)
        # Combinamos las listas de valores en inorden de los subárboles izquierdo y derecho, junto con el valor del nodo actual
        return left_values + current_value + right_values


if __name__ == "__main__":
# Ejemplo de uso
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    print(avl_tree.inorder_traversal(avl_tree.root))  # [10, 20, 25, 30, 40, 50]
