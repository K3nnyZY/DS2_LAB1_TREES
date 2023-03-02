from AVL_Tree import AVLTree

tree = AVLTree()

csv_files = ["./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv"]
user_ids = tree.build_tree(csv_files)

for user_id_ascii, user_name in user_ids:
    tree.insert(user_id_ascii, user_name)

tree.inorder_traversal(tree.root)