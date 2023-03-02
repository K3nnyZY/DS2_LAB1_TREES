from AVL import AVL_Tree

tree = AVL_Tree()

csv_files = ["./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv"]
tree.build_tree(csv_files)

tree.print2D(tree.root)

print("\nlevel order traversal")
tree.printLevelOrder(tree.root)
tree.print2D(tree.root)


print("\n borrar")
tree.delete_node(tree.root, 2359)
tree.printLevelOrder(tree.root)
