import csv

class Node:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        left_child = node.left

        if not left_child:
            return node

        right_child_of_left_child = left_child.right

        left_child.right = node
        node.left = right_child_of_left_child

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1

        return left_child


    def rotate_left(self, node):
        right_child = node.right

        if not right_child:
            return node

        left_child_of_right_child = right_child.left

        right_child.left = node
        node.right = left_child_of_right_child

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1

        return right_child


    def insert(self, user_id, user_name):
        if not self.root:
            self.root = Node(user_id, user_name)
            return

        def _insert(current_node, new_node):
            if new_node.user_id < current_node.user_id:
                if not current_node.left:
                    current_node.left = new_node
                else:
                    current_node.left = _insert(current_node.left, new_node)
            else:
                if not current_node.right:
                    current_node.right = new_node
                else:
                    current_node.right = _insert(current_node.right, new_node)

            current_node.height = max(self.height(current_node.left), self.height(current_node.right)) + 1

            balance = self.balance(current_node)

            if balance > 1 and new_node.user_id < current_node.left.user_id:
                return self.rotate_right(current_node)

            if balance < -1 and new_node.user_id > current_node.right.user_id:
                return self.rotate_left(current_node)

            if balance > 1 and new_node.user_id > current_node.left.user_id:
                current_node.left = self.rotate_left(current_node.left)
                return self.rotate_right(current_node)

            if balance < -1 and new_node.user_id < current_node.right.user_id:
                current_node.right = self.rotate_right(current_node.right)
                return self.rotate_left(current_node)

            return current_node

        new_node = Node(user_id, user_name)
        self.root = _insert(self.root, new_node)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"User name: {node.user_name}, User ID (ASCII): {node.user_id}")
            self.inorder_traversal(node.right)

def process_csv_files(csv_files):
    user_ids = set()

    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id_ascii = sum(ord(c) for c in row['User_ID'])
                user_name = row['User_name']
                user_ids.add((user_id_ascii, user_name))

    avl_tree = AVLTree()

    for user_id_ascii, user_name in user_ids:
        avl_tree.insert(user_id_ascii, user_name)

    avl_tree.inorder_traversal(avl_tree.root)


if __name__ == '__main__':
    csv_files = ["./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv"]
    process_csv_files(csv_files)

