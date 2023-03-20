from AVL import AVL_Tree

def menu():
    tree = AVL_Tree()
    tree.build_tree_csv("./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv")
    print(f"\n¡se creo el arbol!")

    while True:
        print("\n0. Mostrar el arbol")
        print("1. Insertar un nodo")
        print("2. Eliminar un nodo")
        print("3. Buscar un nodo")
        print("4. Recorrido en orden por nivel")
        print("5. Altura de un nodo")
        print("6. Encontrar el abuelo o tío de un nodo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 0:
            tree.mostrar_arbol()

        elif opcion == 1:
            user_id = input("Ingrese el User_ID (lo convertira en ASCII): ")
            user_id = sum([ord(char) for char in user_id])
            user_name = input("Ingrese el User_Name: ")
            tree.insert(user_id, user_name)

        elif opcion == 2:
            user_id = input("Ingrese el User_ID del nodo que desea eliminar: ")
            try:
                user_id = int(user_id)
            except ValueError:
                print("Por favor, ingrese un número válido para el User_ID.")
                continue
            tree.delete(user_id)

        elif opcion == 3:
            user_id = input("Ingrese el User_ID del nodo que desea buscar: ")
            try:
                user_id = int(user_id)
            except ValueError:
                print("Por favor, ingrese un número válido para el User_ID.")
                continue
            result = tree.Search_Node(tree.root, user_id)
            if result is None:
                print("No se ha encontrado el nodo.")
            else:
                print("Nodo encontrado:")
                print(f"User_ID: {result.user_id}")
                print(f"User_Name: {result.user_name}")

        elif opcion == 4:
            tree.LevelTraversal()

        elif opcion == 5:
            user_id = input("Ingrese el User_ID del nodo para calcular su altura: ")
            try:
                user_id = int(user_id)
            except ValueError:
                print("Por favor, ingrese un número válido para el User_ID.")
                continue
            if user_id is None:
                print("No se ha encontrado el nodo.")
            else:
                height = tree.get_height_node(tree.root,user_id)
                print(f"La altura del nodo con User_ID {user_id} es {height}")

        elif opcion == 6:
            user_id = input("Ingrese el User_ID del nodo para encontrar su abuelo o tío: ")
            try:
                user_id = int(user_id)
            except ValueError:
                print("Por favor, ingrese un número válido para el User_ID.")
                continue
            node = tree.Search_Node(tree.root, user_id)
            if node is None:
                print("No se ha encontrado el nodo.")
            else:
                grandparent = tree.find_grand_parent(tree.root, user_id)
                uncle = tree.find_uncle(tree.root,user_id)
                if grandparent is None:
                    print("El nodo no tiene abuelo.")
                else:
                    print(f"El abuelo del nodo con User_ID {user_id} es {grandparent.user_id}")
                if uncle is None:
                    print("El nodo no tiene tío.")
                else:
                    print(f"El tío del nodo con User_ID {user_id} es {uncle.user_id}")

        elif opcion == 7:
            break
menu()
