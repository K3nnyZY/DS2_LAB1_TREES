from Tree import *

# Instanciando el arbol 
DNSsTree = DNSTree()


# añadiendo los nodos
DNSsTree.insert("root", "0.0.0.0")
DNSsTree.insert(".com", "1.1.1.1", "root")
DNSsTree.insert(".org", "2.2.2.2","root")
DNSsTree.insert("Google.com","8.8.8.8", ".com")

# imprimendo el arbol
DNSsTree.Level_Order_traversal()

# Consultar un nodo especifico y sus parametros
P = DNSsTree.Level_Order_Search(".com")
print(P.child[0])