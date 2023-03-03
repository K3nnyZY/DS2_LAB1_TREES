import tkinter as tk
from AVL import AVL_Tree

class App:
    def __init__(self, root):
        self.tree = AVL_Tree()
        self.tree.build_tree_csv("./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv")

        root.title("Árbol AVL")
        root.geometry("800x500")

        self.label = tk.Label(root, text="\n¡Se creó el árbol!\n", font=("Arial", 14))
        self.label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="User_ID (lo convertira en caracteres ASCII):").grid(row=0, column=0)
        self.user_id_entry = tk.Entry(self.frame)
        self.user_id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="User_Name:").grid(row=1, column=0)
        self.user_name_entry = tk.Entry(self.frame)
        self.user_name_entry.grid(row=1, column=1)

        self.extra_label = tk.Label(self.frame, text="Funciones extras:")
        self.extra_label.grid(row=13, column=0)
        self.print_button = tk.Button(self.frame, text="Imprimir árbol", command=self.print_tree)
        self.print_button.grid(row=14, column=0)

        self.insert_button = tk.Button(self.frame, text="Insertar nodo", command=self.insert_node)
        self.insert_button.grid(row=2, column=0)

        tk.Label(self.frame, text="User_ID del nodo a eliminar:").grid(row=3, column=0)
        self.delete_entry = tk.Entry(self.frame)
        self.delete_entry.grid(row=3, column=1)

        self.delete_button = tk.Button(self.frame, text="Eliminar nodo", command=self.delete_node)
        self.delete_button.grid(row=4, column=0)

        tk.Label(self.frame, text="User_ID del nodo a buscar:").grid(row=5, column=0)
        self.search_entry = tk.Entry(self.frame)
        self.search_entry.grid(row=5, column=1)

        self.search_button = tk.Button(self.frame, text="Buscar nodo", command=self.search_node)
        self.search_button.grid(row=6, column=0)

        self.traversal_button = tk.Button(self.frame, text="Recorrido en orden por nivel", command=self.traversal)
        self.traversal_button.grid(row=15, column=0)

        tk.Label(self.frame, text="User_ID del nodo para calcular su altura:").grid(row=8, column=0)
        self.height_entry = tk.Entry(self.frame)
        self.height_entry.grid(row=8, column=1)

        self.height_button = tk.Button(self.frame, text="Calcular altura", command=self.get_height)
        self.height_button.grid(row=9, column=0)

        tk.Label(self.frame, text="User_ID del nodo para encontrar su abuelo o tío:").grid(row=10, column=0)
        self.grandparent_entry = tk.Entry(self.frame)
        self.grandparent_entry.grid(row=10, column=1)

        self.grandparent_button = tk.Button(self.frame, text="Encontrar abuelo o tío", command=self.get_grandparent)
        self.grandparent_button.grid(row=11, column=0)

        self.quit_button = tk.Button(self.frame, text="Salir", command=root.quit)
        self.quit_button.grid(row=18, column=0)

    def print_tree(self):
        result = self.tree.print_tree(self.tree.root)
        self.label.config(text=result, fg="black")
        self.label.config(text="Árbol mostrado en la consola.", fg="green")

    def insert_node(self):
        user_id = self.user_id_entry.get()
        user_name = self.user_name_entry.get()
        if user_id and user_name:
            user_id = sum([ord(char) for char in user_id])
            self.tree.insert(user_id, user_name)
            self.user_id_entry.delete(0, tk.END)
            self.user_name_entry.delete(0, tk.END)
            self.label.config(text="Nodo insertado correctamente.", fg="green")
        else:
            self.label.config(text="Por favor, ingrese un User_ID y User_Name válidos.", fg="red")

    def delete_node(self):
        user_id = self.delete_entry.get()
        if user_id:
            try:
                user_id = int(user_id)
                self.tree.delete(user_id)
                self.delete_entry.delete(0, tk.END)
                self.label.config(text="Nodo eliminado correctamente.", fg="green")
            except ValueError:
                self.label.config(text="Por favor, ingrese un User_ID válido.", fg="red")
        else:
            self.label.config(text="Por favor, ingrese un User_ID para eliminar.", fg="red")

    def search_node(self):
        user_id = self.search_entry.get()
        if user_id:
            try:
                user_id = int(user_id)
                result = self.tree.Search_Node(self.tree.root, user_id)
                if result is None:
                    self.label.config(text="No se ha encontrado el nodo.", fg="red")
                else:
                    self.label.config(text=f"Nodo encontrado:\nUser_ID: {result.user_id}\nUser_Name: {result.user_name}", fg="green")
                self.search_entry.delete(0, tk.END)
            except ValueError:
                self.label.config(text="Por favor, ingrese un User_ID válido.", fg="red")
        else:
            self.label.config(text="Por favor, ingrese un User_ID para buscar.", fg="red")

    def traversal(self):
        self.tree.LevelTraversal()
        self.label.config(text="Recorrido en orden por nivel mostrado en la consola.", fg="green")

    def get_height(self):
        user_id = self.height_entry.get()
        if user_id:
            try:
                user_id = int(user_id)
                height = self.tree.get_height_node(self.tree.root, user_id)
                if height is None:
                    self.label.config(text="No se ha encontrado el nodo.", fg="red")
                else:
                    self.label.config(text=f"La altura del nodo con User_ID {user_id} es {height}.", fg="green")
                self.height_entry.delete(0, tk.END)
            except ValueError:
                self.label.config(text="Por favor, ingrese un User_ID válido.", fg="red")
        else:
            self.label.config(text="Por favor, ingrese un User_ID para calcular su altura.", fg="red")

    def get_grandparent(self):
        user_id = self.grandparent_entry.get()
        if user_id:
            try:
                user_id = int(user_id)
                node = self.tree.Search_Node(self.tree.root, user_id)
                if node is None:
                    self.label.config(text="No se ha encontrado el nodo.", fg="red")
                else:
                    grandparent = self.tree.find_grand_parent(self.tree.root, user_id)
                    uncle = self.tree.find_uncle(self.tree.root, user_id)
                    message = ""
                    if grandparent is None:
                        message += "El nodo no tiene abuelo.\n"
                    else:
                        message += f"El abuelo del nodo con User_ID {user_id} es {grandparent.user_id}.\n"
                    if uncle is None:
                        message += "El nodo no tiene tío."
                    else:
                        message += f"El tío del nodo con User_ID {user_id} es {uncle.user_id}."
                    self.label.config(text=message, fg="green")
                self.grandparent_entry.delete(0, tk.END)
            except ValueError:
                self.label.config(text="Po favor, ingrese un User_ID válido.", fg="red")
        else:
            self.label.config(text="Por favor, ingrese un User_ID para encontrar su abuelo o tío.", fg="red")

root = tk.Tk()
app = App(root)
root.mainloop()





