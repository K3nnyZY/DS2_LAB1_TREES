from B_Tree import Tree

tree = Tree(2)

# Insertamos algunos estudiantes
tree.insert(100, "Mario", 4.5)
tree.insert(200, "Maria ", 4.2)
tree.insert(300, "Jose", 2.9)
tree.insert(400, "Luna", 3.8)
tree.insert(500, "Carlos", 3.1)
tree.insert(600, "Ana", 5.0)

# Imprimimos el árbol
tree.print_tree()

# Buscamos un estudiante por su ID
std_id = 300
result = tree.search(std_id)
if result:
    name, grade = result
    print(f"se encontro el estudiante con ID {std_id}: ({name}, {grade})")
else:
    print(f"No se encontró el estudiante con ID {std_id}")

# Insertamos otro estudiante
tree.insert(700, "Andres", 3.8)
tree.print_tree()

std_id = 700
result = tree.search(std_id)
if result:
    name, grade = result
    print(f"Se encontro el estudiante con ID {std_id}: ({name}, {grade})")
else:
    print(f"No se encontró el estudiante con ID {std_id}")