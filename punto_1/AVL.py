from node import Node
import csv

class AVL_Tree:

    def __init__(self):
        self.root = None

    def insert(self, root, user_id, user_name):
		#Se inserta normal el nodo como si fuera un arbol binario de busqueda
        if not root:
            return Node(user_name, user_id)
        elif user_id > root.user_id:
            root.left = self.insert(root.left, user_id, user_name)
        else:
            root.right = self.insert(root.right, user_id, user_name)
        
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and user_id > root.left.user_id:
            return self.right_rotate(root)
        
        if balance < -1 and user_id > root.right.user_id:
            return self.left_rotate(root)
        
        if balance > 1 and user_id > root.left.user_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and user_id > root.right.user_id:
            root.right = self.rigth_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    

    def left_rotate(self, z):
        y = z.right
        T2 =  y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        
        return y
    

    def right_rotate(self, z):

        y = z.left
        T3 =  y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y 
    

    def get_height(self, root):
        if not root:
            return 0
        return root.height
    

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) -  self.get_height(root.right)


    def build_tree(self, csv_files):
        user_ids = {}

        for filename in csv_files:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    user_id_ascii = sum(ord(c) for c in row['User_ID'])
                    user_name = row['User_name']
                    if user_id_ascii not in user_ids.keys():
                        user_ids[user_id_ascii] = user_name

        print(f"\nlos datos del user id cambiados a codigo ascii \n{user_ids}")
        for user_id_ascii in user_ids.keys():
            self.root = self.insert(self.root, user_id_ascii, user_ids[user_id_ascii])


    def level_order_traversal(self, node):
        if node is None:
            return
        queue = [node]
        while queue:
            root = queue.pop(0)
            print(f"User name: {root.user_name}, User ID (ASCII): {root.user_id}")
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)


    def printLevelOrder(self,root):
        h = self.get_height(root)
        for i in range(1, h+1):
            self.printCurrentLevel(root, i)

    # Funcion para imprimir los nodos en un nivel
    def printCurrentLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(f"User name: {root.user_name}, User ID (ASCII): {root.user_id}")
        elif level > 1:
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)


    def delete_node(self, root, user_id):
        # Step 1 - Perform standard BST delete
        if not root:
            return root
        elif user_id < root.user_id:
            root.left = self.delete_node(root.left, user_id)
        elif user_id > root.user_id:
            root.right = self.delete_node(root.right, user_id)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.user_id = temp.user_id
            root.user_name = temp.user_name
            root.right = self.delete_node(root.right, temp.user_id)
        
        # If the tree has only one node, return it
        if not root:
            return root
        
        # Step 2 - Update the height of the current node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        
        # Step 3 - Get the balance factor of the current node
        balance = self.get_balance(root)
        
        # Step 4 - If the node is unbalanced, perform rotations
        
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)
    

    COUNT = [10]
    def print2DUtil(self, root, space) :
    
        if (root == None) :
            return
    
        space += self.COUNT[0]
    
        self.print2DUtil(root.right, space)
    

        print()
        for i in range(self.COUNT[0], space):
            print(end = " ")
        print(root.user_id)
    
        # Process left child
        self.print2DUtil(root.left, space)
    
    # Wrapper para la funcion print2DUtil()
    def print2D(self,root) :
        
        
        self.print2DUtil(root, 2)
    