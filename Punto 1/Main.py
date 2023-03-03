from AVL import AVL_Tree

tree = AVL_Tree()

tree.build_tree_csv("./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv")

tree.LevelTraversal()
tree.print2D(tree.root)
tree.found_uncle(1141)