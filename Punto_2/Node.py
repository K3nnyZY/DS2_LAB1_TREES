class DNSNode():
    def __init__(self, name, ip, parent=None):
        self.name = name
        self.ip = ip
        self.parent = parent
        self.child = []

    def __str__(self) -> str:
        return f"IP {self.ip} corresponde a {self.name} dentro de {self.parent}"
    
    def addChild(self, child_node):
        self.child.append(child_node)

    def removeChild(self, child_node):
        self.child.remove(child_node)