from B_Tree import BTree
from Node import Estudiante

def main():
    arbol = BTree(2)
    
    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Agregar un estudiante")
        print("2. Buscar un estudiante")
        print("3. Actualizar el promedio de un estudiante")
        print("4. listas de estudiantes:")
        print("5. Salir")

        try:
            opcion = int(input("Ingresa el número de la acción deseada: "))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue

        if opcion == 1:
            id = int(input("Ingresa el número de identificación del estudiante: "))
            nombre = input("Ingresa el nombre completo del estudiante: ")
            promedio = float(input("Ingresa el promedio académico del estudiante: "))
            estudiante = Estudiante(id, nombre, promedio)
            arbol.insert(estudiante)

        elif opcion == 2:
            id = int(input("Ingresa el número de identificación del estudiante: "))
            estudiante = arbol.search(id)
            if estudiante:
                print(f"El estudiante {estudiante.nombre} tiene un promedio de {estudiante.promedio}")
            else:
                print("El estudiante no se encuentra en el sistema")

        elif opcion == 3:
            id = int(input("Ingresa el número de identificación del estudiante: "))
            nuevo_promedio = float(input("Ingresa el nuevo promedio académico del estudiante: "))
            arbol.update_promedio(id, nuevo_promedio)

        elif opcion == 4:
            print("lista de estudiantes añadidos")
            Estudiantes = arbol.get_students_list()
            print(Estudiantes)

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, por favor ingresa una opción válida.")
main()