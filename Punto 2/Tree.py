"""problema: 
Codificar un árbol DNS en el cual puedas consultar la IP del dominio a buscar, por ejemplo: si buscas Google.com te 
devuelva 8.8.8.8 es decir, su IP"""

from Node import DNSNode
# se crea la clase Arbol DNS como DNSTree
# con metodos para insertar, buscar y recorrer
class DNSTree:
    def __init__(self):
        self.root = None
    # inserta nodos al arbol se requiere de un padre
    def insert(self, name, ip, parent=None):
        if self.root is None:
            self.root = DNSNode(name, ip)
        else:
            P = self.Level_Order_Search(parent)
            if P is None:
                return "No existe el Nodo"
            else:
                P.child.append(DNSNode(name, ip, parent))
    # busca un nodo con el parametro que resive el método y lo devuelve a una variable
    def Level_Order_Search(self, parent):
        """
        Searches and returns the object Node if it is present in the tree.
        Attributes
        ----------
        value: int. value to be searched in the tree.
        """
        traversed = []
        traversed.append(self.root)
        if self.root is None:
            return None
        while traversed != []:
            if traversed[0].name == parent:
                return traversed[0]
            x = traversed.pop(0) 
            if x.child:
                traversed.extend(x.child)
        return None
    # recorre el arbol 
    def Level_Order_traversal(self):
        """
        Prints the level order traversal algorithm
        Attributes
        ----------
        None.
        """
        P = self.root
        traversed = []
        traversed.append(P)
        if P is None:
            return None
        while traversed != []:
            print(traversed[0].name)
            x = traversed.pop(0) 
            if x.child:
                traversed.extend(x.child)