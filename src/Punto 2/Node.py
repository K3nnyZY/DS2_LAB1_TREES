# se crea la clase nodo la cual tendra como parametro el nombre, la ip y el padre
class DNSNode():
    def __init__(self, name, ip, parent=None):
        self.name = name
        self.ip = ip
        self.parent = parent
        self.child = []

    def __str__(self) -> str:
        return f"IP {self.ip} corresponde a {self.name} dentro de {self.parent}"
    

    # añade un hijo a un nodo correspondiente(se usa para hacerlo de forma manual)
    def addChild(self, child_node):
        self.child.append(child_node)
    # remueve el hijo de un nodo correspondiente
    def removeChild(self, child_node):
        self.child.remove(child_node)